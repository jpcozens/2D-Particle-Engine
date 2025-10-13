import pygame
import global_state

class Particle:

    MODE_RECT = 0
    MODE_ELLIPSE = 1

    def __init__(self,
                 pos: tuple[int, int],
                 size: tuple[int, int],
                 mode: int,
                 vel: tuple[float, float],
                 ):

        self.surf: pygame.Surface
        self.rect: pygame.Rect

        self.size = size
        self.position = pos
        self.velocity = vel
        self.acceleration = 0,0 

        self.set_mode(mode)
        global_state.PARTICLE_GROUP.append(self)

    def update(self):
        self.velocity = ((self.velocity[0] + self.acceleration[0]),
                          self.velocity[1] + self.acceleration[1])

        self.position = ((self.position[0] + self.velocity[0]),
                          self.position[1] + self.velocity[1])

        self.rect.topleft = (int(self.position[0]), int(self.position[1]))

    def set_mode(self, mode: int):
        self.surf = pygame.Surface(self.size).convert_alpha()
        self.rect = self.surf.get_rect()
        self.rect.topleft = (int(self.position[0]), int(self.position[1]))
        match mode:
            case self.MODE_RECT:
                self.surf.fill((255,255,255))
            case self.MODE_ELLIPSE:
                self.surf.fill((0,0,0,0))
                pygame.draw.ellipse(self.surf, (255,255,255), (0,0,self.size[0], self.size[1]))

    def set_velocity(self, vel: tuple[float, float]):
        self.velocity = vel

    def set_accleration(self, acc: tuple[float, float]):
        self.acceleration = acc

    def delete(self): del self
