from pandas import read_csv
import os
import matplotlib.pyplot as plt

base_dir = '/Users/gangch/Documents/temp/measfile'
exchange = 'NJDRA03BAL'
full_path = base_dir + r'/' + exchange

def format_data(path):
    #显示所有文件
    file_total = os.listdir(path)
    tmpfile1 = open('%s/tmp1.csv' %path,mode='w')
    tmpfile8 = open('%s/tmp8.csv' %path,mode='w')
    tmpfile9 = open('%s/tmp9.csv' % path, mode='w')
    tmpfile11 = open('%s/tmp11.csv' % path, mode='w')
    tmpfile12 = open('%s/tmp12.csv' % path, mode='w')
    tmpfile13 = open('%s/tmp13.csv' % path, mode='w')
    tmpfile14 = open('%s/tmp14.csv' % path, mode='w')
    tmpfile15 = open('%s/tmp15.csv' % path, mode='w')
    tmpfile16 = open('%s/tmp16.csv' % path, mode='w')
    tmpfile17 = open('%s/tmp17.csv' % path, mode='w')
    tmpfile18 = open('%s/tmp18.csv' % path, mode='w')




    for line in file_total:
        #更改文件名中的-_
        a = line.replace('-','.').replace('_','.')
        b = a.split('.')
        if b[1] == 'DIAMGLOBAL':
            df = read_csv('%s/%s' %(path,line),skiprows=2)
            result8 = [b[2],b[3],str(df.at[0,'MSGRCVPS']),
                                str(df.at[0,'MSGSNTPS']),
                                str(df.at[0,'UTLIRATI']),
                                str(df.at[0,'LPDETECT']),
                                str(df.at[0,'SVRQRECV']),
                                str(df.at[0,'SVANRECV']),
                                str(df.at[0,'SVRQSENT']),
                                str(df.at[0,'SVANSENT']),
                                str(df.at[0,'SVANFAIL']),
                                str(df.at[0,'SVRQRERT']),
                                str(df.at[0,'FORWRATI']),
                                str(df.at[0,'AVRGLOAD']),
                                str(df.at[0,'PEAKLOAD']),
                                str(df.at[0,'NUMMPSOL']),
                                str(df.at[0,'MAXMPSOL'])]
            tmpfile8.write(','.join(result8)+'\r\n')

        elif b[1] == 'DIAMSESSIONBIND':
            df = read_csv('%s/%s' % (path, line), skiprows=2)
            result9 = [b[2], b[3], str(df.at[0,'SARMRECV']),
                                    str(df.at[0,'SARMSENT']),
                                    str(df.at[0,'SSAARECV']),
                                    str(df.at[0,'FSAARECV']),
                                    str(df.at[0,'SSAASENT']),
                                    str(df.at[0,'FSAASENT']),
                                    str(df.at[0,'SURMRECV']),
                                    str(df.at[0,'SURMSENT']),
                                    str(df.at[0,'SSUARECV']),
                                    str(df.at[0,'FSUARECV']),
                                    str(df.at[0,'SSUASENT']),
                                    str(df.at[0,'FSUASENT']),
                                    str(df.at[0,'SDRMRECV']),
                                    str(df.at[0,'SDRMSENT']),
                                    str(df.at[0,'SSDARECV']),
                                    str(df.at[0,'FSDARECV']),
                                    str(df.at[0,'SSDASENT']),
                                    str(df.at[0,'FSDASENT']),
                                    str(df.at[0,'IRQMRECV']),
                                    str(df.at[0,'IRQMSENT']),
                                    str(df.at[0,'SIAMRECV']),
                                    str(df.at[0,'FIAMRECV']),
                                    str(df.at[0,'SIAMSENT']),
                                    str(df.at[0,'FIAMSENT']),
                                    str(df.at[0,'TOTALUSR']),
                                    str(df.at[0,'DUPLSBIP'])]
            tmpfile9.write(','.join(result9) + '\r\n')
        
        elif b[1] == 'DIAMS6A':
            df = read_csv('%s/%s' % (path, line), skiprows=2)
            result11 = [b[2], b[3], str(df.at[0, 'SVRQRERT']),
                                    str(df.at[0, 'SVRQRECV']),
                                    str(df.at[0, 'SVANRECV']),
                                    str(df.at[0, 'SVRQSENT']),
                                    str(df.at[0, 'SVANSENT']),
                                    str(df.at[0, 'SVANFAIL']),
                                    str(df.at[0, 'SVAFLOOP']),
                                    str(df.at[0, 'SVAFUNDL']),
                                    str(df.at[0, 'SVAFBUSY']),
                                    str(df.at[0, 'SVAFOTHE']),
                                    str(df.at[0, 'SVANFORW']),
                                    str(df.at[0, 'AIRMRECV']),
                                    str(df.at[0, 'AIAMRECV']),
                                    str(df.at[0, 'AIRMSENT']),
                                    str(df.at[0, 'AIAMSENT']),
                                    str(df.at[0, 'AIAMFAIL']),
                                    str(df.at[0, 'AIAFLOOP']),
                                    str(df.at[0, 'AIAFUNDL']),
                                    str(df.at[0, 'AIAFBUSY']),
                                    str(df.at[0, 'AIAFOTHE']),
                                    str(df.at[0, 'AIAMFORW']),
                                    str(df.at[0, 'ULRMRECV']),
                                    str(df.at[0, 'ULAMRECV']),
                                    str(df.at[0, 'ULRMSENT']),
                                    str(df.at[0, 'ULAMSENT']),
                                    str(df.at[0, 'ULAMFAIL']),
                                    str(df.at[0, 'ULAFLOOP']),
                                    str(df.at[0, 'ULAFUNDL']),
                                    str(df.at[0, 'ULAFBUSY']),
                                    str(df.at[0, 'ULAFOTHE']),
                                    str(df.at[0, 'ULAMFORW']),
                                    str(df.at[0, 'IDRMRECV']),
                                    str(df.at[0, 'IDAMRECV']),
                                    str(df.at[0, 'IDRMSENT']),
                                    str(df.at[0, 'IDAMSENT']),
                                    str(df.at[0, 'IDAMFAIL']),
                                    str(df.at[0, 'IDAFLOOP']),
                                    str(df.at[0, 'IDAFUNDL']),
                                    str(df.at[0, 'IDAFBUSY']),
                                    str(df.at[0, 'IDAFOTHE']),
                                    str(df.at[0, 'IDAMFORW']),
                                    str(df.at[0, 'FORWRATI'])]
            tmpfile11.write(','.join(result11) + '\r\n')

        elif b[1] == 'DIAMRX':
            df = read_csv('%s/%s' % (path, line), skiprows=2)
            result13 = [b[2], b[3], str(df.at[0,'SVRQRERT']),
                                    str(df.at[0,'SVRQRECV']),
                                    str(df.at[0,'SVANRECV']),
                                    str(df.at[0,'SVRQSENT']),
                                    str(df.at[0,'SVANSENT']),
                                    str(df.at[0,'SVANFAIL']),
                                    str(df.at[0,'SVAFLOOP']),
                                    str(df.at[0,'SVAFUNDL']),
                                    str(df.at[0,'SVAFBUSY']),
                                    str(df.at[0,'SVAFOTHE']),
                                    str(df.at[0,'SVANFORW']),
                                    str(df.at[0,'AARMRECV']),
                                    str(df.at[0,'AAAMRECV']),
                                    str(df.at[0,'AARMSENT']),
                                    str(df.at[0,'AAAMSENT']),
                                    str(df.at[0,'AAAMFAIL']),
                                    str(df.at[0,'AAAFLOOP']),
                                    str(df.at[0,'AAAFUNDL']),
                                    str(df.at[0,'AAAFBUSY']),
                                    str(df.at[0,'AAAFOTHE']),
                                    str(df.at[0,'AAAMFORW']),
                                    str(df.at[0,'FORWRATI'])]
            tmpfile13.write(','.join(result13) + '\r\n')

        elif b[1] == 'DIAMGX':
            df = read_csv('%s/%s' % (path, line), skiprows=2)
            result12 = [b[2], b[3], str(df.at[0,'SVRQRERT']),
                                    str(df.at[0,'SVRQRECV']),
                                    str(df.at[0,'SVANRECV']),
                                    str(df.at[0,'SVRQSENT']),
                                    str(df.at[0,'SVANSENT']),
                                    str(df.at[0,'SVANFAIL']),
                                    str(df.at[0,'SVAFLOOP']),
                                    str(df.at[0,'SVAFUNDL']),
                                    str(df.at[0,'SVAFBUSY']),
                                    str(df.at[0,'SVAFOTHE']),
                                    str(df.at[0,'SVANFORW']),
                                    str(df.at[0,'CCRMRECV']),
                                    str(df.at[0,'CCAMRECV']),
                                    str(df.at[0,'CCRMSENT']),
                                    str(df.at[0,'CCAMSENT']),
                                    str(df.at[0,'CCAMFAIL']),
                                    str(df.at[0,'CCAFLOOP']),
                                    str(df.at[0,'CCAFUNDL']),
                                    str(df.at[0,'CCAFBUSY']),
                                    str(df.at[0,'CCAFOTHE']),
                                    str(df.at[0,'CCAMFORW']),
                                    str(df.at[0,'FORWRATI'])]
            tmpfile12.write(','.join(result12) + '\r\n')

        elif b[1] == 'DIAMCX':
            df = read_csv('%s/%s' % (path, line), skiprows=2)
            result14 = [b[2], b[3], str(df.at[0,'SVRQRERT']),
                                    str(df.at[0,'SVRQRECV']),
                                    str(df.at[0,'SVANRECV']),
                                    str(df.at[0,'SVRQSENT']),
                                    str(df.at[0,'SVANSENT']),
                                    str(df.at[0,'SVANFAIL']),
                                    str(df.at[0,'SVAFLOOP']),
                                    str(df.at[0,'SVAFUNDL']),
                                    str(df.at[0,'SVAFBUSY']),
                                    str(df.at[0,'SVAFOTHE']),
                                    str(df.at[0,'SVANFORW']),
                                    str(df.at[0,'UARMRECV']),
                                    str(df.at[0,'UAAMRECV']),
                                    str(df.at[0,'UARMSENT']),
                                    str(df.at[0,'UAAMSENT']),
                                    str(df.at[0,'UAAMFAIL']),
                                    str(df.at[0,'UAAFLOOP']),
                                    str(df.at[0,'UAAFUNDL']),
                                    str(df.at[0,'UAAFBUSY']),
                                    str(df.at[0,'UAAFOTHE']),
                                    str(df.at[0,'UAAMFORW']),
                                    str(df.at[0,'MARMRECV']),
                                    str(df.at[0,'MAAMRECV']),
                                    str(df.at[0,'MARMSENT']),
                                    str(df.at[0,'MAAMSENT']),
                                    str(df.at[0,'MAAMFAIL']),
                                    str(df.at[0,'MAAFLOOP']),
                                    str(df.at[0,'MAAFUNDL']),
                                    str(df.at[0,'MAAFBUSY']),
                                    str(df.at[0,'MAAFOTHE']),
                                    str(df.at[0,'MAAMFORW']),
                                    str(df.at[0,'FORWRATI'])]
            tmpfile14.write(','.join(result14) + '\r\n')

        elif b[1] == 'DIAMSH':
            df = read_csv('%s/%s' % (path, line), skiprows=2)
            result15 = [b[2], b[3], str(df.at[0,'SVRQRERT']),
                                    str(df.at[0,'SVRQRECV']),
                                    str(df.at[0,'SVANRECV']),
                                    str(df.at[0,'SVRQSENT']),
                                    str(df.at[0,'SVANSENT']),
                                    str(df.at[0,'SVANFAIL']),
                                    str(df.at[0,'SVAFLOOP']),
                                    str(df.at[0,'SVAFUNDL']),
                                    str(df.at[0,'SVAFBUSY']),
                                    str(df.at[0,'SVAFOTHE']),
                                    str(df.at[0,'SVANFORW']),
                                    str(df.at[0,'UDRMRECV']),
                                    str(df.at[0,'UDAMRECV']),
                                    str(df.at[0,'UDRMSENT']),
                                    str(df.at[0,'UDAMSENT']),
                                    str(df.at[0,'UDAMFAIL']),
                                    str(df.at[0,'UDAFLOOP']),
                                    str(df.at[0,'UDAFUNDL']),
                                    str(df.at[0,'UDAFBUSY']),
                                    str(df.at[0,'UDAFOTHE']),
                                    str(df.at[0,'UDAMFORW']),
                                    str(df.at[0,'FORWRATI'])]
            tmpfile15.write(','.join(result15) + '\r\n')

        elif b[1] == 'DIAMZH':
            df = read_csv('%s/%s' % (path, line), skiprows=2)
            result16 = [b[2], b[3], str(df.at[0,'SVRQRERT']),
                                    str(df.at[0,'SVRQRECV']),
                                    str(df.at[0,'SVANRECV']),
                                    str(df.at[0,'SVRQSENT']),
                                    str(df.at[0,'SVANSENT']),
                                    str(df.at[0,'SVANFAIL']),
                                    str(df.at[0,'SVAFLOOP']),
                                    str(df.at[0,'SVAFUNDL']),
                                    str(df.at[0,'SVAFBUSY']),
                                    str(df.at[0,'SVAFOTHE']),
                                    str(df.at[0,'SVANFORW']),
                                    str(df.at[0,'FORWRATI'])]
            tmpfile16.write(','.join(result16) + '\r\n')

        elif b[1] == 'DIAMSLH':
            df = read_csv('%s/%s' % (path, line), skiprows=2)
            result17 = [b[2], b[3], str(df.at[0,'SVRQRERT']),
                                    str(df.at[0,'SVRQRECV']),
                                    str(df.at[0,'SVANRECV']),
                                    str(df.at[0,'SVRQSENT']),
                                    str(df.at[0,'SVANSENT']),
                                    str(df.at[0,'SVANFAIL']),
                                    str(df.at[0,'SVAFLOOP']),
                                    str(df.at[0,'SVAFUNDL']),
                                    str(df.at[0,'SVAFBUSY']),
                                    str(df.at[0,'SVAFOTHE']),
                                    str(df.at[0,'SVANFORW']),
                                    str(df.at[0,'FORWRATI'])]
            tmpfile17.write(','.join(result17) + '\r\n')

        elif b[1] == 'DIAMSLG':
            df = read_csv('%s/%s' % (path, line), skiprows=2)
            result18 = [b[2], b[3], str(df.at[0,'SVRQRERT']),
                                    str(df.at[0,'SVRQRECV']),
                                    str(df.at[0,'SVANRECV']),
                                    str(df.at[0,'SVRQSENT']),
                                    str(df.at[0,'SVANSENT']),
                                    str(df.at[0,'SVANFAIL']),
                                    str(df.at[0,'SVAFLOOP']),
                                    str(df.at[0,'SVAFUNDL']),
                                    str(df.at[0,'SVAFBUSY']),
                                    str(df.at[0,'SVAFOTHE']),
                                    str(df.at[0,'SVANFORW']),
                                    str(df.at[0,'FORWRATI'])]
            tmpfile18.write(','.join(result18) + '\r\n')

        elif b[1] == 'DIAMIP':
            df = read_csv('%s/%s' % (path, line), skiprows=2)
            #按行遍历DataFrame
            for index, row in df.iterrows():
                result1 = [b[2], b[3], str(row['NAME']),
                                    str(row['INCPACKS']),
                                    str(row['INCERROR']),
                                    str(row['OUTPACKS']),
                                    str(row['OUTERROR']),
                                    str(row['NUMCOLIS']),
                                    str(row['DEPTHQUE']),
                                    str(row['INCMBYTS']),
                                    str(row['OUTMBYTS'])]
                #print(result1)
                tmpfile1.write(','.join(result1) + '\r\n')

    tmpfile1.close()
    tmpfile8.close()
    tmpfile9.close()
    tmpfile11.close()
    tmpfile12.close()
    tmpfile13.close()
    tmpfile14.close()
    tmpfile15.close()
    tmpfile16.close()
    tmpfile17.close()
    tmpfile18.close()


