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

#### particle\_controller

The particle controller is responsible for a few key functions:
* Acting as the area particles are permitted to exist in
* Storing all existing particles
* Having methods to interact with all particles

The class will be implemented as a **singleton** as it will only be instantiated once.

<br>

**State:**
| Attribute | Type | Usage |
| :--- | :--- | :--- |
| ``PARTICLE_MODE_RECT`` | ``int`` | Stores the integer value for rect particle mode under a recognisable attribute name |
| ``PARTICLE_MODE_CIRCLE`` | ``int`` | Stores the integer value for circle particle mode under a recognisable attribute name |
| ``this.rect`` | ``pygame.Rect`` | Stores the geometry data for the area in which particles can be displayed |
| ``this.particles`` | ``list[Particle]`` | Stores all active particles |

<br>

**Methods:**
| Method | Parameters | Usage |
| :--- | :--- | :--- |
| ``__init__`` | ``size: tuple(x,y),``<br>``pos : tuple(x,y) = (0,0)``<br>``particle_mode: int = Particle_Controller.PARTICLE_MODE_RECT`` | Instantiate the singleton and set the rect attribute based on size argument |
| ``set_particle_mode`` | ``particle_mode: int`` | Set the shape of all particles |
| ``set_particle_velocity`` | ``particle_velocity: float`` | Set the velocity of all particles |
| ``set_particle_acceleration`` | ``particle_acceleration: float`` | Set the acceleration of all particles |
| ``start`` | N/A | Creates 50 particles |
| ``clear`` | N/A | Deletes all particles |
