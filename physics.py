''' Implements basic physics for bead and spring models '''

import Bead
import scipy

def spring_force(atom1, atom2, k):
  r = scipy.spatial.distance.euclidean(atom1.x, atom2.x)
  return -k*r
