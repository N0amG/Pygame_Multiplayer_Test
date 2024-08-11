import socket
import pickle
import _thread

import sys

from player import Player

server = "192.168.1.75"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
    
except socket.error as e:
    print(str(e))

s.listen(2)

players = [Player(0, 0, 50, 50, (0, 255, 0)), Player(100, 100, 50, 50, (255, 0, 0))]

print("Waiting for a connection, Server Started")


def threaded_client(conn, player):
    print("Player: ", player)
    conn.send(pickle.dumps(players[player]))

    while True:
        data = pickle.loads(conn.recv(2048))
        players[player] = data
        
        reply = players[1 - player]
        if not data:
            print("Disconnected")
            break
        print("Received: ", data)
        conn.sendall(pickle.dumps(reply))
    
    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    _thread.start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1