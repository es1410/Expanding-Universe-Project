"""
PHY2071: Introduction to Astonomy Comp. Project
E. Schoenrock (c)2016
"""

import numpy as np
from astropy.time import Time

def read_CSP_sn(ct_infile = '/Users/Eric/Documents/hubble/data.dat'):
    #print 'hello'
    ct_data = open(ct_infile, 'r')

    padded_data = []

    for i in ct_data:
        # print len(i)
        if len(i) != 89:
            while len(i) < 89:
                i = i + ' '
            padded_data.append(i)
        else:
            padded_data.append(i)
        
    snname = []
    EBV_host = []
    EBV_gal = []
    dm15 = []
    z = []
    distmod = []
    stretch = []
    
    for line in padded_data:
        print line[0:7], line[8:28], line[29:36], line[37:53], line[54:63], line[64:77], line[78:89]
        snname.append(line[0:7].replace(' ',''))
        #jd.append(float(line[10:18].replace(' ','')))
        print line[8:28].replace(' ','')
#        if raw_input():
#            print 'cont'
         
        if (line[8:28].replace(' ','')) == '':
#            print  'null'
            EBV_host.append(np.nan)
        else:
            EBV_host.append(float(line[8:28].replace(' ','')))
             
        if (line[29:36].replace(' ','')) == '':
#            print  'null'
            EBV_gal.append(np.nan)
        else:
            EBV_gal.append(float((line[29:36]).replace(' ','')))     
        
        if (line[37:53].replace(' ','')) == '':
#            print  'null'
            dm15.append(np.nan)
        else:
            dm15.append(float(line[37:53].replace(' ','')))

        if (line[54:63].replace(' ','')) == '':
#            print  'null'
            z.append(np.nan)
        else:
            z.append(float(line[54:63].replace(' ','')))        
       
        if (line[64:77].replace(' ','')) == '':
#            print  'null'
            distmod.append(np.nan)
        else:
            distmod.append(float(line[64:77].replace(' ','')))
        
        if (line[78:89].replace(' ','')) == '':
#            print  'null'
            stretch.append(np.nan)
        else:
            stretch.append(float(line[78:89].replace(' ','')))
        '''
        if (line[50:57].replace(' ','')) == '':
#            print  'null'
            k.append(np.nan)
        else:
            k.append(float(line[50:57].replace(' ','')))
            
        if (line[57:61].replace(' ','')) == '':
#            print  'null'
            dk.append(np.nan)
        else:
            dk.append(float(line[57:61].replace(' ','')))
       '''
#       data[0]: SN
#       data[1]: JD
#       data[2]: y
#       data[3]: dy
#       data[4]: j
#       data[5]: dj
#       data[6]: h
#       data[7]: dh
#       data[8]: k
#       data[9] dk
       
       
#        if line[18:24].replace('\n',' ') == '      ':
#            b.append(np.NaN)
#        else:
#            b.append(float(line[18:24]))
#
#        if line[25:30].replace('\n',' ') == '     ':
#            db.append(np.NaN)
#        else:
#            db.append(float(line[25:30]))
#
#        if line[31:37].replace('\n',' ') == '      ':
#            v.append(np.NaN)
#        else:
#            v.append(float(line[31:3/Users/berto/data/phot/CalanTololo/J_AJ_112_2408/table4.da7]))
#
#        if line[38:43].replace('\n',' ') == '     ':
#            dv.append(np.NaN)
#        else:
#            dv.append(float(line[38:43]))
#
#        if line[44:50].replace('\n',' ') == '      ':
#            r.append(np.NaN)/Users/berto/data/phot/CalanTololo/J_AJ_112_2408/table4.da
#        else:
#            r.append(float(line[44:50]))
#
#        if line[51:56].replace('\n',' ') == '     ':
#            dr.append(np.NaN)
#        else:
#            dr.append(float(line[51:56]))
#    for line in padded_data:
#        print line[3:9]
#        if line[57:63].replace('\n',' ') == '      ':
#            i.append(np.NaN)
#        else:unexpected i
#            i.append(float(line[57:63]))
#
#        if line[64:69].replace('\n',' ') == '     ':
#            di.append(np.NaN)
#        else:
#            di.append(float(line[64:69]))
#
    return snname, jd, y, dy, j, dj, h, dh, k, dk
    
def hubble_dict(ct_infile = '/Users/Eric/Documents/hubble/data.dat'):
    #print 'hello'
    ct_data = open(ct_infile, 'r')

    padded_data = []

    for i in ct_data:
        # print len(i)
        if len(i) != 89:
            while len(i) < 89:
                i = i + ' '
            padded_data.append(i)
        else:
            padded_data.append(i)
        
    snname = []
    EBV_host = []
    EBV_gal = []
    dm15 = []
    z = []
    distmod = []
    stretch = []
    
    for line in padded_data:
        print line[0:7], line[8:28], line[29:36], line[37:53], line[54:63], line[64:77], line[78:89]
        snname.append(line[0:7].replace(' ',''))
        #jd.append(float(line[10:18].replace(' ','')))
        print line[8:28].replace(' ','')
#        if raw_input():
#            print 'cont'
         
        if (line[8:28].replace(' ','')) == '':
#            print  'null'
            EBV_host.append(np.nan)
        else:
            EBV_host.append(float(line[8:28].replace(' ','')))
             
        if (line[29:36].replace(' ','')) == '':
#            print  'null'
            EBV_gal.append(np.nan)
        else:
            EBV_gal.append(float((line[29:36]).replace(' ','')))     
        
        if (line[37:53].replace(' ','')) == '':
#            print  'null'
            dm15.append(np.nan)
        else:
            dm15.append(float(line[37:53].replace(' ','')))

        if (line[54:63].replace(' ','')) == '':
#            print  'null'
            z.append(np.nan)
        else:
            z.append(float(line[54:63].replace(' ','')))        
       
        if (line[64:77].replace(' ','')) == '':
#            print  'null'
            distmod.append(np.nan)
        else:
            distmod.append(float(line[64:77].replace(' ','')))
        
        if (line[78:89].replace(' ','')) == '':
#            print  'null'
            stretch.append(np.nan)
        else:
            stretch.append(float(line[78:89].replace(' ','')))    
    
    all_data_dict = dict([('snname', snname), ('EBV_host', EBV_host), ('EBV_gal', EBV_gal), ('dm15', dm15), ('z', z), ('distmod',distmod), ('stretch',stretch)])
    
    sn_dict = dict()

    for k in np.unique(np.array(snname)):
        sn_dict[k] = dict()
        w = np.where(np.array(all_data_dict['snname']) == k)
        for j in all_data_dict.keys():
            sn_dict[k][j] = np.array(all_data_dict[j])[w]
    
    return sn_dict



hubble = hubble_dict()
