"""
PHY2071: Introduction to Astronomy - Comp. Project
E. Schoenrock (c)2016

Calculates theoretical model values of closed universe
"""
import numpy as np
import matplotlib.pyplot as plt

execfile('/Users/Eric/Documents/hubble/READ_distmod_z.py') # load in the dictionary of data


def flat_uni_model(z):
	"""
	Input redshift values as an array, produces graphic model of 
	of eqn for fitting to Hubble diagram based on eqns in the lit.
	for a flat universe model with omega m = 1, omega lambda = 0
	
	
	H0 = 69.32  (taken using current astropy.cosmology value)
	"""
	
	#Flat Om = 1.0, Ol = 0.0
	M = -19.164
	Dl = -((1+z)/(69.32) * (-2/(np.sqrt(z**(-0.5)+1))))**(-3)  #Hubble constant 
	#print (str(Dl) + str(z))
	
	m = -( M + 5 * np.log10(Dl)) +45
#	print (str(m)) 
	#print  str(z)
	
	return[m]
	
#fig, ax = plt.subplots()

for i in distmod_z.keys():
	redshift = distmod_z[i]['z']
	mm  = flat_uni_model(redshift)
	
	print str(redshift)+str(mm)
	#ax.plot(redshift, mm,'o')
	
plt.show()
