import pygame
import pygame_widgets
from ui import UI
from time import time

# pygame setup
def main():
    running = True
    ui = UI()
    timer_delay = time()

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        
        ui.updateScreen()
        ui.drawBoardLines()
        ui.renderText()

        if ui.runAlgo:
            try:
                if time() - timer_delay >= ui.slider.getValue():
                    ui.iterate()
                    timer_delay = time()
            except StopIteration:
                ui.finish()

        pygame_widgets.update(events)
        pygame.display.update()


    pygame.quit()

if __name__ == '__main__':
    main()
