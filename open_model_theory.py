"""
PHY2071: Introduction to Astonomy Comp. Project
E. Schoenrock (c)2016
"""


import numpy as np
import matplotlib.pyplot as plt
import os

execfile('/Users/Eric/Documents/hubble/READ_distmod_z.py') # load in the dictionary of data


def open_uni_model(z):
	"""
	Input redshift values as an array, produces graphic model of 
	of eqn for fitting to Hubble diagram based on eqns in the lit.
	for open universe. with omega m = 0.5, omega lambda = 0
	
	H0 = 69.32  (taken using current astropy.cosmology value)
	"""
	
	#open Om = 0.5, Ol = 0.0
	
	loggs = (np.log10(-1+np.sqrt(z+2)) - np.log10(np.sqrt(z+2)+1))
	
	x_num = ((z+1) * np.sqrt(z+2) * loggs)
	x_dem = (np.sqrt( ((z+1)**2) * (z+2)))
	
	x = (-1) *  (x_num/x_dem)**(-3)
#	print x
	M = -19.164
	
	Dl = ((1+z**2) *np.sin(x)) /(69.32 * np.sqrt(0.5))
	
#	print (str(Dl) + str(z))
	
	m = (( M + 5 * np.log10(Dl**(-3))) +25) 
	print (str(m) + str(z)) 
	#print  str(z)
	
	return[m]
	
#fig, ax = plt.subplots()

for i in distmod_z.keys():
	redshift = distmod_z[i]['z']
	mm  = open_uni_model(redshift)
#	print str(redshift) + str(mm)
	
#	print redshift
#	ax.plot(redshift, mm,'o')
	
#plt.show()
