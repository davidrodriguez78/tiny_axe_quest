from setting import *

# Game class
class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOWS_WIDHT, WINDOWS_HEIGTH))
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

        # groups

        #objects

    def run(self):
        while self.running:
            # delta time
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update

            # draw

            # display update
            pygame.display.update()
        pygame.quit()
        sys.exit()

# Game object
if __name__ == "__main__":
    game = Game()
    game.run()
            
    