#         elif b[1] == 'DIAMCX':
#             df = read_csv('%s/%s' % (path, line), skiprows=2)
#             result14 = [b[2], b[3], str(df.at[0, 'TOTALUSR']),
#                                     str(df.at[0,'SARMRECV'])]
#             tmpfile14.write(','.join(result14) + '\r\n')
#
# def sort_cx(path1,path2):
#     dat = read_csv('%s/tmp14.csv' %path2,names=['day',
#                                                'time',
#                                                ])
#     dat = dat.sort_values(by=["day", "time"])
#     dat = dat.reset_index(drop=True)
#     dat.to_csv('%s/result-cx.csv' %path1)

def sort_ip(path1,path2):
    dat = read_csv('%s/tmp1.csv' %path2,names=['day',
                                                'time',
                                                'NAME',
                                                'INCPACKS',
                                                'INCERROR',
                                                'OUTPACKS',
                                                'OUTERROR',
                                                'NUMCOLIS',
                                                'DEPTHQUE',
                                                'INCMBYTS',
                                                'OUTMBYTS'])
    dat = dat.sort_values(by=["day", "time"])
    dat = dat.reset_index(drop=True)
    dat.to_csv('%s/result-ip.csv' %path1)

def sort_slg(path1,path2):
    dat = read_csv('%s/tmp18.csv' %path2,names=['day',
                                               	'time',
                                               	'SVRQRERT',
                                                'SVRQRECV',
                                                'SVANRECV',
                                                'SVRQSENT',
                                                'SVANSENT',
                                                'SVANFAIL',
                                                'SVAFLOOP',
                                                'SVAFUNDL',
                                                'SVAFBUSY',
                                                'SVAFOTHE',
                                                'SVANFORW',
                                                'FORWRATI'])
    dat = dat.sort_values(by=["day", "time"])
    dat = dat.reset_index(drop=True)
    dat.to_csv('%s/result-slg.csv' %path1)

