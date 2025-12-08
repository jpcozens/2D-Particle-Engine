import pytest
import pygame
from pygame.locals import *
pygame.init()

from particle.particle import Particle
from global_state import PARTICLE_GROUP

# initialise empty display to allow use of Surface.convert_alpha
pygame.display.set_mode()

# UT-001 - set_mode method correctly updates the particle mode
# converts surfaces into BufferProxys and compares raw bytes contents
def test_set_mode():
    particle_test_instance = Particle((0,0), (5,5), Particle.MODE_RECT, (1,1))

    # compare set_mode(ellipse) to particle instantiated as ellipse
    temp_particle_test_instance_ellipse = Particle((0,0), (5,5), Particle.MODE_ELLIPSE, (1,1))
    particle_test_instance.set_mode(Particle.MODE_ELLIPSE)
    surf_ellipse_buffer_temp = temp_particle_test_instance_ellipse.surf.get_view()
    surf_ellipse_buffer_real = particle_test_instance.surf.get_view()
    assert surf_ellipse_buffer_temp.raw == surf_ellipse_buffer_real.raw

    # compare set_mode(rect) to particle instantiated as rect
    temp_particle_test_instance_rect = Particle((0,0), (5,5), Particle.MODE_RECT, (1,1))
    particle_test_instance.set_mode(Particle.MODE_RECT)
    surf_rect_buffer_temp = temp_particle_test_instance_rect.surf.get_view()
    surf_rect_buffer_real = particle_test_instance.surf.get_view()
    assert surf_rect_buffer_temp.raw == surf_rect_buffer_real.raw


# UT-002 - update method correctly updates particle state
no_acceleration_test_data = [
    ((5,5), (5,5)),
    ((5,5), (10,10)),
    ((5,5), (15,15)),
    ((5,5), (20,20)),
    ((5,5), (25,25)),
    ((5,5), (30,30)),
]

acceleration_test_data = [
    ((6,6), (6,6)),
    ((7,7), (13,13)),
    ((8,8), (21,21)),
    ((9,9), (30,30)),
    ((10,10), (40,40)),
    ((11,11), (51,51)),
]

# assert that particle state update calls follow test data for (5,5) velocity, 0 acceleration
particle_test_instance_no_acceleration = Particle((0,0), (5,5), Particle.MODE_RECT, (5,5))
@pytest.mark.parametrize("vel, pos", no_acceleration_test_data)
def test_update_no_acceleration(vel, pos):
    particle_test_instance_no_acceleration.update()
    assert particle_test_instance_no_acceleration.velocity == vel
    assert particle_test_instance_no_acceleration.position == pos

# assert that particle state update calls follow test data for (5,5) velocity, (1,1) acceleration
particle_test_instance_acceleration = Particle((0,0), (5,5), Particle.MODE_RECT, (5,5))
@pytest.mark.parametrize("vel, pos", acceleration_test_data)
def test_update_acceleration(vel, pos):
    particle_test_instance_acceleration.set_acceleration((1,1))
    particle_test_instance_acceleration.update()
    assert particle_test_instance_acceleration.velocity == vel
    assert particle_test_instance_acceleration.position == pos


# UT-003 - delete method correctly deletes particle from sprite group
# assert that deleted particle does not exist within particle group
def test_delete():
    particle_test_instance = Particle((0,0), (5,5), Particle.MODE_RECT, (1,1))
    particle_test_instance.delete()
    assert particle_test_instance not in PARTICLE_GROUP 
