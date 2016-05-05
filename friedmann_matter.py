"""
PHY2071: Introduction to Astonomy Comp. Project
E. Schoenrock (c)2016

Script to solve Friedmann eqns for the main three competing scenarios in a matter-dominated (P=0) universe
"""

import numpy as np
import scipy.constants as s
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Define the constants 
p_crit = np.square(cosmo.H(0)/100) * 1.87e-29 #critical density of the universe at present
const = (8*s.pi*s.G)/3 #Define this as a constant, makes life easier


'''
Flat Universe
'''
#Flat universe matter approx 
def flat_universe (y,t):
    dy0 = np.sqrt(const * y[1] * np.square(y[0]))
    dy1 = -((3*y[1])*dy0)/y[0]
    return[dy0, dy1]
    
init_y= [1, 7.4*1e-27] #set the initial conditions (same as before)
time_y = np.arange(0,12e17, 10e10) #set time parameter
yy = odeint(flat_universe, init_y, time_y) #Solves the ODE in a flat universe



'''
Open Universe
'''
#Open universe matter approx
def open_universe (x,t):
    dx0 = np.sqrt(const * x[1] * np.square(x[0]) + 0.1)
    dx1 = -((3*x[1])*dx0)/x[0]
    return[dx0, dx1]
    
init_x = [1, 7.4*1e-27] #set the initial conditions (same as before)
time_x = np.arange(0,12e17, 10e10) #set time parameter
xx = odeint(open_universe, init_x, time_x) #Solves the ODE in an open universe



'''
Closed Universe
'''
#Closed universe matter approx
n = np.linspace(0,16,200)*s.pi
a_max = 0.7
a_matter= a_max*(1-np.cos(0.35*n))
t_matter = a_max*(n-np.sin(0.35*n))

#Slightly different method to solving for closed universe, since imaginary numbers becoming a bit of an issue
#used this approximation, since will be focusing on the flat universe scenario, not too problematic


#Plotting
fig, ax = plt.subplots()

ax.plot(time_y, yy[:,0], color = 'red', label = 'Flat Universe') #plot flat universe
ax.plot(time_x, xx[:,0]*1e-17 +1, color = 'green', label = 'Open Universe') #plot open universe
ax.plot(t_matter*1e17,(a_matter*0.5)+1, color = 'blue', label = 'Closed Universe') #plot closed universe


#Add a legend
legend = ax.legend(loc = 'upper left')
frame = legend.get_frame()
frame.set_facecolor('0.9')

for label in legend.get_texts():
    label.set_fontsize('large')

for label in legend.get_lines():
    label.set_linewidth(1.5)


#Label the graph
ax.set_title('Matter-Dominated Friedmann Universe')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Scale Factor of the Universe')


#..and set the limits
ax.set_xlim((0, 1.2e18))
#ax.set_ylim((1,11))
       
plt.show()
