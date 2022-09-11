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


enimyImg = pygame.image.load('alien.png')
enimyX = 30
enimyY = random.randrange(00, 90)

def enimy():
    screen.blit(enimyImg, (enimyX, enimyY))

def player(x, y):
    screen.blit(playerImg, (x, y))

FPS = 60
running = True

while running:

    clock = pygame.time.Clock()
    clock.tick(FPS)

    screen.fill((20, 30, 29))

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



    enimies = 0
    for i in range(7):
        enimy()
        if enimies < 7:
            enimy()
            enimyX += random.randrange(60, 90)
        else:
            pass

    player(playerX, playerY)

    pygame.display.update()
