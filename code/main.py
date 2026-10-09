from setting import *
from player import Player
# Game class
class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOWS_WIDHT, WINDOWS_HEIGTH))
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

        # groups
        self.all_sprites_groups = pygame.sprite.Group()
        #objects
        self.player = Player(pygame.Vector2(WINDOWS_WIDHT / 2, WINDOWS_HEIGTH /2), self.all_sprites_groups)
    def run(self):
        while self.running:
            # delta time
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.display_surface.fill("darkgrey")
            # update
            self.all_sprites_groups.update(dt)
            # draw
            self.all_sprites_groups.draw(self.display_surface)
            # display update
            pygame.display.update()
            print(dt)
        pygame.quit()
        sys.exit()

# Game object
if __name__ == "__main__":
    game = Game()
    game.run()
            
    