import pygame

screenWidth = 1280
screenHeight = 720
frameRate = 60

dvdLogoWidth = 120
dvdLogoHeight = 50

screen = pygame.display.set_mode( (screenWidth, screenHeight) )
clock = pygame.time.Clock()

while True:
    clock.tick(frameRate)

    pygame.event.get()

    # Calculations
    

    # Drawing

    pygame.display.flip()
