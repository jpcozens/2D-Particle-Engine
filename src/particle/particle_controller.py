from particle import Particle

class Particle_Controller:

    def __init__(self,
                 size: tuple(int,int),
                 pos: tuple(int,int) = (0,0),
                 particle_mode: int = Particle.MODE_SQUARE,
                 particle_size: int = 5,
                 particle_size: int = 5,
                 particle_vel = tuple(float,float) = (5,5)):
        pass

    def start(): pass
    def clear(): pass
    def set_particle_mode(particle_mode: int): pass
    def set_particle_velocity(particle_vel: tuple(float,float)): pass
    def set_particle_acceleration(particle_acc: tuple(float,float)): pass
    def delete_particle(particle: particle.Particle): pass
