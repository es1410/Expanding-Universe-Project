'''
PHY2071: Introduction to Astonomy Comp. Project
E. Schoenrock (c)2016

Hubble Diagram script for low z SNe Ia sample from CSP dr1 and dr2

- stretch calculated using SNooPy
- Color calculated using SNooPy -- extinction corrections have been taken into account
'''

import os 
import matplotlib.pyplot as plt
import numpy as np

# -------- LOADING AND RUNNING CSP DATA --------
os.system("python /Users/Eric/Documents/hubble/hubble_data.py") #loads in hubble data script containing the redshifts
execfile('/Users/Eric/Documents/hubble/hubble_data.py') #runs the hubble data

os.system("python /Users/Eric/Documents/hubble/read_CSPX_sn.py") #loads CSP data release 1
os.system("python /Users/Eric/Documents/hubble/read_CSPY_sn.py") #loads CSP data release 2


execfile("/Users/Eric/Documents/hubble/read_CSPX_sn.py") #runs CSP data release 1
execfile("/Users/Eric/Documents/hubble/read_CSPY_sn.py") #runs CSP data release 2

# -------- MERGE TWO CSP DATA DICTIONARIES INTO 1 --------
CSP = data_OPT1.copy()
CSP.update(data_OPT2)

# --------- Open File to Save data to
f = open("/Users/Eric/Documents/hubble/distmod.txt", "w")

# -------- CREATE DATA POINTS FOR GRAPH---------

# -- Parameters --
alpha = 1.395	 #set value of constant alpha
beta = 3.164 		 #set value of constant beta
M = -19.164		 # set value for constant M 



fig, ax = plt.subplots()  #create fig for plotting data onto 

for i in hubble.keys():
	A_v = 3.1 * (hubble[i]['EBV_host'] + hubble[i]['EBV_gal'])  #finds the A_v for each SNe using 3.1 for MW
	extinction = A_v * (1-0.6556677218308204)		#extinction correction for each individual SNe Ia
	
	Col_BV = np.nanmin(CSP[i]['B'] - CSP[i]['V']) - extinction		#calculate the B-V col with extinction correction (Lira)
	
	SN = hubble[i]['snname']		#define the SN name
	redshift = hubble[i]['z']		#set the redshift to a parameter
	
	distmod_1 = -np.nanmin(CSP[i]['B']) + (alpha * (hubble[i]['stretch']-1)) - (beta * Col_BV) + M 
	distmod_2 = -np.nanmin(CSP[i]['B']) - (alpha * (hubble[i]['stretch']-1)) + (beta * Col_BV) + M  #calc the dist modulus
	 
	f.write( str(SN) + str(distmod_2) +  str(redshift) + str(distmod_1) +"\n")   #write data to file, used later
	
	distmod = (distmod_1 + distmod_2)/2
	print distmod
	#
	#ax.plot(hubble[i]['z'], (distmod)*-1, 'o', color = 'green')
	#ax.plot(redshift, (distmod_2) *-1, 'o', color = 'red')  #plot data

f.close()  #close file 

#ax.set_xlabel('Redshift z')
#ax.set_ylabel('Distance Modulus')

#plt.show()
