'''
PHY2071: Introduction to Astronomy
E.Schoenrock (C)2016

Script to calculate chi square fits for SNe Ia  model from CSP data 

'''
import os
import numpy as np


# ---- Loads in the data for the sample --- 

os.system("python /Users/Eric/Documents/hubble/READ_distmod_z.py") #loads distance modulus data
execfile("/Users/Eric/Documents/hubble/READ_distmod_z.py") #runs dist mod data


alpha_beta_err = np.square(0.11/1.395) + np.square(0.09/3.164)

for i in distmod_z.keys():
    numerator = np.square( distmod_z[i]['distmod_data'] - distmod_z[i]['distmod_mod'] )  #numerator in  the chi square fitting
    error_MB =  np.square( distmod_z[i]['error_mb']*100)  #error in the light curve fitting
    sigma = np.sqrt( alpha_beta_err + 100 + error_MB)
    chi = numerator/sigma
    #print sigma
    print chi