def sort_slh(path1,path2):
    dat = read_csv('%s/tmp17.csv' %path2,names=['day',
                                                'time',
                                                'SVRQRERT',
                                                'SVRQRECV',
                                                'SVANRECV',
                                                'SVRQSENT',
                                                'SVANSENT',
                                                'SVANFAIL',
                                                'SVAFLOOP',
                                                'SVAFUNDL',
                                                'SVAFBUSY',
                                                'SVAFOTHE',
                                                'SVANFORW',
                                                'FORWRATI'])
    dat = dat.sort_values(by=["day", "time"])
    dat = dat.reset_index(drop=True)
    dat.to_csv('%s/result-slh.csv' %path1)


def sort_zh(path1,path2):
    dat = read_csv('%s/tmp16.csv' %path2,names=['day',
                                                'time',
                                                'SVRQRERT'
                                                'SVRQRECV',
                                                'SVANRECV',
                                                'SVRQSENT',
                                                'SVANSENT',
                                                'SVANFAIL',
                                                'SVAFLOOP',
                                                'SVAFUNDL',
                                                'SVAFBUSY',
                                                'SVAFOTHE',
                                                'SVANFORW',
                                                'FORWRATI'])
    dat = dat.sort_values(by=["day", "time"])
    dat = dat.reset_index(drop=True)
    dat.to_csv('%s/result-zh.csv' %path1)

