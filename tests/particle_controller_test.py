import pytest
import pygame
from pygame.locals import *
pygame.init()

from particle.particle_controller import Particle_Controller
from particle.particle import Particle
from global_state import PARTICLE_GROUP

# IT-001: start method instantiates exactly 50 particles with default/input state

# check for default state
def test_start_default():
    # constructor calls the start method with default parameters
    particle_controller_test_instance_default = Particle_Controller((1920, 1080))
    assert len(particle_controller_test_instance_default.particles) == 50

    # assert state is as intended
    for particle_test_instance in particle_controller_test_instance_default.particles:
        assert particle_test_instance.acceleration == (0,0)
        assert particle_test_instance.size == (5,5)

        temp_particle_test_instance = Particle(particle_test_instance.position, particle_test_instance.size, Particle.MODE_RECT, particle_test_instance.velocity)
        surf_buffer_temp = temp_particle_test_instance.surf.get_view()
        surf_buffer_real = particle_test_instance.surf.get_view()
        assert surf_buffer_temp.raw == surf_buffer_real.raw

# check for provided state (vel and pos are randomised)
def test_start():
    # constructor calls the start method with non-default parameters
    particle_controller_test_instance = Particle_Controller((1920, 1080), particle_mode=Particle.MODE_ELLIPSE, particle_size=(50,50))
    assert len(particle_controller_test_instance.particles) == 50

    # assert state is as intended
    for particle_test_instance in particle_controller_test_instance.particles:
        assert particle_test_instance.acceleration == (0,0)
        assert particle_test_instance.size == (50,50)

        temp_particle_test_instance = Particle(particle_test_instance.position, particle_test_instance.size, Particle.MODE_ELLIPSE, particle_test_instance.velocity)
        surf_pixelarray_temp = pygame.PixelArray(temp_particle_test_instance.surf)
        surf_pixelarray_real = pygame.PixelArray(particle_test_instance.surf)

        pixelarray_comparison_mask = surf_pixelarray_temp.compare(surf_pixelarray_real)
        for row in pixelarray_comparison_mask:
            for pixel in row:
                # check integer pixel code is -1 (white)
                # white indicates the same colour as per the comparison mask
                assert pixel == -1


# IT-002: clear method deletes all particles and removes them from the active particle list

# ensure previous tests dont affect this one
PARTICLE_GROUP = []

def test_clear():
    particle_controller_test_instance = Particle_Controller((1920,1080))
    particle_controller_test_instance.clear()
    assert len(particle_controller_test_instance.particles) == 0
    assert len(PARTICLE_GROUP) == 0
