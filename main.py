import pygame
import time
import random

if __name__ == '__main__':
    pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0


enimyImg = pygame.image.load('enimy.png')
enimyX = random.randrange(60, 700)
enimyY = random.randrange(30, 90)
enimyX_change = 2
enimyY_change = 25

def enimy(x, y):
    screen.blit(enimyImg, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))

FPS = 60
running = True

while running:

    screen.fill((20, 30, 29))
    clock = pygame.time.Clock()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            moving = True
            if event.key == pygame.K_LEFT and moving == True:
                playerX_change = -3
            elif event.key == pygame.K_RIGHT:
                playerX_change = 3
            elif event.key == pygame.K_UP:
                playerY_change = -3
            elif event.key == pygame.K_DOWN:
                playerY_change = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                moving = False
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
                moving = False

    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    elif playerY <= 0:
        playerY = 0
    elif playerY > 536:
        playerY = 536

    

    player(playerX, playerY)
    enimy(enimyX, enimyY)
    if enimyX > 736:
        enimyY += enimyY_change
        enimyY_change += 0
        enimyX_change -= 2
    if enimyX <= 0:
        enimyX = 0
        enimyY += enimyY_change
        enimyY_change += 0
        enimyX_change += 2
    enimyX += enimyX_change
    pygame.display.update()