def sort_sh(path1,path2):
    dat = read_csv('%s/tmp15.csv' %path2,names=['day',
                                                'time',
                                                'SVRQRERT',
                                                'SVRQRECV',
                                                'SVANRECV',
                                                'SVRQSENT',
                                                'SVANSENT',
                                                'SVANFAIL',
                                                'SVAFLOOP',
                                                'SVAFUNDL',
                                                'SVAFBUSY',
                                                'SVAFOTHE',
                                                'SVANFORW',
                                                'UDRMRECV',
                                                'UDAMRECV',
                                                'UDRMSENT',
                                                'UDAMSENT',
                                                'UDAMFAIL',
                                                'UDAFLOOP',
                                                'UDAFUNDL',
                                                'UDAFBUSY',
                                                'UDAFOTHE',
                                                'UDAMFORW',
                                                'FORWRATI'])
    dat = dat.sort_values(by=["day", "time"])
    dat = dat.reset_index(drop=True)
    dat.to_csv('%s/result-sh.csv' %path1)

def sort_cx(path1,path2):
    dat = read_csv('%s/tmp14.csv' %path2,names=['day',
                                               	'time',
                                                'SVRQRERT',
                                                'SVRQRECV',
                                                'SVANRECV',
                                                'SVRQSENT',
                                                'SVANSENT',
                                                'SVANFAIL',
                                                'SVAFLOOP',
                                                'SVAFUNDL',
                                                'SVAFBUSY',
                                                'SVAFOTHE',
                                                'SVANFORW',
                                                'UARMRECV',
                                                'UAAMRECV',
                                                'UARMSENT',
                                                'UAAMSENT',
                                                'UAAMFAIL',
                                                'UAAFLOOP',
                                                'UAAFUNDL',
                                                'UAAFBUSY',
                                                'UAAFOTHE',
                                                'UAAMFORW',
                                                'MARMRECV',
                                                'MAAMRECV',
                                                'MARMSENT',
                                                'MAAMSENT',
                                                'MAAMFAIL',
                                                'MAAFLOOP',
                                                'MAAFUNDL',
                                                'MAAFBUSY',
                                                'MAAFOTHE',
                                                'MAAMFORW',
                                                'FORWRATI'])
    dat = dat.sort_values(by=["day", "time"])
    dat = dat.reset_index(drop=True)
    dat.to_csv('%s/result-cx.csv' %path1)
    
