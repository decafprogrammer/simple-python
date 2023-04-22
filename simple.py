import pygame
import random
import time
from Apple import Apple

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 608

background = pygame.Surface((800,608))

for i in range(25):
    for j in range(19):
        image = pygame.image.load("images/background.png")
        mask = (random.randrange(0,20),random.randrange(0,20),random.randrange(0,20))
        image.fill(mask, special_flags=pygame.BLEND_ADD)
        background.blit(image,(i32,j32))

pygame.init()
display = pygame.display.set_mode([DISPLAY_WIDTH,DISPLAY_HEIGHT])
clock = pygame.time.Clock()

apple = Apple()
apples = pygame.sprite.Group()
apples.add(apple)

game_on = True
while game_on:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_on = False
        elif event.type == pygame.QUIT:
            game_on = False
    display.blit(background,(0,0))

    for apple in apples:
        display.blit(apple.image,apple.rect)

    pygame.display.flip()
    clock.tick(30)

time.sleep(3)
pygame.quit()