import numpy as np
from astropy.time import Time

def READ_distmod_z(ct_infile = '/Users/Eric/Documents/hubble/distmod_z.dat'):
    #print 'hello'
    ct_data = open(ct_infile, 'r')

    padded_data = []

    for i in ct_data:
        # print len(i)
        if len(i) != 48:
            while len(i) < 48:
                i = i + ' '
            padded_data.append(i)
        else:
            padded_data.append(i)
        
    snname = []
    distmod_data = []
    z = []
    distmod_mod = []
    error_mb = []
    
    for line in padded_data:
        #print line[0:6], line[7:19], line[20:28]
        snname.append(line[0:6].replace(' ',''))
        #jd.append(float(line[10:18].replace(' ','')))
        #print line[7:19].replace(' ','')
#        if raw_input():
#            print 'cont'
         
        if (line[7:19].replace(' ','')) == '':
#            print  'null'
            distmod_data.append(np.nan)
        else:
            distmod_data.append(float(line[7:19].replace(' ','')))
             
        if (line[20:28].replace(' ','')) == '':
#            print  'null'
            z.append(np.nan)
        else:
            z.append(float((line[20:28]).replace(' ','')))     
        
        if (line[29:42].replace(' ','')) == '':
#            print  'null'
            distmod_mod.append(np.nan)
        else:
            distmod_mod.append(float((line[29:42]).replace(' ','')))
            
        if (line[43:48].replace(' ','')) == '':
#            print  'null'
            error_mb.append(np.nan)
        else:
            error_mb.append(float((line[43:48]).replace(' ','')))
            
            

    return snname, distmod_data, z, distmod_mod, error_mb
    
def READ_distmod_z(ct_infile = '/Users/Eric/Documents/hubble/distmod_z.dat'):
    #print 'hello'
    ct_data = open(ct_infile, 'r')

    padded_data = []

    for i in ct_data:
        # print len(i)
        if len(i) != 48:
            while len(i) < 48:
                i = i + ' '
            padded_data.append(i)
        else:
            padded_data.append(i)
        
    snname = []
    distmod_data = []
    z = []
    distmod_mod = []
    error_mb = []
    
    for line in padded_data:
        #print line[0:6], line[7:19], line[20:28]
        snname.append(line[0:7].replace(' ',''))
        #jd.append(float(line[10:18].replace(' ','')))
        #print line[7:19].replace(' ','')
#        if raw_input():
#            print 'cont'
         
        if (line[7:19].replace(' ','')) == '':
#            print  'null'
            distmod_data.append(np.nan)
        else:
        	distmod_data.append(float(line[7:19].replace(' ','')))
             
        if (line[20:28].replace(' ','')) == '':
#            print  'null'
            z.append(np.nan)
        else:
            z.append(float((line[20:28]).replace(' ','')))     
        
        if (line[29:42].replace(' ','')) == '':
#            print  'null'
            distmod_mod.append(np.nan)
        else:
            distmod_mod.append(float((line[29:42]).replace(' ','')))
        
        if (line[43:48].replace(' ','')) == '':
#            print  'null'
            error_mb.append(np.nan)
        else:
            error_mb.append(float((line[42:48]).replace(' ','')))
 
 
    all_data_dict = dict([('snname', snname), ('distmod_data',distmod_data), ('z', z), ('distmod_mod', distmod_mod), ('error_mb', error_mb) ])
    
    sn_dict = dict()

    for k in np.unique(np.array(snname)):
        sn_dict[k] = dict()
        w = np.where(np.array(all_data_dict['snname']) == k)
        for j in all_data_dict.keys():
            sn_dict[k][j] = np.array(all_data_dict[j])[w]
    
    return sn_dict



distmod_z = READ_distmod_z()
