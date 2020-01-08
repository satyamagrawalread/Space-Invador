import pygame
import random
from math import *
pygame.init()
screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Space Invador: Designed by SATYAM")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

playerimg=pygame.image.load("ufo1.png")
PlayerX=(35/80)*(screen_width)
PlayerY=(5/6)*(screen_height)
Xchange=0
Ychange=0

def player(x,y):
    screen.blit(playerimg,(x,y))

num_of_enemies=20
enemyimg=[]
enemyX=[]
enemyY=[]
en_X_change=[]
en_Y_change=[]

limit=100

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,screen_width-64))
    enemyY.append(random.randint(0,limit))
    en_X_change.append(5)
    en_Y_change.append(40)

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
background=pygame.image.load("back.png")


bulletimg=pygame.image.load("bullet.png")
bulletX=(35/80)*(screen_width)
bulletY=(5/6)*(screen_height)
bullet_X_change=0
bullet_Y_change=0

def bullet_fire(x,y):
    screen.blit(bulletimg,(x+16,y-10))

def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance=sqrt(pow(enemyX-bulletX,2)+pow(enemyY-bulletY,2))
    if(distance<27):
        return True
def iscollision_1(enemyX,enemyY,PlayerX,PlayerY):
    dist=sqrt(pow(enemyX[i]-PlayerX,2)+pow(enemyY[i]-PlayerY,2))
    if(dist<64):
        return True


score_value=0
font=pygame.font.Font('freesansbold.ttf',32)

textX=10
textY=10

def score_card(x,y):
    score=font.render("SCORE : "+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

over_font=pygame.font.Font("freesansbold.ttf",64)

def game_over_text():
    over_sc=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_sc,(200,200))



running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                Xchange=-5
            if event.key==pygame.K_RIGHT:
                Xchange=5
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                Xchange=0

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                Ychange=-5
            if event.key==pygame.K_DOWN:
                Ychange=5

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                Ychange=0

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if(bulletY<=0):
                    bulletX=PlayerX
                    bulletY=PlayerY
                    bullet_Y_change=0
                if(bulletX==PlayerX and bulletY==PlayerY):
                    bullet_fire(bulletX,bulletY)
                    bullet_Y_change=-15
                    bulletY+=bullet_Y_change
            
    if(bulletY>0 and bulletY<PlayerY):
        bulletY+=bullet_Y_change
        bullet_fire(bulletX,bulletY,)

    
    
        
    PlayerX+=Xchange
    PlayerY+=Ychange

    
    
    if(PlayerX<0):
        PlayerX=0
    if(PlayerX>736):
        PlayerX=736

    if(PlayerY<0):
        PlayerY=0
    if(PlayerY>screen_height-64):
        PlayerY=screen_height-64

    for i in range(num_of_enemies):
        if(enemyX[i]<0):
            en_X_change[i]=5
            enemyY[i]+=40
        if(enemyX[i]>screen_width-64):
            en_X_change[i]=-5
            enemyY[i]+=40
        enemyX[i]+=en_X_change[i]
        collision=iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY=-1
            score_value+=1
            enemyX[i]=random.randint(0,screen_width-64)
            enemyY[i]=random.randint(0,100)
        enemy(enemyX[i],enemyY[i],i)
    
    for i in range(num_of_enemies):
        collision_1=iscollision_1(enemyX,enemyY,PlayerX,PlayerY)
        if (collision_1 or enemyY[i]>screen_height):
            for i in range(num_of_enemies):
                enemyY[i]=2000
    for i in range(num_of_enemies):
        if(enemyY[i]>1000):
            game_over_text()


    score_card(textX,textY)

    

    
    
    player(PlayerX,PlayerY)
    
    pygame.display.update()
pygame.quit()
quit()

