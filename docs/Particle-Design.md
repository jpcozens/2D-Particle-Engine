# Particle Module Design

## Contents

### base-particle

Responsible for the foundation of particle instances. Contains a particle controller, which acts as an area for particles to exist in,
which is used as an interface to interact with particles as a collective, and the particle class itself, which will, at this point, contain
state and logic for basic motion (position, velocity, acceleration), as well as support for different shaped particles.

### drag-particle

Allows for more complex particle motion, in which external forces gravity and drag allow for more complex acceleration-based motion.

### object-collisions-particle

This sub-module will introduce objects, which particles will collide with and move accordingly via collision handling logic.

### particle-collisions-particle

The final sub-module of the particle module will introduce inter-particle collisions, adding an extra layer of depth onto the collision logic.

---

## Non-Functional Requirements

| Requirement-ID | Description |
| :--- | :--- |
| NFR1 | The particle system can handle 5000 particles at 60FPS |
| NFR2 | Particle collisions are smooth and do not overlap with objects or other particles |

---

## Sub-Module Design

### base-particle

Two class files are contained within this sub-module:
* particle\_controller.py
* particle.py

> Note that pygame's rect object do not support floating point values for position or size. It is for this reason that
positional attributes are stored as floats, and are casted to integers when used for the rect attribute's position AND
size parameters are taken as integers for object initialisation.

#### particle\_controller

The particle controller is responsible for a few key functions:
* Acting as the area particles are permitted to exist in
* Storing all existing particles
* Having methods to interact with all particles

The particle controller will be implemented as a **singleton** instance it will only be instantiated once.

<br>

**State:**
| Attribute | Type | Usage |
| :--- | :--- | :--- |
| ``self.rect`` | ``pygame.Rect`` | Stores the geometry data for the area in which particles can be displayed |
| ``self.particles`` | ``list[Particle]`` | Stores all active particles |

<br>

**Methods:**
| Method | Parameters | Usage |
| :--- | :--- | :--- |
| ``__init__`` | ``size: tuple(int,int),``<br>``pos : tuple(int,int) = (0,0)``<br>``particle_mode: int = Particle.MODE_RECT``<br>``particle_size: int = 5`` | Instantiate the singleton and set the rect attribute based on size and pos arguments |
| ``set_particle_mode`` | ``particle_mode: int`` | Set the shape and collision mode of all particles |
| ``set_particle_velocity`` | ``particle_vel: tuple(float, float)`` | Set the velocity of all particles |
| ``set_particle_acceleration`` | ``particle_acc: tuple(float, float)`` | Set the acceleration of all particles |
| ``delete_particle`` | ``particle_instance: Particle`` | Pops the given particle from the active particles list |
| ``start`` | N/A | Creates 50 particles with random position and velocity |
| ``clear`` | N/A | Deletes all particles from the active particle list |

<br>

##### Tests

* IT-001: ``start`` method instantiates exactly 50 particles with desired physics state (input or default)
* IT-002: ``clear`` method deletes all particles from the active particle list

#### particle

The particle file will contain all the functionality of particle objects.
This will be implemented as a class.

This sub-module covers the following functionality:
* Pygame rendering setup (rect and surf attributes)
* State for position, velocity and acceleration
* An update method that will update the position of the particle based on its physics state.
* Options for different shape particles - rect and ellipse.

<br>

**State:**
| Attribute | Type | Usage |
| :--- | :--- | :--- |
| ``MODE_RECT`` | ``int`` | Stores the integer code for rect particle mode under a recognisable attribute name |
| ``MODE_ELLIPSE`` | ``int`` | Stores the integer code for circle particle mode under a recognisable attribute name |
| ``self.size`` | ``tuple(int,int)`` | Stores the size of the particle used when setting the surface in the ``set_mode`` method |
| ``self.position`` | ``tuple(float,float)`` | Stores the current axial positions of the particle |
| ``self.velocity`` | ``tuple(float,float)`` | Stores the current velocities of the particle |
| ``self.acceleration`` | ``tuple(float,float)`` | Stores the current accelerations of the particle |
| ``self.rect`` | ``pygame.Rect`` | Stores the geometry data for the particle instance |
| ``self.surf`` | ``pygame.surface.Surface`` | Stores the render data for the particle instance |

<br>

**Methods:**
| Method | Parameters | Usage |
| :--- | :--- | :--- |
| ``__init__`` | ``pos: tuple(int,int)``<br>``size: int``<br>``mode: int``<br>``vel: tuple(float,float)`` | Instantiate the particle |
| ``update`` | N/A | Uses particle physics state to update float position and subsequently integer rect position |
| ``set_mode`` | ``mode: int`` | Sets the particle shape and collision mode |
| ``set_velocity`` | ``vel: tuple(float,float)`` | Sets the particle velocity |
| ``set_acceleration`` | ``acc: tuple(float,float)`` | Sets the particle acceleration |
| ``delete`` | N/A | Deletes the particle from the particle sprite group |

<br>

##### Tests

* UT-001: ``set_mode`` method correctly updates the particle mode
* UT-002: ``update`` method correctly updates particle state
* UT-003: ``delete`` method correctly deletes particle from particle sprite group
