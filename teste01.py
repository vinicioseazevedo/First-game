import pygame

print('Setup start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Loop Start')
while True:
    # Checcck for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT  # closer window
            quit()  # end pygame
