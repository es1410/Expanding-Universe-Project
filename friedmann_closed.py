"""
PHY2071: Introduction to Astronomy - Comp. Project
E. Schoenrock (c)2016

Script to solve friedmann equations in a CLOSED UNIVERSE (K>0). Comparison between matter-dominated scenario
and radiation-dominated scenario
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as s
from scipy.integrate import odeint
from astropy.cosmology import WMAP9 as cosmo

p_crit = np.square(cosmo.H(0)/100) * 1.87e-29 #critical density of the universe at present
const = (8*s.pi*s.G)/3 #define this as a const (makes life easier)


#Matter-dominated universe
n = np.linspace(0,2,200)*s.pi #set the alpha values for universe
a_max = 1 #maximum value of closed universe, symmetric about this value

a_matter= a_max*(1-np.cos(n)) #scale factor of the universe 
t_matter = a_max*(n-np.sin(n)) #time parameter


#radiation-dominated universe
m = np.linspace(0,2,200)*s.pi #set the alpha values for universe
b_max = 1 #maximum value of closed universe, symmetric about this value

a_rad = b_max*(1-np.cos(m)) #scale factor of the universe 
t_rad = b_max*(m-np.sin(m)) #time parameter


#Plotting 
fig, ax = plt.subplots()

ax.plot(2*t_matter*1e17,a_matter, color = 'red', label = 'Matter-Dominated')
ax.plot(1.2*t_rad*1e17, 0.5*(a_rad), color = 'green', label = 'Radiation-Dominated')


#Add a legend
legend = ax.legend(loc = 'upper left')
frame = legend.get_frame()
frame.set_facecolor('0.9')

for label in legend.get_texts():
    label.set_fontsize('large')

for label in legend.get_lines():
    label.set_linewidth(1.5)

#add labels to the graph (make it look nice)
ax.set_title('Closed Universe')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Scale Factor of the Universe')

#set the limits, makes for a better looking graph
ax.set_xlim((0,1.3e18))
ax.set_ylim((0,2.1))
plt.show()
