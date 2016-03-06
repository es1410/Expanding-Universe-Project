"""
Created on Wed Mar  2 16:11:44 2016

@author: Eric Saboya	'/Users/Eric/Documents/hubble/friedmann_open.py'

Script to solve friedmann equations in an OPEN UNIVERSE (K<0). Comparison between matter-dominated scenario
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
def open_universe_dust (y,t):
    dy0 = np.sqrt(const * y[1] * np.square(y[0]) + 0.1) #friedmann eqn qith k=-0.1
    dy1 = -((3*y[1])*dy0)/y[0] #fluid eqn 
    return[dy0, dy1]


##Radiation Approximation Function
def open_universe_rad (x,t):
    dx0 = np.sqrt(const * x[1] * np.square(x[0])+ 0.1) #friedmann eqn qith k=-0.1
    dx1 = -((4*x[1])*dx0)/x[0] #fluid eqn
    return[dx0, dx1]


#Solving the functions
init = [1, 1e-27] #define the initial conditions of the universe at present
time = np.arange(0,10e17, 10e10) #set the time parameters

yy = odeint(open_universe_dust, init, time) #solve the dust approx ODEs
xx = odeint(open_universe_rad, init, time) #solve the rad approx ODEs


#Plotting
fig, ax = plt.subplots()

ax.plot(time, yy[:,0]*1e-17 +1, color = 'red', label='Matter-Dominated') #plot the matter dominated 
ax.plot(time, xx[:,0]*1e-17 +1, color = 'green', label = 'Radiation-Dominated') #plot the rad dominated

#Add a legend
legend = ax.legend(loc = 'upper left')
frame = legend.get_frame()
frame.set_facecolor('0.9')

for label in legend.get_texts():
    label.set_fontsize('large')

for label in legend.get_lines():
    label.set_linewidth(1.5)


#Add labels/ titles
ax.set_title('Open Universe')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Scale Factor of the Universe')

plt.show()