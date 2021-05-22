import pygame
import math
import time
from pygame import mixer

# pygame initialization
pygame.init()
# screen
screen = pygame.display.set_mode((800, 600))
back = pygame.image.load('back.png')
# title an dlogo
pygame.display.set_caption("BouncyBall")
icon = pygame.image.load('bounce.png')
pygame.display.set_icon(icon)
# PlayerImg
playerImg = pygame.image.load("football.png")
playerX = 100
playerY = 293
playerYchange = 23
m = 1
isjump = False
# obstacle image
obstacleImg = []
obstacleX = []
obstacleY = []
obstacleXchange = []
num = 3
temp1 = 500
for i in range(num):
    temp1 += 375
    obstacleImg.append(pygame.image.load('obstacle.png'))
    obstacleX.append(temp1)
    obstacleY.append(293)
    obstacleXchange.append(0)


def obstacle(x, y, i):
    screen.blit(obstacleImg[i], (x, y))


def isCollision(obstacleX, obstacleY, playerX, playerY):
    distance = math.sqrt((math.pow(playerX - obstacleX, 2)) + (math.pow(playerY - obstacleY, 2)))
    if (distance < 65):
        return False
    else:
        return True


over_font = pygame.font.Font('freesansbold.ttf', 64)


def gameOver():
    over_text = over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (200, 250))
    pygame.display.update()
    time.sleep(2)


# loop
running = True
while (running):
    # background
    screen.fill((0, 0, 255))
    screen.blit(back, (0, 0))

    screen.blit(playerImg, (playerX, playerY))

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    # stores keys pressed
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # it will make exit the while loop
            running = False

    if isjump == False:

        # if space bar is pressed
        if keys[pygame.K_SPACE]:
            # make isjump equal to True
            isjump = True
            sound = mixer.Sound("laser.wav")
            sound.play()

    if isjump:
        # calculate force (F). F = 1 / 2 * mass * velocity ^ 2.
        F = (playerYchange)

        # change in the y co-ordinate
        playerY -= F

        # decreasing velocity while going up and become negative while coming down
        playerYchange -= 1

        # object reached its maximum height
        if playerYchange <= 0:
            # negative sign is added to counter negative velocity
            m = -1

        # objected reaches its original state
        if playerYchange == -24:
            # making isjump equal to false
            isjump = False

            # setting original values to v and m
            playerYchange = 23
            m = 1

    for i in range(num):
        if (obstacleX[i] != 0):
            obstacleX[i] -= 5
        else:
            obstacleX[i] = 800

        obstacle(obstacleX[i], obstacleY[i], i)
        collision = isCollision(obstacleX[i], obstacleY[i], playerX, playerY)
        if not collision:
            gameOver()

    pygame.display.update()
