import os
from pandas import read_csv
import matplotlib.pyplot as plt

base_dir = '/Users/gangch/Documents/temp/measfile'
exchange = 'NJDRA03BAL'
full_path = base_dir + r'/' + exchange

def format_ls(path1,path2):
    file_total = os.listdir(path2)
    tmpfile5 = open('%s/tmp5.csv' %path2,mode='w')
    print('1/2:Begin to collect DIAMLINKSET data,pls wait...')

    for line in file_total:
        # 更改文件名中的-_
        a = line.replace('-', '.').replace('_', '.')
        b = a.split('.')
        if b[1] == 'DIAMLINKSET':
            df = read_csv('%s/%s' % (path2, line), skiprows=2)
            for index, row in df.iterrows():
                result = [b[2],b[3],str(row['NAME']),
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
                tmpfile5.write(','.join(result) + '\r\n')
    tmpfile5.close()

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
    print('2/2:Begin to resort,pls wait...')
    dat = dat.sort_values(by=["day", "time"])
    dat = dat.reset_index(drop=True)
    dat.to_csv('%s/result-ls.csv' %path1)

def format_global(path1,path2):
    file_total = os.listdir(path2)
    tmpfile8 = open('%s/tmp8.csv' %path2,mode='w')
    print('1/2:Begin to collect DIAMGLOBAL data,pls wait...')

    for line in file_total:
        # 更改文件名中的-_
        a = line.replace('-', '.').replace('_', '.')
        b = a.split('.')
        if b[1] == 'DIAMGLOBAL':
            df = read_csv('%s/%s' % (path2, line), skiprows=2)
            result = [b[2], b[3], str(df.at[0, 'MSGRCVPS']),
                                   str(df.at[0, 'MSGSNTPS']),
                                   str(df.at[0, 'UTLIRATI']),
                                   str(df.at[0, 'LPDETECT']),
                                   str(df.at[0, 'SVRQRECV']),
                                   str(df.at[0, 'SVANRECV']),
                                   str(df.at[0, 'SVRQSENT']),
                                   str(df.at[0, 'SVANSENT']),
                                   str(df.at[0, 'SVANFAIL']),
                                   str(df.at[0, 'SVRQRERT']),
                                   str(df.at[0, 'FORWRATI']),
                                   str(df.at[0, 'AVRGLOAD']),
                                   str(df.at[0, 'PEAKLOAD']),
                                   str(df.at[0, 'NUMMPSOL']),
                                   str(df.at[0, 'MAXMPSOL'])]
            tmpfile8.write(','.join(result) + '\r\n')

    tmpfile8.close()

    dat = read_csv('%s/tmp8.csv' % path2, names=['day',
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
    # 按日期和时间排序
    print('2/2:Begin to resort,pls wait...')
    dat = dat.sort_values(by=["day", "time"])
    # 重新排列序号
    dat = dat.reset_index(drop=True)
    dat.to_csv('%s/result-global.csv' % path1, sep=',')



def main_menu():
    print('--------------------------------------------------------------------------')
    print('|             DRA measurement format  program v0.1                       |')
    print('|                          Main  Menu                                    |')
    print('--------------------------------------------------------------------------')
    print('|        1.  DIAMIP                      2.    DIAMCPU                   |')
    print('|        3.  DIAMSCTP                    4.    DIAMLINK                  |')
    print('|        5.  DIAMLINKSET                 6.    DIAMROUTESET              |')
    print('|        7.  DIAMBOARD                   8.    DIAMGLOBAL                |')
    print('|        9.  DIAMSESSIONBIND            10.    DIAMAPN                   |')
    print('|       11.  DIAMS6A                    12.    DIAMGX                    |')
    print('|       13.  DIAMRX                     14.    DIAMCX                    |')
    print('|       15.  DIAMSH                     16.    DIAMZH                    |')
    print('|       17.  DIAMSLH                    18.    DIAMSLG                   |')
    print('|        a.  all                                                         |')
    print('|        q.  quit                                                        |')
    print('--------------------------------------------------------------------------')

while True:
    #os.system('clear')
    main_menu()
    option = input("   please input your select:")
    if str(option) == 'q':
        select = input("Please input yes to confirm quit:")
        if str(select) == 'yes':
            os.system('clear')
            print("Thanks for you used, bye!")
            print("author:chengang")
            print('mail:gang.f.chen@nokia-sbell.com')
            break
        else:
            print("You don't confirm to quit,continu")

    elif str(option) == '1':
        print('1')

    elif str(option) == '2':
        print('2')

    elif str(option) == '3':
        print('3')

    elif str(option) == '4':
        print('4')

    elif str(option) == '5':
        print('Your select is DIAMLINKSET measurement,pls wait...')
        print('The data is very big and so many time to excuting!')
        format_ls(base_dir, full_path)
        print('Successful excuting...')

    elif str(option) == '6':
        print('6')

    elif str(option) == '7':
        print('7')

    elif str(option) == '8':
        print('Your select is DIAMGLOBAL measurement,pls wait...')
        format_global(base_dir,full_path)
        print('Successful excuting...')

    elif str(option) == '9':
        print('9')

    elif str(option) == '10':
        print('10')

    elif str(option) == '11':
        print('11')

    elif str(option) == '12':
        print('12')

    elif str(option) == '13':
        print('13')

    elif str(option) == '14':
        print('14')

    elif str(option) == '15':
        print('15')

    elif str(option) == '16':
        print('16')

    elif str(option) == '17':
        print('17')

    elif str(option) == '18':
        print('18')

    elif str(option) == 'a':
        print('all')

    else:
        print('Warning!!!')
        print('Your select is invalid,please check...')