import pygame, random
from .particle import Particle

class Particle_Controller:

    def __init__(self,
                 size: tuple[int, int],
                 pos: tuple[int,int] = (0,0),
                 particle_mode: int = Particle.MODE_RECT,
                 particle_size: int = 5,
                 particle_vel: tuple[float,float] = (5,5),
    ):
        self.particles = []
        self.rect = pygame.Rect(pos, size)
        for _ in range(0,50): self.particles.append(Particle((random.randint(self.rect.left,self.rect.right),random.randint(self.rect.top,self.rect.bottom)),particle_size, particle_mode, particle_vel))

    def start(self): pass
    def clear(self): pass
    def set_particle_mode(self, particle_mode: int): pass
    def set_particle_velocity(self, particle_vel: tuple[float,float]): pass
    def set_particle_acceleration(self, particle_acc: tuple[float,float]): pass
    def delete_particle(self, particle: Particle): pass
