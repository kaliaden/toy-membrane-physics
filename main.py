'''Main simulation loop '''

import numpy as np
import Bead
import physics

#Run parameters:
dim = 2
N_mols = 100

molecules = []
x0 = np.rand(N_mols, dim)
v0 = np.rand(N_mols, dim)
a0 = np.rand(N_mols, dim)
for i in range(N_mols):
    molecules[i] = Bead(x0[i,:], v0[i,:], a0[i,:], 1)

 '''Rewrite this to include new Bead and physics module. This version
 is obsolete
 '''
