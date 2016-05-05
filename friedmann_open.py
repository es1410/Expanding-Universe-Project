"""
PHY2071: Introduction to Astonomy Comp. Project
E. Schoenrock (c)2016'

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

k = -1.0 #curvature of space

##Matter Approximation Function
def open_universe_dust (y,t):
    dy0 = np.sqrt(const * y[1] * np.square(y[0]) - k) #friedmann eqn 
    dy1 = -((3*y[1])*dy0)/y[0] #fluid eqn
    return[dy0, dy1]
    
 
##Radiation Approximation Function
def open_universe_rad (x,t):
    dx0 = np.sqrt(const * x[1] * np.square(x[0]) - k) #friedmann eqn
    dx1 = -((4*x[1])*dx0)/x[0] #fluid eqn
    return[dx0, dx1]

a0 = 1
p0 = 10e-26
init = [a0,p0] #set the initial conditions at time now
time = np.linspace(0,10e17, 40000) #set the time length, form now to a few million/ billion yrs in the future


yy = odeint(open_universe_dust, init, time) #solves ODE for dust approx
xx = odeint(open_universe_rad, init, time)#solves ode for rad approx

init1 = [1, 10e-2]

ww = odeint(open_universe_dust, init1, time)
vv = odeint(open_universe_rad, init1, time)

#Plotting  *1e-17 +1
fig, ax = plt.subplots()

ax.plot(time, yy[:,0], color = 'red', label='Matter-Dominated - open') #plot the matter dominated 
ax.plot(time, xx[:,0], color = 'green', label = 'Radiation-Dominated - closed') #plot the rad dominated
ax.plot(time, ww[:,0], color = 'blue', label = 'Matter approx, flat')
ax.plot(time, vv[:,0], color = 'black', label = 'rad approx, flat')


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