def sort_gx(path1,path2):
    dat = read_csv('%s/tmp12.csv' %path2,names=['day',
                                                'time',
                                                'SVRQRERT',
                                                'SVRQRECV',
                                                'SVANRECV',
                                                'SVRQSENT',
                                                'SVANSENT',
                                                'SVANFAIL',
                                                'SVAFLOOP',
                                                'SVAFUNDL',
                                                'SVAFBUSY',
                                                'SVAFOTHE',
                                                'SVANFORW',
                                                'CCRMRECV',
                                                'CCAMRECV',
                                                'CCRMSENT',
                                                'CCAMSENT',
                                                'CCAMFAIL',
                                                'CCAFLOOP',
                                                'CCAFUNDL',
                                                'CCAFBUSY',
                                                'CCAFOTHE',
                                                'CCAMFORW',
                                                'FORWRATI'])
    dat = dat.sort_values(by=["day", "time"])
    dat = dat.reset_index(drop=True)
    dat.to_csv('%s/result-gx.csv' %path1)

def sort_rx(path1,path2):
    dat = read_csv('%s/tmp13.csv' %path2,names=['day',
                                                'time',
                                                'SVRQRERT',
                                                'SVRQRECV',
                                                'SVANRECV',
                                                'SVRQSENT',
                                                'SVANSENT',
                                                'SVANFAIL',
                                                'SVAFLOOP',
                                                'SVAFUNDL',
                                                'SVAFBUSY',
                                                'SVAFOTHE',
                                                'SVANFORW',
                                                'AARMRECV',
                                                'AAAMRECV',
                                                'AARMSENT',
                                                'AAAMSENT',
                                                'AAAMFAIL',
                                                'AAAFLOOP',
                                                'AAAFUNDL',
                                                'AAAFBUSY',
                                                'AAAFOTHE',
                                                'AAAMFORW',
                                                'FORWRATI'])
    dat = dat.sort_values(by=["day", "time"])
    dat = dat.reset_index(drop=True)
    dat.to_csv('%s/result-rx.csv' %path1)

