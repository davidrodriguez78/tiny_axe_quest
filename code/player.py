from setting import *

# Plpayer class
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.idle = [
            pygame.image.load(join("assets", "playeridle", "0.png")).convert_alpha(),
            pygame.image.load(join("assets", "playeridle", "1.png")).convert_alpha()
        ]
        self.run_frames = [
            pygame.image.load(join("assets", "playerrun", "0.png")),
            pygame.image.load(join("assets", "playerrun", "1.png")),
            pygame.image.load(join("assets", "playerrun", "2.png")),
            pygame.image.load(join("assets", "playerrun", "3.png"))
        ]
        self.frame_index = 0
        self.frame_speed = 0
        self.direction = pygame.Vector2()
        self.image = self.idle[self.frame_index]
        self.rect =self.image.get_frect(center = pos)
        self.moveing = False
        self.speed = 80
        self.animation_timer = 0

    def animate(self, dt):
       pass     

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize()if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt
        self.animate(dt)