class Particle:

    MODE_RECT = 0
    MODE_CIRCLE = 1

    def __init__(self,
                 pos: tuple[int,int],
                 size: int,
                 mode: int,
                 vel: tuple[float,float],
    ):
        pass

    def update(self): pass

    def set_mode(self, mode: int): pass
    def set_velocity(self, vel: tuple[float,float]): pass
    def set_accleration(self, acc: tuple[float,float]): pass
    def delete(self): pass
