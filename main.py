import pygame
import time
import random
from time import sleep
import math

if __name__ == '__main__':
    pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

galaxyImg = pygame.image.load('galaxy.jpg')

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0


num_of_enimies = 6
enimyImg = []
enimyX = []
enimyY = []
enimyX_change = []
enimyY_change = []
for i in range(num_of_enimies):
    enimyImg.append(pygame.image.load('enimy.png'))
    enimyX.append(random.randrange(60, 700))
    enimyY.append(random.randrange(30, 90))
    enimyX_change.append(2)
    enimyY_change.append(25)

bulletImg = pygame.image.load('bullet.png')
bulletX = playerX + 16
bulletY = playerY - 16
bulletY_change = 10
bullet_state = "ready"
bullet_count = 2

def enimy(x, y, i):
    screen.blit(enimyImg[i], (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))

def fire(x, y):
    global bullet_count
    global bullet_state
    screen.blit(bulletImg, (x, y))
    bullet_state = 'fire'

def isCollision(enimyX, enimyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enimyX - bulletX, 2) + math.pow(bulletY - enimyY, 2))
    if distance < 27:
        return True
    else:
        return False


FPS = 60
running = True
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

game_over = pygame.font.Font('freesansbold.ttf', 64)
gameoverX = 300
gameoverY = 226

def game_over_text():
    gameover_txt = font.render('GAMEOVER', True, (255, 255, 255))
    screen.blit(gameover_txt, (gameoverX, gameoverY))

def show_score(x, y):
    score_txt = font.render('Score: ' + str(score), True, (255, 255, 255))
    screen.blit(score_txt, (x, y))

while running:

    screen.fill((20, 30, 29))
    clock = pygame.time.Clock()
    clock.tick(FPS)

    screen.blit(galaxyImg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            moving = True
            if event.key == pygame.K_LEFT and moving == True:
                playerX_change = -4
            elif event.key == pygame.K_RIGHT:
                playerX_change = 4
            elif event.key == pygame.K_UP:
                playerY_change = -4
            elif event.key == pygame.K_DOWN:
                playerY_change = 4
            elif event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletX = playerX + 16
                    fire(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                moving = False
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
                moving = False


    if bullet_state == 'fire':
        fire(bulletX, bulletY)
        bulletY -= bulletY_change

    if bulletY <= 0:
        bulletX = playerX + 16
        bulletY = playerY - 10
        bullet_state = 'ready'   

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

    for i in range(num_of_enimies):

        if enimyY[i] > 200:
            for j in range(num_of_enimies):
                enimyY[j] = 2000
            game_over_text()
            break

        enimy(enimyX[i], enimyY[i], i)
        enimyX[i] += enimyX_change[i]

        if enimyX[i] > 736:
            enimyY[i] += enimyY_change[i]
            enimyY_change[i] += 0
            enimyX_change[i] -= 2
        if enimyX[i] <= 0:
            enimyX[i] = 0
            enimyY[i] += enimyY_change[i]
            enimyY_change[i] += 0
            enimyX_change[i] += 2

        collision = isCollision(enimyX[i], enimyY[i], bulletX, bulletY)

        if collision:
            bullet_state = 'ready'
            bulletX = playerX + 16
            bulletY = playerY - 10
            score += 1
            enimyX[i] = random.randrange(60, 700)
            enimyY[i] = random.randrange(30, 90)
    show_score(textX, textY)
    pygame.display.update()
