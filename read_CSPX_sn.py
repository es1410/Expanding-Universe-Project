import numpy as np
from astropy.time import Time

def read_CSPX_sn(ct_infile = '/Users/Eric/Documents/Python/CSP_Data/table4_dr2.dat'):
    """
    this code does some stuff    
    """
    ct_data = open(ct_infile, 'r')

    padded_data = []

    for i in ct_data:
        # print len(i)
        if len(i) != 85:
            while len(i) < 85:
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
        print line[3:9], line[10:17], line[20:26], line[27:30], line[31:37], line [38:41], line[42:48], line[50:52], line[53:59], line[60:63], line[64:70], line[71:74], line[75:81], line[82:85]
        snname.append(line[3:9].replace(' ',''))
        jd.append(float(line[10:17].replace(' ','')))
        print line[20:26].replace(' ','')
#        if raw_input():
#            print 'cont'
         
        if (line[20:26].replace(' ','')) == '':
#            print  'null'
            u.append(np.nan)
        else:
            u.append(float(line[20:26].replace(' ','')))
             
        if (line[27:30].replace(' ','')) == '':
#            print  'null'
            du.append(np.nan)
        else:
            du.append(float((line[27:30]).replace(' ','')))     
        
        if (line[31:37].replace(' ','')) == '':
#            print  'null'
            g.append(np.naalbumn)
        else:
            g.append(float(line[31:37].replace(' ','')))

        if (line[38:41].replace(' ','')) == '':
#            print  'null'
            dg.append(np.nan)
        else:
            dg.append(float(line[38:41].replace(' ','')))        
        
        if (line[42:48].replace(' ','')) == '':
#            print  'null'
            r.append(np.nan)
        else:
            r.append(float(line[42:48].replace(' ','')))
        
        if (line[50:52].replace(' ','')) == '':
#            print  'null'
            dr.append(np.nan)
        else:
            dr.append(float(line[50:52].replace(' ','')))
        
        if (line[53:59].replace(' ','')) == '':
#            print  'null'
            i.append(np.nan)
        else:
            i.append(float(line[53:59].replace(' ','')))
            
        if (line[60:63].replace(' ','')) == '':
#            print  'null'

            di.append(np.nan)
        else:
            di.append(float(line[60:63].replace(' ','')))
             
        if (line[64:70].replace(' ','')) == '':
#            print  'null'
            B.append(np.nan)
        else:
            B.append(float(line[64:70].replace(' ','')))
            
        if (line[71:74].replace(' ','')) == '':
#            print  'null'
            dB.append(np.nan)
        else:
            dB.append(float(line[71:74].replace(' ','')))
            
        if (line[75:81].replace(' ','')) == '':
#            print  'null'
            V.append(np.nan)
        else:
            V.append(float(line[75:81].replace(' ','')))
            
        if (line[82:85].replace(' ','')) == '':
#            print  'null'
            dV.append(np.nan)
        else:
            dV.append(float(line[82:85].replace(' ','')))

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
#        if line[44:50].realbumplace('\n',' ') == '      ':
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
    
def read_CSPX_sn_dict(ct_infile = '/Users/Eric/Documents/Python/CSP_Data/table4_dr2.dat'):
    
    ct_data = open(ct_infile, 'r')

    padded_data = []

    for i in ct_data:
        # print len(i)
        if len(i) != 85:
            while len(i) < 85:
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
        #print line[3:9], line[10:17], line[20:26], line[27:30], line[31:37], line [38:41], line[42:48], line[50:52], line[53:59], line[60:63], line[64:70], line[71:74], line[75:81], line[82:85]
        snname.append(line[3:9].replace(' ',''))
        jd.append(float(line[10:17].replace(' ','')))
        #print line[20:26].replace(' ','')
#        if raw_input():
#            print 'cont'
         
        if (line[20:26].replace(' ','')) == '':
#            print  'null'
            u.append(np.nan)
        else:
            u.append(float(line[20:26].replace(' ','')))
             
        if (line[27:30].replace(' ','')) == '':
#            print  'null'
            du.append(np.nan)
        else:
            du.append(float((line[27:30]).replace(' ',''))/1000.0)     
        
        if (line[31:37].replace(' ','')) == '':
#            print  'null'
            g.append(np.nan)
        else:
            g.append(float(line[31:37].replace(' ','')))

        if (line[38:41].replace(' ','')) == '':
#            print  'null'
            dg.append(np.nan)
        else:
            dg.append(float(line[38:41].replace(' ',''))/1000.0)        
        
        if (line[42:48].replace(' ','')) == '':
#            print  'null'
            r.append(np.nan)
        else:
            r.append(float(line[42:48].replace(' ','')))
        
        if (line[50:52].replace(' ','')) == '':
#            print  'null'
            dr.append(np.nan)
        else:
            dr.append(float(line[50:52].replace(' ',''))/1000.0)
        
        if (line[53:59].replace(' ','')) == '':
#            print  'null'
            i.append(np.nan)
        else:
            i.append(float(line[53:59].replace(' ','')))
            
        if (line[60:63].replace(' ','')) == '':
#            print  'null'
            di.append(np.nan)
        else:
            di.append(float(line[60:63].replace(' ',''))/1000.0)
             
        if (line[64:70].replace(' ','')) == '':
#            print  'null'
            B.append(np.nan)
        else:
            B.append(float(line[64:70].replace(' ','')))
            
        if (line[71:74].replace(' ','')) == '':
#            print  'null'
            dB.append(np.nan)
        else:
            dB.append(float(line[71:74].replace(' ',''))/1000.0)
            
        if (line[75:81].replace(' ','')) == '':
#            print  'null'
            V.append(np.nan)
        else:
            V.append(float(line[75:81].replace(' ','')))
            
        if (line[82:85].replace(' ','')) == '':
#            print  'null'
            dV.append(np.nan)
        else:
            dV.append(float(line[82:85].replace(' ',''))/1000.0)

    all_data_dict = dict([('snname', snname), ('jd', jd), ('u', u), ('du', du), ('g', g), ('dg', dg), ('r', r), ('dr', dr), ('i', i), ('di', di), ('B',B), ('dB', dB), ('V', V), ('dV', dV)])
    sn_dict = dict()

    for k in np.unique(np.array(snname)):
        sn_dict[k] = dict()
        w = np.where(np.array(all_data_dict['snname']) == k)
        for j in all_data_dict.keys():
            sn_dict[k][j] = np.array(all_data_dict[j])[w]
    
    return sn_dict


data_OPT2 = read_CSPX_sn_dict()
