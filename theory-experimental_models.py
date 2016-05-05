"""
PHY2071: Introduction to Astonomy Comp. Project
E. Schoenrock (c)2016

Script plots experimental data with theoretical models in one graph. 
Make comparison between data and theoretical scenarios. 
"""

import numpy as np
import matplotlib.pyplot as plt

# --- Redshift values

z = [0.0055, 0.0057, 0.0067, 0.007899, 0.010847
, 0.0126, 0.0139, 0.0141, 0.01491, 0.0151, 0.01512, 0.015701, 
0.015786, 0.016739, 0.0177, 0.019207, 0.0213, 0.0217, 0.022012, 
0.0226]#, 0.0309, 0.030985, 0.0322 , 0.0334, 0.034043, 0.0455]

# --- Distance modulus 
'''
distmod = [33.02917168 , 34.30653666 , 33.85064, 32.88698665, 
33.39945648 ,34.11192313, 36.163624, 35.94712654, 34.07688159, 35.20852805, 
35.97277071, 34.87731939, 34.80190467, 34.75625656, 35.60303546, 34.61771678 , 
36.00031779, 35.91952653, 35.91219057, 35.94799018, 35.7983958, 36.49280234, 
36.90312483, 34.8917291, 35.98822186, 38.99698432]
'''
distmod = [32.444, 33.792, 33.175, 33.015, 33.605, 34.073, 35.059, 35.326,
34.486, 34.831, 35.203, 34.653, 34.406, 34.352, 35.131, 34.861,
35.989, 35.901, 35.177, 35.199]
 

# --- Error values

dist_err = [11.1806541, 12.20684345, 12.80652283, 12.20684345, 
10.05022522, 11.66220506, 12.20684345, 10.06066732, 12.80652283, 10.14381718, 
13.4538852, 12.80652283, 12.80652283, 11.66220506, 10.49985842, 12.20684345, 
11.18065414, 13.4538852, 12.80652283, 12.80652283]

#error for the graphing process
error = 0.16*np.square(dist_err)/(distmod)

## --------------------------------------------------------------------- ##


#-------------- THEORETICAL MODEL OF DIST MOD VALUES (FLAT UNIVERSE)
flat_dist = np.array([31.15551779, 31.17940736, 31.29932204, 31.44412944, 31.80498416,
32.0228394, 32.18599103, 32.21121235, 32.31369003, 32.33780511,
32.34034525, 32.41427833, 32.42511776, 32.54705106, 32.67076169,
32.86629199, 33.1409818, 33.19389515, 33.23526076, 33.3134415])

#-------------- THEORETICAL MODEL OF DIST MOD VALUES (OPEN UNIVERSE)
open_dist = np.array([31.15551779, 31.17940736, 31.29932204, 31.44412944, 31.80498416,
32.0228394, 32.18599103, 32.21121235, 32.31369003, 32.33780511,
32.34034525, 32.41427833, 32.42511776, 32.54705106, 32.67076169,
32.86629199, 33.1409818, 33.19389515, 33.23526076, 33.3134415])

#-------------- THEORETICAL MODEL OF DIST MOD VALUES (CLOSED UNIVERSE)
closed_dist = np.array([31.15551779, 31.17940736, 31.29932204, 31.44412944, 31.80498416,
32.0228394, 32.18599103, 32.21121235, 32.31369003, 32.33780511,
32.34034525, 32.41427833, 32.42511776, 32.54705106, 32.67076169,
32.86629199, 33.1409818, 33.19389515, 33.23526076, 33.3134415])


## --------------------------------------------------------------------- ##

# --- Create model for data set 

poly_1 = np.polyfit(z, distmod, 2)  #fits the data to a '3' degree poly - n to be determined by chi^2
f1 = np.poly1d(poly_1)  #get values for poly

x = np.linspace(0.004, 0.025, 60)  # create array of redshifts for model 
y = f1(x)	#model poly with the tabulated redshifts  

# ------ CREATE THEORETICAL MODEL FOR FLAT UNIVERSE 
poly_2 = np.polyfit(z, flat_dist, 2)
f2 = np.poly1d(poly_2)

tm = f2(x)

# ------ CREATE THEORETICAL MODEL FOR OPEN UNIVERSE 
poly_3 = np.polyfit(z, open_dist, 2)
f3 = np.poly1d(poly_3)

tmo = f3(x)

# ------ CREATE THEORETICAL MODEL FOR Closed UNIVERSE 
poly_4 = np.polyfit(z, closed_dist, 2)
f4 = np.poly1d(poly_4)

tmc = f4(x)

#---- plot the data and model ----

fig, ax = plt.subplots()

ax.plot(x,y,'-', color = 'red', label = r'CSP SNe Ia Model')  #data model 
ax.plot(x, tm, '--', color = 'blue', label =r'Einstein-Desitter Universe ($\Omega_{M} = 1, \Omega_{\Lambda} = 0$)') # theoretical model for flat universe
ax.plot(x, tmo, '--', color = 'black', label = r' Open Universe ($\Omega_{M} = 0.5, \Omega_{\Lambda} = 0$) ')  #theoretical open universe model
ax.plot(x, tmc, '--', color = 'green', label =r'Closed Universe ($\Omega_{M} = 2, \Omega_{\Lambda} = 0$)')  #theoretical closed universe model

#plot SNe Ia data
ax.errorbar(z, distmod, yerr = error, ecolor = '#336699',color = '#336699', linestyle = 'none', fmt='o')
ax.set_xlim((0.005, 0.025))

#- Add legend to graph
legend = ax.legend(loc = 'bottom right')
frame = legend.get_frame()
frame.set_facecolor('0.9')

for label in legend.get_texts():
    label.set_fontsize('large')

for label in legend.get_lines():
    label.set_linewidth(1.5)


plt.show()
