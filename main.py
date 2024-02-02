# Example file showing a circle moving on screen
import pygame
import pygame_widgets
import ui as ui
import asyncio

# pygame setup
def main():
    clock = pygame.time.Clock()
    running = True
    dt = 0


    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        
        ui.updateScreen()
        ui.drawBoardLines()

        pygame_widgets.update(events)
        pygame.display.update()
        # limits FPS to 60
        dt = clock.tick(60) / 1000


    pygame.quit()

if __name__ == '__main__':
    main()
