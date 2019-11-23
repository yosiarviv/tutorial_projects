import pygame
from network import Network
import pickle
pygame.font.init()

width = 500
height = 500
win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Client")


class Button:
    def __init__(self, text , x , y , color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self,win):
        pygame.draw.rect(win, self.color , (self.x,self.y,self.width,self.height))
        font = pygame.font.SysFont("comicsans",40)
        text = font.render(self.txt,1,(255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2)), (self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self , pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False

def redrawWindow(win,game,p):
    win.fill((128,128,128))
    pass

btns =


def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()
    p2 = n.send(p)

    while run:
        clock.tick(60)
        p2 = n.send(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win,p,p2)

main()