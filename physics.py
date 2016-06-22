''' Implements basic physics for bead and spring models '''

import Bead
import scipy
import math

inter = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] #5x5 interaction matirx between 5 molecules
lipids = [(1,2),(3,4)]
mass=[0,0,0,0,0]
crit_dist=0.0
def spring_force(atom1, atom2, k):
  r = scipy.spatial.distance.euclidean(atom1.x, atom2.x)
  if r<crit_dist:
    return -k*r
  else:
    return force(atom1,atom2)

def force(atom1,atom2):
  r = scipy.spatial.distance.euclidean(atom1.x, atom2.x)
  return inter[atom1-1][atom2-1]*(1./r**6 - 1./r**12)

for i in range(atom_len_1):
  force_vec=[0,0]
  for j in range(atom_len_2):
    if ((atom1,atom2) in lipids) or ((atom2,atom1) in lipids:
      force_exp=spring_force(atom1,atom2,inter[atom1-1][atom2-1])
      angl=math.atan((atom1.x-atom2.x)[1]/(atom1.x-atom2.x)[0])
      force_vec[0]+=force_exp*math.cos(angl)
      force_vec[1]+=force_exp*math.sin(angl)
    else:
      force_exp=force(atom1,atom2,inter[atom1-1][atom2-1])
      angl=math.atan((atom1.x-atom2.x)[1]/(atom1.x-atom2.x)[0])
      force_vec[0]+=force_exp*math.cos(angl)
      force_vec[1]+=force_exp*math.sin(angl)
  force_net=(force_vec[0]**2+force_vec[1]**2)**0.5
  angle_net=math.atan(force_vec[1]/force_vec[0])
  accl_vec=force_vec/mass
  vel_fin=vel_init+t*accl_vec
  pos_final=pos_init+vel_init*t+0.5*accl_vec*t**2
      
