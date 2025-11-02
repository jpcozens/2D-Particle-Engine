import pygame, random
from .particle import Particle

class Particle_Controller:

    def __init__(self,
                 size: tuple[int, int],
                 pos: tuple[int, int] = (0,0),
                 particle_mode: int = Particle.MODE_RECT,
                 particle_size: tuple[int, int] = (5,5),
                 ):

        self.rect = pygame.Rect(pos, size)
        self.particles = []
        self.start(particle_mode, particle_size)

    # create 50 particles, clear current particles if any
    def start(self, mode: int, size: tuple[int, int]):
        if len(self.particles) != 0:
            self.clear()

        for _ in range(0,50):
            x_pos = random.randint(self.rect.left,self.rect.right)
            y_pos = random.randint(self.rect.top,self.rect.bottom)
            pos = x_pos, y_pos

            x_vel = random.randint(1,5)
            y_vel = random.randint(1,5)
            vel = x_vel, y_vel
            self.particles.append(Particle(pos, size, mode, vel))

    def clear(self):
        while len(self.particles) > 0: 
            self.particles.pop()

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
