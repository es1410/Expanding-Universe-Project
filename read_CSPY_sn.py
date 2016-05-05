import numpy as np
from astropy.time import Time

def read_CSPY_sn(ct_infile = '/Users/Eric/Documents/Python/CSP_Data/table4_dr1.dat'):

    ct_data = open(ct_infile, 'r')

    padded_data = []

    for i in ct_data:
        # print len(i)
        if len(i) != 90:
            while len(i) < 90:
                i = i + ' '
            padded_data.append(i)
        else:
            padded_data.append(i)
        
    snname = []
    jd = []
    u = []
    du = []
    g = []
    dg = []
    r = []
    dr = []
    i = []
    di = []
    B = []
    dB = []
    V = []
    dV = []
    
    for line in padded_data:
        print line[0:7], line[7:18], line[18:25], line[25:30], line[30:37], line [37:42], line[42:49], line[49:54], line[54:61], line[61:66], line[66:73], line [73:78], line[78:85], line[85:90]
        snname.append(line[0:7].replace(' ',''))
        jd.append(float(line[7:18].replace(' ','')))
        print line[18:25].replace(' ','')
#        if raw_input():
#            print 'cont'
         
        if (line[18:25].replace(' ','')) == '':
#            print  'null'
            u.append(np.nan)
        else:
            u.append(float(line[18:25].replace(' ','')))
             
        if (line[25:30].replace(' ','')) == '':
#            print  'null'
            du.append(np.nan)
        else:
            du.append(float((line[25:30]).replace(' ','')))     
        
        if (line[30:37].replace(' ','')) == '':
#            print  'null'
            g.append(np.nan)
        else:
            g.append(float(line[30:37].replace(' ','')))

        if (line[37:42].replace(' ','')) == '':
#            print  'null'
            dg.append(np.nan)
        else:
            dg.append(float(line[37:42].replace(' ','')))        
        
        if (line[42:49].replace(' ','')) == '':
#            print  'null'
            r.append(np.nan)
        else:
            r.append(float(line[42:49].replace(' ','')))
        
        if (line[49:54].replace(' ','')) == '':
#            print  'null'
            dr.append(np.nan)
        else:
            dr.append(float(line[49:54].replace(' ','')))
        
        if (line[54:61].replace(' ','')) == '':
#            print  'null'
            i.append(np.nan)
        else:
            i.append(float(line[54:61].replace(' ','')))
            
        if (line[61:66].replace(' ','')) == '':
#            print  'null'
            di.append(np.nan)
        else:
            di.append(float(line[61:66].replace(' ','')))
            
        if (line[66:73].replace(' ','')) == '':
#            print  'null'
            B.append(np.nan)
        else:
            B.append(float(line[66:73].replace(' ','')))
            
        if (line[73:78].replace(' ','')) == '':
#            print  'null'
            dB.append(np.nan)
        else:
            dB.append(float(line[73:78].replace(' ','')))
            
        if (line[78:85].replace(' ','')) == '':
#            print  'null'
            V.append(np.nan)
        else:
            V.append(float(line[78:85].replace(' ','')))
            
        if (line[85:90].replace(' ','')) == '':
#            print  'null'
            dV.append(np.nan)
        else:
            dV.append(float(line[85:90].replace(' ','')))
       
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
    return snname, jd, u, du, g, dg, r, dr, i, di, B, dB, V, dV
    
def read_CSPY_sn_dict(ct_infile = '/Users/Eric/Documents/Python/CSP_Data/table4_dr1.dat'):

    ct_data = open(ct_infile, 'r')

    padded_data = []

    for i in ct_data:
        # print len(i)
        if len(i) != 90:
            while len(i) < 90:
                i = i + ' '
            padded_data.append(i)
        else:
            padded_data.append(i)
        
    snname = []
    jd = []
    u = []
    du = []
    g = []
    dg = []
    r = []
    dr = []   
    i = []
    di = []
    B = []
    dB = []
    V = []
    dV = []
    
    for line in padded_data:
        #print line[0:7], line[7:18], line[18:25], line[25:30], line[30:37], line [37:42], line[42:49], line[49:54], line[54:61], line[61:66], line[66:73], line [73:78], line[78:85], line[85:90]
        snname.append(line[0:7].replace(' ',''))
        jd.append(float(line[7:18].replace(' ','')))
        #print line[18:25].replace(' ','')
#        if raw_input():
#            print 'cont'
         
        if (line[18:25].replace(' ','')) == '':
#            print  'null'
            u.append(np.nan)
        else:
            u.append(float(line[18:25].replace(' ','')))
             
        if (line[25:30].replace(' ','')) == '':
#            print  'null'
            du.append(np.nan)
        else:
            du.append(float((line[25:30]).replace(' ','')))     
        
        if (line[30:37].replace(' ','')) == '':
#            print  'null'
            g.append(np.nan)
        else:
            g.append(float(line[30:37].replace(' ','')))

        if (line[37:42].replace(' ','')) == '':
#            print  'null'
            dg.append(np.nan)
        else:
            dg.append(float(line[37:42].replace(' ','')))        
        
        if (line[42:49].replace(' ','')) == '':
#            print  'null'
            r.append(np.nan)
        else:
            r.append(float(line[42:49].replace(' ','')))
        
        if (line[49:54].replace(' ','')) == '':
#            print  'null'
            dr.append(np.nan)
        else:
            dr.append(float(line[49:54].replace(' ','')))
        
        if (line[54:61].replace(' ','')) == '':
#            print  'null'
            i.append(np.nan)
        else:
            i.append(float(line[54:61].replace(' ','')))
            
        if (line[61:66].replace(' ','')) == '':
#            print  'null'
            di.append(np.nan)
        else:
            di.append(float(line[61:66].replace(' ','')))
            
        if (line[66:73].replace(' ','')) == '':
#            print  'null'
            B.append(np.nan)
        else:
            B.append(float(line[66:73].replace(' ','')))
            
        if (line[73:78].replace(' ','')) == '':
#            print  'null'
            dB.append(np.nan)
        else:
            dB.append(float(line[73:78].replace(' ','')))
            
        if (line[78:85].replace(' ','')) == '':
#            print  'null'
            V.append(np.nan)
        else:
            V.append(float(line[78:85].replace(' ','')))
            
        if (line[85:-1].replace(' ','')) == '':
            #print  'null'
            dV.append(np.nan)
        else:
           # print line[85:-1]
            dV.append(float(line[85:-1].replace(' ','')))

    all_data_dict = dict([('snname', snname), ('jd', jd), ('u', u), ('du', du), ('g', g), ('dg', dg), ('r', r), ('dr', dr), ('i', i), ('di', di), ('B', B), ('dB', dB), ('V', V), ('dV', dV)])
    sn_dict = dict()

    for k in np.unique(np.array(snname)):
        sn_dict[k] = dict()
        w = np.where(np.array(all_data_dict['snname']) == k)
        for j in all_data_dict.keys():
            sn_dict[k][j] = np.array(all_data_dict[j])[w]
    
    return sn_dict



data_OPT1 = read_CSPY_sn_dict()
def pad_CSP1(ct_infile = '/Users/Eric/Documents/Python/CSP_Data/table4_dr1.dat'):

    ct_data = open(ct_infile, 'r')

    padded_data = []

    for i in ct_data:
        # print len(i)
        if len(i) != 90:
            while len(i) < 90:
                i = i + ' '
            padded_data.append(i)
        else:
            padded_data.append(i)
    return padded_data
