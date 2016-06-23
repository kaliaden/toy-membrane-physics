''' Implements basic physics for bead and spring models '''

from Bead import 
import scipy
import math

inter = np.asarray([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]) #5x5 interaction matirx between 5 molecules

#Masses
mass_water = 0.1
mass_lip1h = 0.2
mass_lip1t = 0.3
mass_lip2h = 0.4
mass_lip2t = 0.5

masses = np.asarray([mass_water,mass_lip1h,mass_lip1t,mass_lip2h,mass_lip2t]) # masses of each particle to calculate accl

sp_range = 1.5
len_range = 2
bond_length = 1

def spring_force(atom1, atom2, k, mean, threshold):
  dirvec = np.zeros(2)
  r = scipy.spatial.distance.euclidean(atom1.x, atom2.x)
  if (r<threshold):
    F = -k*(r-mean)
    dirvec = (atom2.x-atom1.x)/r
  return F*dirvec

def lennard_force(atom1, atom2, e, threshold):
  dirvec = np.zeros(2)
  r = scipy.spatial.distance.euclidean(atom1.x, atom2.x)
  if (r<threshold):
    F = e*(1./r**6 - 1./r**12)
    dirvec = (atom2.x-atom1.x)/r
  return F*dirvec

def euler_integrate(initial, slope, time_step):
  return np.asarray(initial) + time_step*np.asarray(slope)

for i in range(N_atoms): # relapce atom_len_1 with numer of atoms
  force_net = np.zeros(2)
  force_vec = np.zeros(2)
  atom1 = atoms[i] # get atom1 from Bead. It should be a number between 1 and 5
  
  for j in range(N_atoms): # replace atom_len_2 with the numer of atome atom1 interacts with
    if (i==j):
      continue
    atom2 = atoms[j] # get interacting atom2 from bead. It should be a number between 1 and 5
      
    if (atom1.isBonded(atom2)):
      force_vec = spring_force(atom1, atom2, inter[atom1.arg][atom2.arg], bond_length, sp_range)
    else:
      force_vec = lennard_force(atom1, atom2, inter[atom1.arg][atom2.arg], len_range)
    
    force_net = force_net + force_vec

  accel_vec = (np.asarray([1,1,1,1,1])/masses)*(force_net)
  atoms[i].a = accel_vec
  atoms[i].v = euler_integrate(atoms[i].v, accel_vec, dt)
  atoms[i].x = euler_integrate(atoms[i].x, vel_vec, dt)
