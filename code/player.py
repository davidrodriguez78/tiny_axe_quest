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
        self.idle_index = 0
        self.run_index = 0
        self.direction = pygame.Vector2()
        self.image = self.idle[self.idle_index]
        self.original_image = self.image
        self.rect = self.image.get_frect(center = pos)
        self.moveing = False
        self.speed = 80
        self.animation_timer = 0
        self.facing = "right"

    def idle_anim(self):
        if self.animation_timer >= 0.20:
            self.animation_timer = 0
            self.idle_index += 1
            if self.idle_index >= len(self.idle):
                self.idle_index = 0
        self.image = self.idle[self.idle_index]

    def run_anim(self):
        if self.animation_timer >= 0.16:
            self.animation_timer = 0
            self.run_index += 1
            if self.run_index >= len(self.run_frames):
                self.run_index = 0
        self.image = self.run_frames[self.run_index]

    def animate(self, dt):
        self.animation_timer += dt
        
        if self.moveing:
            self.run_anim()
        else:
            self.idle_anim()
        # flipping sprite
        if self.direction.x < 0: 
            self.facing = "left"
        else:
            self.facing = "rith"
        print(self.facing)
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = (int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT]) or int(keys[pygame.K_d]) - int(keys[pygame.K_a]))
        self.direction.y = (int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP]) or int(keys[pygame.K_s]) - int(keys[pygame.K_w]))
        self.direction = self.direction.normalize()if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        # movement
        if self.direction.length() > 0:
            self.moveing = True
        else:
            self.moveing = False
            
        # animate
        self.animate(dt)
            