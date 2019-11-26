import os
import sys

basedir = 'C:/temp'
orginf1 = input('Please input the config filename:')
policy1 = input('Please input the delete policy name:')
f1 = open('%s/%s' % (basedir, orginf1), mode='r').readlines()
logfile = open('%s/result.log' % basedir, mode='w')


def SapFunction(num, flag):
    if flag:
        if f1[num - 2].find('sap'):
            logfile.write(f1[num - 2])
        else:
            logfile.write(f1[num - 3])
        logfile.write(f1[num - 1])
        logfile.write('                pppoe-policy "pppoe-policy-s"' + '\n')
        logfile.write('                pppoe-user-db "ludb-s"' + '\n')
        logfile.write('            exit' + '\n')
    else:
        pass


def VplsFunction(num, flag):
    if flag:
        logfile.write(f1[num])
        logfile.write(f1[num + 1])
        logfile.write(f1[num + 2])
        logfile.write(f1[num + 3])
    else:
        pass


for i in range(0, len(f1)):
    if f1[i].find('vpls') != -1:
        VplsFunction(i, 1)

    elif f1[i].find('pppoe-policy') != -1:
        if f1[i].find('%s' % policy1) != -1:
            SapFunction(i, 0)
        else:
            SapFunction(i, 1)

    else:
        continue

logfile.close
