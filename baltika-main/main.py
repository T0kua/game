import pygame
import os
import random

pygame.init()

width = 600
height = 800
fps = 260

screen = pygame.display.set_mode((width,height))
os.system('pause')
pygame.display.set_caption('piano')

white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
color = [white,black,green]

clock = pygame.time.Clock()
myself = str(__file__).replace("main.py","Nainai.mp3")# !

ggLoad = myself.replace("Nainai.mp3","gg.png")
gg = pygame.image.load(ggLoad)

baltikaLoad = myself.replace("Nainai.mp3","baltika.png")
baltika = pygame.image.load(baltikaLoad)

game = True

pygame.mixer.music.load(myself)
pygame.mixer.music.play(-1)
class player() :
    def __init__(self) :
        self.x = 2
        self.score = 0
        self.pos = (300,690)
        self.color = color[0]

class Rect() :
    def __init__(self,x,y) :
        self.x = x
        self.y = y

rect0 = Rect(30,0)
rect1 = Rect(230,-300)
rect2 = Rect(430,-600)

rect = [rect0,rect1,rect2]

player = player()

def Input() :
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_LEFT] :
        player.x = 1
    elif keystate[pygame.K_DOWN] :
        player.x = 2
    elif keystate[pygame.K_RIGHT] :
        player.x = 3
def Draw() :
    screen.fill(color[1])
    pygame.draw.rect(screen,color[0],(200,0,1,height),0)
    pygame.draw.rect(screen,color[0],(400,0,1,height),0)
    for i in rect :
        screen.blit(baltika,(i.x + 40 ,i.y,150,150))
        #pygame.draw.rect(screen,color[0],(i.x,i.y,150,150),0)
        i.y += 1.6
    screen.blit(gg,player.pos)
    #pygame.draw.circle(screen,player.color,player.pos,70) # drawing player
    pygame.display.flip()
def Logic() :
    global fps
    fps += player.score % fps + 0.6
    clock.tick(fps)
    player.color = color[0]
    if player.x == 1 :
        player.pos = (40,670)
    elif player.x == 2 :
        player.pos = (240,670)
    elif player.x == 3 :
        player.pos = (440,670)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            print(player.score)
            os.system('pause')
            exit()
    for i in rect :
        print(i.x)
        if i.y >= 760 :
            pygame.mixer.music.stop()
            os.system('pause')
            exit()
        if i.x + 10 == player.pos[0] and i.y >= 600 and i.y <= 760 :
            player.color = color[2]
            player.score += 100
            if random.randint(1,3) == 1 :
                i.x = 30
            if random.randint(1,3) == 2 :
                i.x = 230
            if random.randint(1,3) == 3 :
                i.x = 430
            i.y = random.randint(-200,-130)
while True :
    Input()
    Draw()
    Logic()
