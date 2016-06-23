''' Implements basic physics for bead and spring models '''

from Bead import 
import scipy
import math

inter = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] #5x5 interaction matirx between 5 molecules


#Masses
mass_water = 0.1
mass_lip1h = 0.2
mass_lip1t = 0.3
mass_lip2h = 0.4
mass_lip2t = 0.5

masses = np.asarray([mass_water,mass_lip1h,mass_lip1t,mass_lip2h,mass_lip2t]) # masses of each particle to calculate accl

crit_dist=0.0 # distance below which a lipids are bonded
bond_length = 1

def spring_force(atom1, atom2, k, mean):
  r = scipy.spatial.distance.euclidean(atom1.x, atom2.x)
  F = -k*(r-mean)
  dirvec = (atom2.x-atom1.x)/r
  return F*dirvec

def lennard_force(atom1, atom2, e):
  r = scipy.spatial.distance.euclidean(atom1.x, atom2.x)
  F = e*(1./r**6 - 1./r**12)
  dirvec = (atom2.x-atom1.x)/r
  return F*dirvec

def euler_integrate(initial, slope, time_step):
  return np.asarray(initial) + time_step*np.asarray(slope)

for i in range(N_atoms): # relapce atom_len_1 with numer of atoms
  force_net = np.zeros(2)
  force_vec = np.zeros(2)
  atom1 = i # get atom1 from Bead. It should be a number between 1 and 5
  
  for j in range(N_atoms): # replace atom_len_2 with the numer of atome atom1 interacts with
    if (i==j):
      continue
    atom2=j # get interacting atom2 from bead. It should be a number between 1 and 5
      
    if (atom1.isBonded(atom2)):
      force_vec = spring_force(atom1, atom2, inter[atom1.arg][atom2.arg], bond_length)
    else:
      force_vec = lennard_force(atom1, atom2, inter[atom1.arg][atom2.arg])
    
    force_net = force_net + force_vec

accel_vec = (np.asarray([1,1,1,1,1])/masses)*(force_vec)
vel_vec = euler_integrate(vel_vec, accel_vec, dt)
pos_vec = euler_integrate(pos_vec, vel_vec, dt)
      
if r<crit_dist:
    return spring_force(atom1, atom2)
  else:
    return lennard_force(atom1,atom2)