def sort_s6a(path1,path2):
    dat = read_csv('%s/tmp11.csv' %path2,names=['day',
                                                'time',
                                                'SVRQRERT',
                                                'SVRQRECV',
                                                'SVANRECV',
                                                'SVRQSENT',
                                                'SVANSENT',
                                                'SVANFAIL',
                                                'SVAFLOOP',
                                                'SVAFUNDL',
                                                'SVAFBUSY',
                                                'SVAFOTHE',
                                                'SVANFORW',
                                                'AIRMRECV',
                                                'AIAMRECV',
                                                'AIRMSENT',
                                                'AIAMSENT',
                                                'AIAMFAIL',
                                                'AIAFLOOP',
                                                'AIAFUNDL',
                                                'AIAFBUSY',
                                                'AIAFOTHE',
                                                'AIAMFORW',
                                                'ULRMRECV',
                                                'ULAMRECV',
                                                'ULRMSENT',
                                                'ULAMSENT',
                                                'ULAMFAIL',
                                                'ULAFLOOP',
                                                'ULAFUNDL',
                                                'ULAFBUSY',
                                                'ULAFOTHE',
                                                'ULAMFORW',
                                                'IDRMRECV',
                                                'IDAMRECV',
                                                'IDRMSENT',
                                                'IDAMSENT',
                                                'IDAMFAIL',
                                                'IDAFLOOP',
                                                'IDAFUNDL',
                                                'IDAFBUSY',
                                                'IDAFOTHE',
                                                'IDAMFORW',
                                                'FORWRATI'])
    dat = dat.sort_values(by=["day", "time"])
    dat = dat.reset_index(drop=True)
    dat.to_csv('%s/result-s6a.csv' %path1)

