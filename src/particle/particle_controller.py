import pygame, random
from .particle import Particle

class Particle_Controller:

    def __init__(self,
                 size: tuple[int, int],
                 pos: tuple[int, int] = (0,0),
                 particle_mode: int = Particle.MODE_RECT,
                 particle_size: int = 5,
                 particle_vel: tuple[float, float] = (5,5),
                 ):

        self.rect = pygame.Rect(pos, size)
        self.particles = []
        self.start(particle_mode, particle_size, particle_vel)

    # create 50 particles, clear current particles if any
    def start(self, mode: int, size: int, vel: tuple[float, float]):
        if len(self.particles) != 0:
            self.clear()

        for _ in range(0,50):
            x = random.randint(self.rect.left,self.rect.right)
            y = random.randint(self.rect.top,self.rect.bottom)
            self.particles.append(Particle((x,y), size, mode, vel))

    def clear(self):
        while len(self.particles) > 0: 
            self.particles.pop().delete()

    def set_particle_mode(self, particle_mode: int):
        for particle in self.particles:
            particle.set_mode(particle_mode)

    def set_particle_velocity(self, particle_vel: tuple[float, float]):
        for particle in self.particles:
            particle.set_velocity(particle_vel)

    def set_particle_acceleration(self, particle_acc: tuple[float, float]):
        for particle in self.particles:
            particle.set_acceleration(particle_acc)

    def delete_particle(self, particle_instance: Particle):
        self.particles.remove(particle_instance)
        particle_instance.delete()
