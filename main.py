'''Main simulation loop '''

import numpy as np
import Bead
import physics

#Run parameters:
N_atoms = 100

atoms = []
x0 = []
y0 = []
for i in range(N_atoms):
    atoms[i] = (x0[i], v0[i], a0[i], 1)
