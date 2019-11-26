import os
import pandas as pd
from pandas import read_csv
from pandas import read_excel
base_dir = '/Users/gangch/Documents/temp/measfile'
exchange = 'NJDRA03BAL'
full_path = base_dir + r'/' + exchange

dat = read_excel('%s/global-10.xlsx' % base_dir, names=['day',
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
                                                 'MAXMPSOL'])
#转换day和time为字符串
dat['day'] = dat['day'].astype('str')
dat['time'] = dat['time'].astype('str')
dat['UTLIRATI'].max()

