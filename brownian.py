# -*- coding: utf-8 -*-
"""
Implements 2-D Brownian motion

Created on Tue Jun 21 10:16:09 2016

@author: kaliaden
"""

from math import sqrt
from scipy.stats import norm
import numpy as np
from pylab import plot, show, grid, axis, xlabel, ylabel, title
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import Bead


'''Physical object class definitions'''
        
'''Physics module'''


#Parameters
sigma = 1
dt = 0.2

#Initial Conditions
x0 = 0

#Run Parameters
runtime = 50

def brownian(x0, n ,sigma, dt, out=None):
    """
    Generate an instance of Brownian motion (i.e. the Wiener process):

        X(t) = X(0) + N(0, delta**2 * t; 0, t)

    where N(a,b; t0, t1) is a normally distributed random variable with mean a and
    variance b.  The parameters t0 and t1 make explicit the statistical
    independence of N on different time intervals; that is, if [t0, t1) and
    [t2, t3) are disjoint intervals, then N(a, b; t0, t1) and N(a, b; t2, t3)
    are independent.

    Written as an iteration scheme,

        X(t + dt) = X(t) + N(0, delta**2 * dt; t, t+dt)


    If `x0` is an array (or array-like), each value in `x0` is treated as
    an initial condition, and the value returned is a numpy array with one
    more dimension than `x0`.

    Arguments
    ---------
    x0 : float or numpy array (or something that can be converted to a numpy array
         using numpy.asarray(x0)).
        The initial condition(s) (i.e. position(s)) of the Brownian motion.
    n : int
        The number of steps to take.
    dt : float
        The time step.
    delta : float
        delta determines the "speed" of the Brownian motion.  The random variable
        of the position at time t, X(t), has a normal distribution whose mean is
        the position at time t=0 and whose variance is delta**2*t.
    out : numpy array or None
        If `out` is not None, it specifies the array in which to put the
        result.  If `out` is None, a new numpy array is created and returned.

    Returns
    -------
    A numpy array of floats with shape `x0.shape + (n,)`.

    Note that the initial value `x0` is not included in the returned array.
    """

    x0 = np.asarray(x0)

    # For each element of x0, generate a sample of n numbers from a
    # normal distribution.
    r = norm.rvs(size=x0.shape + (n,), scale=sigma*sqrt(dt))

    # If `out` was not given, create an output array.
    if out is None:
        out = np.empty(r.shape)

    # This computes the Brownian motion by forming the cumulative sum of
    # the random samples.
    np.cumsum(r, axis=-1, out=out)

    # Add the initial condition.
    out += np.expand_dims(x0, axis=-1)

    return out

x1 = np.empty((2,runtime+1))
x1[:, 0] = 0.0

x2 = np.empty((2,runtime+1))
x2[:, 0] = 0.0

brownian(x1[:,0], runtime, dt, sigma, out=x1[:,1:])
brownian(x2[:,0], runtime, dt, sigma, out=x2[:,1:])

# Plot the 2D trajectory.
plot(x1[0],x1[1])
plot(x2[0],x2[1])

# Mark the start and end points.
plot(x1[0,0],x1[1,0], 'go')
plot(x1[0,-1], x1[1,-1], 'ro')
plot(x2[0,0],x2[1,0], 'bo')
plot(x2[0,-1], x2[1,-1], 'yo')


# More plot decorations.
title('2D Brownian Motion')
xlabel('x', fontsize=16)
ylabel('y', fontsize=16)
axis('equal')
grid(True)
show()

'''fig, ax = plt.subplots()
points, = ax.plot(x1[1], 'o')
ax.set_ylim(0, 1)

def update(data):
    points.set_ydata(x1[0])
    return points,

def generate_points():
    while True:
        yield np.random.rand(10)  # change this

ani = animation.FuncAnimation(fig, update, generate_points, interval=300)
ani.save('animation.gif', writer='imagemagick', fps=4);
plt.show()
'''
