# 2D Particle Engine

**An interactive demonstration environment to simulate 2D particle physics and collisions. Designed with modular architecture for future external integration in pygame projects.**

### Tech Stack

[! Version-proofing to be completed at project finalisation.]
[! Current language version is a placeholder]
* Language: **Python 3.11+**
* Dependencies: **Pygame, Pytest**

---

## Project Scope

The following table is a representation of the high-level features of this project. For functional/non-functional requirements, please visit the design documentation files for the respective modules.

### In Scope:

| Feature-ID | Description |
| :--- | :--- |
| F1 | Initialise a scene with 100 particles of equal velocity |
| F2 | A GUI for interacting with particle settings |
| F3 | Particles collide with objects |
| F4 | Particles collide with each other |

### Out of Scope: (Future roadmap)

* Configurable particle presets with save/load functionality.
* The deployment of a python package/API.
* Graphical configuration - textures/animated particles.

---

## Module Structure & Integration

This project will be developed submodule by submodule, following the process of design, development and testing before being integrated.
These are the high-level modules for this project.

| Module | Description |
| :--- | :--- |
| Particle | The particle physics system containing movement, collisions and behaviour | 
| GUI | The GUI for interacting with the demo environment | 

These are the submodules derived from each module:

### Particle

| Sub-Module | Description |
| :--- | :--- |
| base-particle | The base requirements for a particle including storing physics state, translating that state into movement and options for different shapes/hitboxes |
| drag-particle | Support for forces that oppose motion on the particle, including air resistance and gravity |
| object-collisions-particle | Collision handling and detection between particles and objects |
| particle-collisions-particle | Collision handling and detection between particles and other particles |

### GUI

| Sub-Module | Description |
| :--- | :--- |
| base-GUI | The interaction options for the base-particle submodule. Includes changing individual and overall particle velocities and positions | 
| drag-GUI | The interaction options for the drag-particle submodule. Includes changing individual and overall particle gravity and air resistance modifiers | 
| collision-GUI | The interaction options for the object-collisions-particle and particle-collisions-particle submodules. Includes placing and removing objects from the demo, as well as disabling collisions for particle-particle or object-particle |

---

## Professional Practices

### Documentation
* Architecture: detailed module design documents can be found in the [docs directory](/docs/).
* In-Code: code should be self-describing, however the less obvious code will be documented with comments.

### Version Control
* Branching: All code development will only take place on feature branches.
* Branch names: The naming convention for branch development uses the following notation: Feature-Module-Submodule
* Merging: Feature branches only to be merged after completed unit tests.
