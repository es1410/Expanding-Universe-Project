"""
PHY2071: Introduction to Astronomy Computational Project
E.Schoenrock (C)2016

Creates model fit of closed Universe based on Eqn (1) Perlmutter '95
- Theoretical model of closed universe
- plots distace modulus against redshift
"""

import numpy as np
import matplotlib.pyplot

execfile('/Users/Eric/Documents/hubble/READ_distmod_z.py') # load in the dictionary of data


def closed_uni_model(z):
	"""
	Input redshift values as an array, produces graphic model of 
	of eqn for fitting to Hubble diagram based on eqns in the lit.
	for closed universe. with omega m = 1, omega lambda = 0.5
	
	H0 = 69.32  (taken using current astropy.cosmology value)
	"""
	
	#Solution to eqn (1) in Perlmutter '95 for closed universe
	
	#break up the solution of integral to make life simpler
	x_num = (2*(z+1) * np.sqrt((2*z)+1) * np.arctan(np.sqrt(2*z + 1)))**4  
	x_dem = (np.sqrt( ((z+1)**2) * (2*z +1)) )
	x = x_num/x_dem
	
	M = 3.0#-19.164
	Dl = ((1+z)* np.sinh(x))/(69.32) 
	
#	print (str(Dl) + str(z))
	
	m = ( M + 5 * np.log10(Dl)) +25  #The distance modulus from theoretical model
#	print (str(m)) 
	#print  str(z)
	
	return[m]


# ------ Plots the model fit 

	
#fig, ax = plt.subplots()

for i in distmod_z.keys():
	redshift = distmod_z[i]['z']
	mm  = closed_uni_model(redshift)
	
	print (str(redshift)+str(mm))
#	ax.plot(redshift, mm,'o')
	
#plt.show()
