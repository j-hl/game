from platform import platform
from re import T
from turtle import goto
from unittest import skip
import pygame
import sys

pygame.init()
screen_high=1207
screen_width=2400
hintergrund=pygame.image.load("Grafiken/hintergrund2.png")
screen=pygame.display.set_mode([screen_width,screen_high])
clock=pygame.time.Clock()
pygame.display.set_caption("Game") 


stehen=pygame.image.load("Grafiken/stand.png")
sprung=pygame.image.load("Grafiken/sprung.png")
rechtsGehen = [pygame.image.load("Grafiken/rechts1.png"),pygame.image.load("Grafiken/rechts2.png"),pygame.image.load("Grafiken/rechts3.png"),pygame.image.load("Grafiken/rechts4.png"),pygame.image.load("Grafiken/rechts5.png"),pygame.image.load("Grafiken/rechts6.png"),pygame.image.load("Grafiken/rechts7.png"),pygame.image.load("Grafiken/rechts8.png")]
linksGehen = [pygame.image.load("Grafiken/links1.png"),pygame.image.load("Grafiken/links2.png"),pygame.image.load("Grafiken/links3.png"),pygame.image.load("Grafiken/links4.png"),pygame.image.load("Grafiken/links5.png"),pygame.image.load("Grafiken/links6.png"),pygame.image.load("Grafiken/links7.png"),pygame.image.load("Grafiken/links8.png")]
plat=pygame.Rect(400,800,200,20)
plat1=pygame.Rect(800,600,200,20)
boden=pygame.Rect(0,1100,2400,1)
def zeichnen(liste):
    global schriteLinks, schriteRechts
    screen.blit(hintergrund,(0,0))          
    if schriteRechts==63:
        schriteRechts=0
    if schriteLinks==63:
        schriteLinks=0
    if liste[0]:
        screen.blit(linksGehen[schriteLinks//8],(x,y))
    if liste[1]:
        screen.blit(rechtsGehen[schriteRechts//8],(x,y))
    if liste[2]:
        screen.blit(stehen,(x,y))
    if liste[3]:
        screen.blit(sprung,(x,y))
    pygame.draw.rect(screen,(155,0,0),plat)
    pygame.draw.rect(screen,(155,0,0),plat1)
    pygame.display.update()
x=300
y=300
ges=5
breite=100
hohe=100
fall=6



test=1
go=True
sprungvar=-16
richtg=[0,0,0,0]
schriteRechts=0
schriteLinks=0
while go:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:sys.exit()
    spielerRechteck=pygame.Rect(x,y,70,135)
    gedruckt=pygame.key.get_pressed()
    richtg=[0,0,1,0]
    if not spielerRechteck.colliderect(boden or plat or plat1):
        if abs(spielerRechteck.bottom-boden.top)>0 and not spielerRechteck.colliderect(plat) and not spielerRechteck.colliderect(plat1):
            y+=fall
        if abs(spielerRechteck.bottom-plat.top)<5:
            y+=fall
        if abs(spielerRechteck.bottom-plat1.top)<5:
            y+=fall
    if gedruckt[pygame.K_UP] and sprungvar==-20 and spielerRechteck.colliderect(plat1):
           sprungvar=19
    if gedruckt[pygame.K_UP] and sprungvar==-20 and spielerRechteck.colliderect(plat):
           sprungvar=19
    if gedruckt[pygame.K_UP] and sprungvar==-20 and spielerRechteck.colliderect(boden):
           sprungvar=19
    if gedruckt[pygame.K_RIGHT] and not spielerRechteck.right > screen_width:
            x+=ges
            richtg=[0,1,0,0]
            schriteRechts+=1
    if gedruckt[pygame.K_LEFT] and not spielerRechteck.left < 0:
            x-=ges
            richtg=[1,0,0,0]
            schriteLinks+=1
    if sprungvar>=-19:
        n=1
        if sprungvar<=0:
            n=0
        richtg=[0,0,0,1]
        y-=(sprungvar**2)*0.17*n
        sprungvar-=1
    if richtg[2]or richtg[3]:
        schriteRechts=0
        schriteLinks=0
    zeichnen(richtg)
    clock.tick(60)
    