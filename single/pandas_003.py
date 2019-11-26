from pandas import read_csv
import os
import matplotlib.pyplot as plt

base_dir = '/Users/gangch/Documents/temp/measfile'
exchange = 'NJDRA03BAL'
full_path = base_dir + r'/' + exchange

#def format_data(path):
    #显示所有文件
file_total = os.listdir(full_path)
# tmpfile5 = open('%s/tmp5.csv' %base_dir,mode='w')
#
def format_ls(path,file,day,time):
    df = read_csv('%s/%s' % (path,file), skiprows=2)
    for index, row in df.iterrows():
        result = [day,time,str(row['NAME']),
                            str(row['NUMBUNAV']),
                            str(row['DURAUNAV']),
                            str(row['DATARECV']),
                            str(row['SVRQRECV']),
                            str(row['SVANRECV']),
                            str(row['DATASENT']),
                            str(row['SVRQSENT']),
                            str(row['SVANSENT']),
                            str(row['SVANFAIL']),
                            str(row['SVAFLOOP']),
                            str(row['SVAFUNDL']),
                            str(row['SVAFBUSY']),
                            str(row['SVAFOTHE']),
                            str(row['SVANFORW']),
                            str(row['FORWRATI']),
                            str(row['RCVSRDIS']),
                            str(row['SNTSRDIS']),
                            str(row['RCVSADIS']),
                            str(row['SNTSADIS']),
                            str(row['SVRQDISC']),
                            str(row['SVANDISC'])]
        print(result)
        result.to_excel()
#         tmpfile5.write(','.join(result) + '\r\n')
#
#
# for line in file_total:
#     #更改文件名中的-_
#     a = line.replace('-','.').replace('_','.')
#     b = a.split('.')
#     if b[1] == 'DIAMLINKSET':
#         format_ls(full_path,line,b[2],b[3])
#         # df = read_csv('%s/%s' % (full_path, line), skiprows=2)
#         #print(df.columns)
#         #print(df.index(0))
#         #print(df.loc[:,'NAME'])
#         #print(df.iloc[:,[0,1]])
#         # for index, row in df.iterrows():
#             #print(row['NAME'])
#             # result1 = [b[2], b[3],str(row['NAME']),str(row['INCPACKS'])]
#             # print(result1)
#         #result1 = [b[2],b[3],df]
#         #result1 = [b[2], b[3], str(df.loc['NAME']),str(df.loc['INCPACKS']])
#         #print(result1)
#             # tmpfile1.write(','.join(result1) + '\r\n')
#     else:
#         continue
#
#tmpfile5.close()

def sort_ls(path1,path2):
    dat = read_csv('%s/tmp5.csv' %path2,names=['day',
                                                'time',
                                                'NAME',
                                                'NUMBUNAV',
                                                'DURAUNAV',
                                                'DATARECV',
                                                'SVRQRECV',
                                                'SVANRECV',
                                                'DATASENT',
                                                'SVRQSENT',
                                                'SVANSENT',
                                                'SVANFAIL',
                                                'SVAFLOOP',
                                                'SVAFUNDL',
                                                'SVAFBUSY',
                                                'SVAFOTHE',
                                                'SVANFORW',
                                                'FORWRATI',
                                                'RCVSRDIS',
                                                'SNTSRDIS',
                                                'RCVSADIS',
                                                'SNTSADIS',
                                                'SVRQDISC',
                                                'SVANDISC'])
    dat = dat.sort_values(by=["day", "time"])
    dat = dat.reset_index(drop=True)
    dat.to_csv('%s/result-ls.csv' %path1)

sort_ls(base_dir,base_dir)
