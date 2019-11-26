import os
import sys
import difflib


# def com_file():
#basedir = 'Z:/Downloads/Github/project1'
basedir = 'C:/temp'
#filename = 'NJDRA01AAL-B'
orginf1 = input('Please input the older dradata filename:')
orginf2 = input('Please input the newer dradata filename:')
f1 = open('%s/%s' % (basedir, orginf1), mode='r').readlines()
f2 = open('%s/%s' % (basedir, orginf2), mode='r').readlines()
diff = difflib.ndiff(f1, f2)

# 输出结果重定向到文件
oldstdout = None
logfile = None
try:
    logfile = open('%s/temp.log' % basedir, mode='w')
    oldstdout = sys.stdout
    sys.stdout = logfile
    sys.stdout.writelines(diff)
finally:
    if logfile:
        logfile.close()
    if oldstdout:
        sys.stdout = oldstdout

f3 = open('%s/temp.log' % basedir, mode='r').readlines()
f3_tmp1 = open('%s/addscript.log' % basedir, mode='w')
f3_tmp2 = open('%s/delscript.log' % basedir, mode='w')
for i in f3:
    if i.find('+ <') != -1:
        f3_tmp1.write(i)    {  }[]

    elif i.find('- <') != -1:
        f3_tmp2.write(i)
f3_tmp1.close
f3_tmp2.close