def sort_sessionbind(path1,path2):
    dat = read_csv('%s/tmp9.csv' %path2,names=['day',
                                               'time',
                                                'SARMRECV',
                                                'SARMSENT',
                                                'SSAARECV',
                                                'FSAARECV',
                                                'SSAASENT',
                                                'FSAASENT',
                                                'SURMRECV',
                                                'SURMSENT',
                                                'SSUARECV',
                                                'FSUARECV',
                                                'SSUASENT',
                                                'FSUASENT',
                                                'SDRMRECV',
                                                'SDRMSENT',
                                                'SSDARECV',
                                                'FSDARECV',
                                                'SSDASENT',
                                                'FSDASENT',
                                                'IRQMRECV',
                                                'IRQMSENT',
                                                'SIAMRECV',
                                                'FIAMRECV',
                                                'SIAMSENT',
                                                'FIAMSENT',
                                                'TOTALUSR',
                                                'DUPLSBIP'])
    dat = dat.sort_values(by=["day", "time"])
    dat = dat.reset_index(drop=True)
    dat.to_csv('%s/result-sessionbind.csv' %path1)

def sort_global(path1,path2):
    dat = read_csv('%s/tmp8.csv' %path2,names=['day',
                                                'time',
                                                'MSGRCVPS',
                                                'MSGSNTPS',
                                                'UTLIRATI',
                                                'LPDETECT',
                                                'SVRQRECV',
                                                'SVANRECV',
                                                'SVRQSENT',
                                                'SVANSENT',
                                                'SVANFAIL',
                                                'SVRQRERT',
                                                'FORWRATI',
                                                'AVRGLOAD',
                                                'PEAKLOAD',
                                                'NUMMPSOL',
                                                'MAXMPSOL'],sep=',')
        #按日期和时间排序
    dat = dat.sort_values(by = ["day","time"])
    #重新排列序号
    dat = dat.reset_index(drop=True)
    # dat['day'] = dat['day'].astype(str)
    # dat['time'] = dat['time'].astype(str)
    dat.to_csv('%s/result-global.csv' %path1)
    # year = dat['day'].str.slice(0,4)
    # month = dat['day'].str.slice(4,6)
    # days = dat['day'].str.slice(6,8)
    # print('year %s month %s day %s' %(year,month,days))
    # print(dat.head(100))



format_data(full_path)
sort_ip(base_dir,full_path)
# sort_global(base_dir,full_path)
# sort_sessionbind(base_dir,full_path)
# sort_s6a(base_dir,full_path)
# sort_gx(base_dir,full_path)
# sort_rx(base_dir,full_path)
# sort_cx(base_dir,full_path)
# sort_sh(base_dir,full_path)
# sort_zh(base_dir,full_path)
# sort_slh(base_dir,full_path)
# sort_slg(base_dir,full_path)







# data = dat['ULTIRATI']
# plt.hist(data,bins=40,normed=0,facecolor="blue",
#          edgecolor="red",alpha=0.7)
# plt.show()


