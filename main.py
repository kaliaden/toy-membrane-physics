'''Main simulation loop '''

import numpy as np
import Bead
import physics

#Run parameters:
dim = 2
N_atoms = 100

atoms = []
x0 = np.rand(N_atoms)
y0 = np.rand(N-atoms)
for i in range(N_atoms):
    atoms[i] = (x0[i], v0[i], a0[i], 1)


for i in range(atom_len_1): # relapce atom_len_1 with numer of atoms
  force_vec=[0,0]
  atom1=0 # get atom1 from Bead. It should be a number between 1 and 5
  
  for j in range(atom_len_2): # replace atom_len_2 with the numer of atome atom1 interacts with
    atom2=0 # get interacting atom2 from bead. It should be a number between 1 and 5
    
    if ((atom1,atom2) in lipids) or ((atom2,atom1) in lipids:
      force_exp=spring_force(atom1,atom2,inter[atom1-1][atom2-1])
      angl=math.atan((atom2.x-atom1.x)[1]/(atom2.x-atom1.x)[0])
      force_vec[0]+=force_exp*math.cos(angl)
      force_vec[1]+=force_exp*math.sin(angl)
    else:
      force_exp=force(atom1,atom2,inter[atom1-1][atom2-1])
      angl=math.atan((atom2.x-atom1.x)[1]/(atom2.x-atom1.x)[0])
      force_vec[0]+=force_exp*math.cos(angl)
      force_vec[1]+=force_exp*math.sin(angl)
  
  force_net=(force_vec[0]**2+force_vec[1]**2)**0.5
  angle_net=math.atan(force_vec[1]/force_vec[0])
  accl_vec=force_vec/mass
  vel_fin=vel_init+t*accl_vec
  pos_final=pos_init+vel_init*t+0.5*accl_vec*t**2
      
if r<crit_dist:
    return spring_force(atom1, atom2)
  else:
    return lennard_force(atom1,atom2)
