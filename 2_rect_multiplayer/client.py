import pygame
from network import Network
from player import Player

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

def redrawWindow(win,player, player2):
    win.fill((0,0,0))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        
        p2 = n.send(p)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p, p2)

main()