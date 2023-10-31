import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Race Car Game')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
car_speed = 60
car_width = 73

# Gambar untuk mobil silahkan ganti sendiri sesuai gambar anda
carImg = pygame.image.load('racecar.png')
# Gambar untuk rintangan ~~~~#~~~~~~~~~~~~~~#~~~~~~~~~~
obstacleImg = pygame.image.load('obstacle.png')


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def obstacle(obx, oby, obw, obh, color):
    gameDisplay.blit(obstacleImg, (obx, oby))


def crash():
    message_display('You Crashed')


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    ob_startx = random.randrange(0, display_width)
    ob_starty = -600
    ob_speed = 7
    ob_width = 100
    ob_height = 100

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

        # Rintangan bergerak
        obstacle(ob_startx, ob_starty, ob_width, ob_height, black)
        ob_starty += ob_speed

        car(x, y)

        if x > display_width - car_width or x < 0:
            crash()

        if ob_starty > display_height:
            ob_starty = 0 - ob_height
            ob_startx = random.randrange(0, display_width)

        if y < ob_starty+ob_height:
            if x > ob_startx and x < ob_startx + ob_width or x+car_width > ob_startx and x + car_width < ob_startx+ob_width:
                crash()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
