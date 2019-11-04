import pygame
from network import Network
from player import Player
width = 500
height = 500
win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Client")



def redrawWindow(win,player,player2):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    startPos = read_pos(n.getPos())

    p = Player(startPos[0],startPos[1],100,100,(0,255,0))
    p2 = Player(0,0,100,100,(255,0,0))
    while run:
        p2Pos = read_pos(n.send(make_pos((p.x,p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win,p,p2)

main()