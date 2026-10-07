from setting import *

# Plpayer class
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.idle_frames = [
            pygame.image.load(join("assets", "playeridle", "0.png")).convert_alpha(),
            pygame.image.load(join("assets", "playeridle", "1.png")).convert_alpha()
        ]
        self.frame_index = 0
        self.frame_speed = 0
        self.image = self.idle_frames[self.frame_index]
        self.rect =self.image.get_frect(center = pos)

        self.speed = 10
    def update(self, dt):
        pass
