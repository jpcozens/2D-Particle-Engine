# learning pytest

import pytest
import pygame
from pygame.locals import *
pygame.init()

from particle.particle import Particle 

# initialise empty display
pygame.display.set_mode()

particle_test_instance = Particle((0,0), (5,5), Particle.MODE_RECT, (1,1))

# tests

def test_always_fails():
    assert particle_test_instance.velocity == (2,1)

def test_always_fails2():
    assert particle_test_instance.velocity == (3,1)

test_pass_data = [
        (5,5),
        (5,5),
        (5,5),
        (5,5),
        (5,5),
        (5,5),
        (5,5),
        (5,5),
        (1,4)
]

@pytest.mark.parametrize("a, b", test_pass_data)
def test_always_passes(a, b):
    assert particle_test_instance.size == (a, b)
