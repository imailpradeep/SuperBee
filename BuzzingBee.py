import pygame, sys, random
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Buzzing Bee')
screen = pygame.display.set_mode((700, 500))
flower = pygame.transform.scale(pygame.image.load("rosehip.png").convert_alpha(), (700, 500))
bee = pygame.transform.scale(pygame.image.load("bee.png").convert_alpha(), (70, 50))
xvel, yvel, x, y = 1, 1, 175, 325
while True:
    # Buttons for exit---------------------------------------- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
    screen.fill((75, 75, 250))
    screen.blit(flower, (0, 0))
    x += xvel
    y += yvel
    xvel, yvel = random.randint(-2,2), random.randint(-3,3)
    screen.blit(bee, (x, y))
    pygame.display.update()
    #mainClock.tick(70)

