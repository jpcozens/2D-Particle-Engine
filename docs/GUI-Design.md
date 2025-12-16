# GUI Module Design

## Contents

### base-GUI

Gives the user control over setting all of the base attributes of a particle (velocity, acceleration, etc), which are covered in the base-particle submodule. 
Also includes pauing, resuming and restarting the simulation.

### drag-GUI

...

### collision-GUI

...

---

## Non-Functional Requirements

| Requirement-ID | Description |
| :--- | :--- |
| NFR1 | The particle system can handle 5000 particles at 60FPS |
| NFR2 | Particle collisions are smooth and do not overlap with objects or other particles |

---

## Sub-Module Design

### base-GUI

X class files are contained within this sub-module:
* Panel
* Text
* Button
* Slider

#### Panel

Panels are simply visual blocks used to group elements together.
They will also be the parent of buttons, as buttons have a similar visual style.

Panel will be implemented as a class with a slightly rounded, translucent surface attribute.
This class will only have customisable size, as major customisation is not required - it is only being
used to create a simple menu with useability in mind.

<br>

**State:**
| Attribute | Type | Usage |
| :--- | :--- | :--- |
| ``self.rect`` | ``pygame.Rect`` | Stores the geometry data for the surface |
| ``self.surf`` | ``pygame.Surface`` | The surface element storing render data for the panel |

<br>

**Methods:**
| Method | Parameters | Usage |
| :--- | :--- | :--- |
| ``__init__`` | ``size: tuple(int, int)``<br>``pos: tuple(int,int)`` | Instantiate the panel |
| ``set_surface`` | ``opacity: int`` | Sets the surface attribute with the desired opacity. Not in constructor so that is inherited by Button class |
| ``delete`` | N/A | Deletes the panel from the GUI sprite group |

<br>

##### Tests

* ...
* ...

#### Text

A simple class which takes plaintext and geometric arguments.
Not designed to be updated after initialisation.

<br>

**State:**
| Attribute | Type | Usage |
| :--- | :--- | :--- |
| ``self.rect`` | ``pygame.Rect`` | Stores the geometry data for the surface |
| ``self.surf`` | ``pygame.Surface`` | The surface element storing render data for the text |

<br>

**Methods:**
| Method | Parameters | Usage |
| :--- | :--- | :--- |
| ``__init__`` | ``pos: tuple(int, int)``<br>``font_size: int``<br>``content: str = ""`` | Instantiate the text |
| ``delete`` | N/A | Deletes the text from the GUI sprite group |

<br>

##### Tests

* ...
* ...

#### Button

Buttons are children of the Panel class, with the following additions:
* Surface opacity changing: default -> onhover -> onclick
* onclick event handling
* Contained Text class instances via composition

<br>

**State**
| Attribute | Type | Usage |
| :--- | :--- | :--- |
| ``self.rect`` | pygame.Rect | Stores the geometry data for the surface |
| ``self.surf`` | pygame.Surface | Stores the render data for the button panel |
| ``self.text_instance`` | GUI.Text | The text instance to title the panel |
| ``self.onclick_function`` | Callable | The function to call when an onclick is receieved |
| ``self.onclick_args`` | tuple(Any, ...) | The arguments to pass to the onlick function |

<br>

**Methods**
| Method | Parameters | Usage |
| :--- | :--- | :--- |
| ``__init__`` | ``pos: tuple(int,int)``<br>``size: tuple(int,int)``<br>``onclick: Callable``<br>``*onclick_args: tuple(Any, ...)``| Initialise the button |
| ``update`` | N/A | Check for mouse interaction with the button |
| ``delete`` | N/A | Remove the button from the GUI sprite group |

<br>

##### Tests

* ...
* ...

<br>

#### Slider

Sliders are also children of the panel class, however the panel represents the
length of the slider. They contain a button via composition that is the actual
slider interaction element. Sliders should:
* Receive mouse input on the button element
* The button element should follow the mouse along the slider to either end
* The length across the slider should change the slider's value
* The slider should call a function with its value everytime it's updated

<br>

**State**

| Attribute | Type | Usage |
| :--- | :--- | :--- |
| ``self.rect`` | pygame.Rect | Stores geometric data for the slider panel |
| ``self.surf`` | pygame.Surface | Stores render data for the slider panel |
| ``self.slider_range`` | tuple(int, int) | The range of values the slider covers |
| ``self.slider_button`` | GUI.Button | Button instance for the slider button |
| ``self.slider_function`` | Callable | The function the slider should call when updated |

<br>

**Methods**

| Method | Parameters | Usage |
| :--- | :--- | :--- |
| ``__init__`` | ``range: tuple(int,int)``<br>``slider_function: Callable`` | Initialises the slider |
| ``slider_update`` | N/A | Updates the position of the slider button and calls the associated slider function with the slider's value. Called by the onclick of the ``slider_button`` element |
| ``delete`` | N/A | Removes the slider from the GUI sprite group |

<br>

##### Tests

* ...
* ...
