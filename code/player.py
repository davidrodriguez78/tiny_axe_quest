from setting import *

# Plpayer class
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_groups):
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
        self.rect = self.image.get_frect(center = pos)
        self.collision_group = collision_groups
        self.moveing = False
        self.speed = 80
        self.animation_timer = 0
        self.flip = False

    def idle_anim(self):
        if self.animation_timer >= 0.20:
            self.animation_timer = 0
            self.idle_index += 1
            if self.idle_index >= len(self.idle):
                self.idle_index = 0
        frame = self.idle[self.idle_index]
            
        self.image = pygame.transform.flip(frame, self.flip, False)

    def run_anim(self):
        if self.animation_timer >= 0.16:
            self.animation_timer = 0
            self.run_index += 1
            if self.run_index >= len(self.run_frames):
                self.run_index = 0
        frame = self.run_frames[self.run_index]
        self.image = pygame.transform.flip(frame, self.flip, False)

    def animate(self, dt):
        self.animation_timer += dt
        
        if self.moveing:
            self.run_anim()
        else:
            self.idle_anim()

    def collosion(self, direction):
        pass
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.flip = False
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.flip = True
        else:
            self.direction.x = 0
        
        if keys[pygame.K_DOWN]:
            self.direction.y = 1
        elif keys[pygame.K_UP]:
            self.direction.y = -1
        else:
            self.direction.y = 0
        
        self.direction = self.direction.normalize()if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        # direction
        self.collosion("horizontal")
        self.collosion("vertical")
        # movement
        if self.direction.length() > 0:
            self.moveing = True
        else:
            self.moveing = False
       
        # animate
        self.animate(dt)
        
            