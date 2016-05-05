"""
PHY2071: Introduction to Astonomy Comp. Project
E. Schoenrock (c)2016

Script to solve friedmann equations in a FLAT UNIVERSE (K=0). Comparison between matter-dominated scenario
and radiation-dominated scenario
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as s
from scipy.integrate import odeint
from astropy.cosmology import WMAP9 as cosmo


p_crit = np.square(cosmo.H(0)/100) * 1.87e-29 #critical density of the universe at present
const = (8*s.pi*s.G)/3 #Define this as a constant, makes life easier


##Matter Approximation Function
def flat_universe (y,t):
    dy0 = np.sqrt(const * y[1] * np.square(y[0])) #friedmann eqn 
    dy1 = -((3*y[1])*dy0)/y[0] #fluid eqn
    return[dy0, dy1]
    
 
##Radiation Approximation Function
def flat_universe_rad (x,t):
    dx0 = np.sqrt(const * x[1] * np.square(x[0])) #friedmann eqn
    dx1 = -((4*x[1])*dx0)/x[0] #fluid eqn
    return[dx0, dx1]


init = [1, 0.72*1.87e-23] #set the initial conditions at time now
time = np.arange(0,10e17, 10e10) #set the time length, form now to a few million/ billion yrs in the future


yy = odeint(flat_universe, init, time) #solves ODE for dust approx
xx = odeint(flat_universe_rad, init, time)#solves ode for rad approx


##Plotting
fig, ax = plt.subplots()

ax.plot(time, yy[:,0], color = 'red', label = 'Matter-Dominated') #plot matter dominated universe
ax.plot(time, xx[:,0], color = 'green', label = 'Radiation-Dominated') #plot rad dominated universe

#add a legend
legend = ax.legend(loc = 'upper left')
frame = legend.get_frame()
frame.set_facecolor('0.9')

for label in legend.get_texts():
    label.set_fontsize('large')

for label in legend.get_lines():
    label.set_linewidth(1.5)

#add labels to the graph (make it look nice)
ax.set_title('Flat Universe')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Scale Factor of the Universe')

#set the limits, makes for a better looking graph
ax.set_xlim((0,6e17))
#ax.set_ylim((1,1.34))
       
plt.show()
