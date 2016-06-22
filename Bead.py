import numpy as np

class Bead:
    def __init__(self, x, v, a, arg):
        self.x = np.asarray(x) #Position
        self.v = np.asarray(v) #Velocity
        self.a = np.asarray(a) #Acceleration
        self.arg = arg
        self.bonds = []
    
    def bondTo(self, bead):
        self.bonds.append(bead)
        bead.bonds.append(self)
    
    def isBonded(self, bead):
        return bead in self.bonds

    def draw(self):
        pass
