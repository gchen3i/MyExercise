#!/usr/bin/python

######################## Change History #####################################################
## v1.0: 20150317 initialized by YangCheng (M3UA not covered)
## latest updated in 20161121
#############################################################################################

import re
import os
import sys
import string
import time

lk_rawfile = '/tmp/t3_tmp0'
tmpf1 = '/tmp/t3_tmp1'
tmpf2 = '/tmp/t3_tmp2'
tmpf3 = '/tmp/t3_tmp3'
rsltdir = '/var/measfile/traffic/'
n7measdir = '/var/log/report/MeasReport/'
m3measdir = '/var/measfile/StatFiles/'
t3mode = ''
alarm_threshold = {'2m':0.4,'64k':0.4,'m2pa':1.2,'pcr':0.4,'m3ua':1.2}

def collectlinkdata():
    print "LINK DATA CELLECTING, PLEASE WAIT ... ... ..."
    os.system("/usr/local/sbin/S12MPTMON.pl ORJ 241:LKID=ALL,DETAIL=1. > %s"%lk_rawfile)
    f_0 = open(lk_rawfile,'r')
    f0 = f_0.readlines()
    got241 = 0
    for i in range(0,len(f0)):
        if f0[i].find('LAST REPORT') != -1:
            got241 = 1
            break
    if got241 == 0:
        print "LINK DATA COLLECTING FAILED, PLEASE CHECK MPTMON ENVIORMENT."
        sys.exit()
    else:
        print "LINK DATA COLLECTED."
    f_0.close()

def managelinkinfo():
    f_0 = open(lk_rawfile,'r')
    f_1 = open(tmpf1,'w')
    f0 = f_0.readlines()
    sgname = ''
    str_a = ''
    str_b = ''
    str_c = ''
    str_d = ''
    for i in range(0,len(f0)):
        f_line = f0[i].strip()
        if f_line.find('JOB SUBMITTED') != -1:
            nlist = f0[i+5].strip().split()
            if len(nlist) > 0:
                sgname = nlist[0]
        if f_line == ('LKSET            DEST        LOGNET           RTESID           OPCIND'):
            for j in range(i+2,len(f0)):
                f_line = f0[j].strip()
                if len(f_line) < 65:
                    break
                # lkset + dest + lognet
                str_a = str_a + f_line[0:16].strip()+","+f_line[17:28].strip()+","+f_line[29:45].strip()+"\n"
        if f_line == ('LKSET            SLC LKSTYPE  LKPARSET         LKTYPE    LKID'):
            for j in range(i+2,len(f0)):
                f_line = f0[j].strip()
                if len(f_line) == 0:
                    break
                plist = f_line.split()
                if str(plist[3]) == "LKST":
                    # lkset + slc + lkid + LKPARSET(not lktype)
                    str_b = str_b + str(plist[0])+","+str(plist[1])+","+str(plist[6])+","+str(plist[4])+"\n"
                    LKSNAME = str(plist[0])
                elif str(plist[2]) == "LKST":
                    # lkset + slc + lkid + LKPARSET(not lktype)
                    str_b = str_b + LKSNAME+","+str(plist[0])+","+str(plist[5])+","+str(plist[3])+"\n"
                else:
                    print "LINK DATA FOUND SOMETHING WRONG IN LINE %d:"%(j+1)
                    print f0[j]
                    sys.exit()
        if f_line == ('LKSET            LKID             +----CCSMEN----+  +-----DTMEN------+'):
            for j in range(i+3,len(f0)):
                f_line = f0[j][24:].strip()
                if len(f_line) == 0:
                    break
                plist = f_line.split()
                if len(plist) > 3:
                    # lkid + ccsm_lce + ccsm_pce + en
                    str_c = str_c + str(plist[0])+","+str(plist[1])+","+str(plist[2])+","+str(plist[3])+"\n"
                else:
                    print "LINK DATA FOUND SOMETHING WRONG IN LINE %d:"%(j+1)
                    print f0[j]
                    sys.exit()
    # combine these 3 parts into one line
    lksinfo = str_a.split('\n')
    lkinfo1 = str_b.split('\n')
    lkinfo2 = str_c.split('\n')
    if len(lkinfo1) != len(lkinfo2):
        print "LINK DATA FOUND SOMETHING WRONG, LOOK FOR SUPPORT."
        sys.exit()
    for i in range(0,len(lkinfo1)):
        if len(lkinfo1[i]) == 0:
            continue
        for j in range(0,len(lksinfo)):
            if len(lksinfo[j]) != 0:
                if str(lkinfo1[i].split(',')[0]) == str(lksinfo[j].split(',')[0]):
                    # lkset + slc + lkid + LKPARSET + lkid + ccsm_lce + ccsm_pce + tn + lkset + dest + lognet
                    str_d = str_d+lkinfo1[i]+","+lkinfo2[i]+","+lksinfo[j]+"\n" # note: here i didn't check if the last 2 parts are in same sequence!
                    break
    print >> f_1, ("%s"%sgname)
    print >> f_1, ("%s"%str_d)
    f_0.close()
    f_1.close()

def decoden7meas(measflist):
    global t3mode
    f_3 = open(measflist,'r')
    f_2 = open(tmpf2,'w')
    for f3line in f_3.readlines():
        gott3 = 0
        t3time = ''
        str_a = ''
        f3list = f3line.strip().split()
        measfile = f3list[-1]
        f_0 = open("%s%s"%(n7measdir,measfile),'r')
        f0 = f_0.readlines()
        for i in range(0,len(f0)):
            f_line = f0[i].strip()
            if f_line.find('RESULTS FOR TABLE 3') != -1:
                gott3 = 1
                if f0[i+2].strip() == 'LINK IDENTITY FORMAT = LCE & TN':
                    t3mode = 'LCE'
                elif f0[i+2].strip() == 'LINK IDENTITY FORMAT = PCE & TN':
                    t3mode = 'PCE'
                else:
                    print "GETTING LKID FORMAT(LCE/PCE) FAILED IN %s."%measfile
                if f0[i-4].strip()[0:4] == 'DATE' and f0[i-3].strip()[0:6] == 'OUTPUT' and f0[i-2].strip()[0:6] == 'RECORD':
                    if t3time != f0[i-4].strip()+','+ f0[i-3].strip()+','+ f0[i-2].strip():
                        t3time = f0[i-4].strip()+','+ f0[i-3].strip()+','+ f0[i-2].strip()
                        t3start = (int(f0[i-3].strip()[16:18])*60+int(f0[i-3].strip()[19:21]))*60
                        t3stop = (int(f0[i-3].strip()[24:26])*60+int(f0[i-3].strip()[27:29]))*60
                        t3period = str(t3stop-t3start)
                        # date + output + record + period of this report in seconds + pce/lce
                        str_a = str_a + t3time + ','+t3period+','+t3mode+'\n'
                for j in range(i+4,len(f0)):
                    f_line = f0[j].strip()
                    if not len(f_line) > 0:
                        break
                    if f_line[0:4] == ": H'":
                        plist = f_line.split()
                        plist1 = f0[j+1].strip().split()
                        if len(plist) > 9 and len(plist1) > 5 :
                            # pce/lce + tn + t31 + t33 + t34 + t35
                            str_a = str_a + str(plist[1])+","+str(plist[3])+","+str(plist[5])+","+str(plist[9])+","+str(plist1[1])+","+str(plist1[5])+"\n"
        if gott3 == 1:
            print >> f_2, ("%s"%str_a)
        else:
            print "TABLE 3 DOES NOT FOUND IN %s, PLEASE CHECK."%measfile
        f_0.close()
    f_3.close()
    f_2.close()



def buildtable(plkset,resultfile):
    f_1 = open(tmpf1,'r')
    f_2 = open(tmpf2,'r')
    if not os.path.exists(rsltdir):
        os.makedirs(rsltdir)
    f_3 = open(rsltdir+resultfile,'w')
    f1 = f_1.readlines()
    f2 = f_2.readlines()
    sgname = f1[0].strip()
    print >> f_3, ("%s"%sgname)
    Pointer_Period = []
    Indicator_H = ''
    t3period = 0
    t3start = t3stop = t3date = ''
    lk_counter = 0
    for j in range(0,len(f2)):
        if f2[j][0:4] != 'DATE' and j < len(f2)-1:
            continue
        f2list = f2[j].strip().split(',')
        if Indicator_H == '': # the first 'date', initiate the viarables:
            Pointer_Period = Pointer_Period + [j]
            t3date = str(f2list[0])
            t3period = int(f2list[3])
            t3start = str(f2list[1])[16:21]
            t3stop = str(f2list[1])[24:29]
            Indicator_H = str(f2list[1])[0:19]
            continue
        if len(f2list) > 4:
            if str(f2list[1])[0:19] == Indicator_H and str(f2list[4]) == t3mode:
                t3period = t3period + int(f2list[3])   # sum up the duration of this circle for every hour
                t3stop = str(f2list[1])[24:29]         # record stop time of this circle
                Pointer_Period = Pointer_Period + [j]  # record time pointers for every hour
                continue
        if (f2[j][0:4] == 'DATE' and str(f2list[1])[0:19] != Indicator_H) or j == len(f2)-1:
            # print a periodic report when meeting a new period, or the end of file.
            print >> f_3, ("%s\tOUTPUT PERIOD : %s - %s\tPERIOD : %d SEC"%(t3date,t3start,t3stop,t3period))
            print >> f_3,("+----------------+------+---+----------------+--------+----+----------+----------+--------+----------+----------+--------+--------+")
            print >> f_3,("|LKSET           |LOGNET|SLC|LINK            | %s& EN|TYPE|  TX BYTEs|   TX MSUs|  TXLOAD|  RX BYTEs|   RX MSUs|  RXLOAD|   TOTAL|"%t3mode)
            print >> f_3,("+----------------+------+---+----------------+--------+----+----------+----------+--------+----------+----------+--------+--------+")
            Pointer_Period = Pointer_Period + [j]
            lks_last = ''
            t3txtol = t3rxtol = 0
            t3tx_arr = t3rx_arr = []
            tx_imbalance = rx_imbalance=' '
            txtol_sum = rxtol_sum = 0.0
            # print lk info line by line
            for i in range(0,len(f1)):
                f1list = f1[i].strip().split(',')
                if len(f1list) < 11:
                    continue
                if plkset != 'All' and str(f1list[0]) != plkset:
                    continue
                if str(f1list[3]) == 'NCCM_2M' or str(f1list[3]) == 'NCCM2M': #update 20150928 for 2m link name NCCM2M
                    lktype = '2m'
                elif str(f1list[3]) == 'NCCM' or str(f1list[3]) == 'NCCMGR64': #update 20151030 for 64k link name NCCMGR64
                    lktype = '64k'
                elif str(f1list[3]) == 'PCR': #update 20161121 for link name PCR
                    lktype = 'pcr'
                elif str(f1list[3]) == 'M3UAVLK': #lktype = 'm3ua'
                    continue    #update 20160120 link-traversing stop at 1st m3ua link, modify 'break' to 'continue'
                elif str(f1list[3]) == 'M2PA':
                    lktype = 'm2pa'
                else:
                    lktype = str(f1list[3])
                t31 = t33 = t34 = t35 = 0
                t3txload = t3rxload = 0.0
                t3txalarm = t3rxalarm = ' '
                lk_counter +=1
                if t3mode == 'PCE':
                    ccsm = str(f1list[6])
                elif t3mode == 'LCE':
                    ccsm = str(f1list[5])
                else:
                    print "LKID FORMAT(LCE/PCE) NOT DEFINED! PLEASE CHECK MEAS FILES"
                    return 0
                # look for this LK's corresponding t3 counter in meas report file
                for k in range(0,len(Pointer_Period)-1):
                    for l in range(Pointer_Period[k],Pointer_Period[k+1]):
                        f2list2 = f2[l].strip().split(',')
                        if len(f2list2) > 5:
                            if ccsm == str(f2list2[0]) and str(f1list[7]) == str(f2list2[1]):
                                t31 = t31+int(f2list2[2])
                                t33 = t33+int(f2list2[3])
                                t34 = t34+int(f2list2[4])
                                t35 = t35+int(f2list2[5])
                                break
                if lktype == '2m':
                    t3txload = (t31+t33*9)/8000.0/31/t3period # tx_erl = (t31+t33*9)*8/64k/31/period
                    t3rxload = (t34+t35*9)/8000.0/31/t3period # rx_erl = (t34+t35*9)*8/64k/31/period
                elif lktype == 'm2pa':
                    t3txload = (t31+t33*16)/8000.0/31/t3period # tx_erl = (t31+t33*16)*8/64k/31/period header_len: sctp 28(ignore?), m2pa 16
                    t3rxload = (t34+t35*16)/8000.0/31/t3period # rx_erl = (t34+t35*16)*8/64k/31/period header_len: sctp 28(ignore?), m2pa 16
                else: #lktype=64k or pcr
                    t3txload = (t31+t33*6)/8000.0/t3period # tx_erl = (t31+t33*6)*8/64k/period
                    t3rxload = (t34+t35*6)/8000.0/t3period # rx_erl = (t34+t35*6)*8/64k/period
                # update 20160706: tx/rx mis-exchanged, correct it
                if alarm_threshold.has_key(lktype): #update 20161121: to avoid err with unpredictable lktype
                    if t3txload >= alarm_threshold[lktype]:
                        t3txalarm = '*'
                    if t3rxload >= alarm_threshold[lktype]:
                        t3rxalarm = '*'
                if str(f1list[0]) != lks_last or i == len(f1)-1:
                    if lks_last != '':
                        for lk in t3tx_arr:
                            if lk > t3txtol*1.5/len(t3tx_arr) or lk < t3txtol*0.75/len(t3tx_arr):
                                tx_imbalance = '@'
                        for lk in t3rx_arr:
                            if lk > t3rxtol*1.5/len(t3rx_arr) or lk < t3rxtol*0.75/len(t3rx_arr):
                                rx_imbalance = '@'
                        print >> f_3,("+----------------+------+---+----------------+--------+----+----------+----------+--------+----------+----------+--------+--------+")
                        print >> f_3,("|%-16s|                                                              %s|%8.4f|                    %s|%8.4f|%8.4f|"%(lks_last,
                        tx_imbalance,t3txtol,rx_imbalance,t3rxtol,t3txtol+t3rxtol))
                        print >> f_3,("+----------------+------+---+----------------+--------+----+----------+----------+--------+----------+----------+--------+--------+")
                    t3txtol = t3txload
                    t3rxtol = t3rxload
                    tx_imbalance = rx_imbalance=' '
                    t3tx_arr = [t3txload]
                    t3rx_arr = [t3rxload]
                    lks_last = str(f1list[0])
                    lksname = str(f1list[0])
                else:
                    t3txtol = t3txtol+ t3txload
                    t3rxtol = t3rxtol+ t3rxload
                    t3tx_arr = t3tx_arr + [t3txload]
                    t3rx_arr = t3rx_arr + [t3rxload]
                    # lksname = ''    # commenting it to show lkset name for all links
                txtol_sum = txtol_sum + t3txload
                rxtol_sum = rxtol_sum + t3rxload
                print >> f_3,("|%-16s|%6s|%3s|%-16s|%4s&%3s|%4s|%10d|%10d|%s%7.4f|%10d|%10d|%s%7.4f|%8.4f|"%(lksname,str(f1list[10]),str(f1list[1]),str(f1list[2]),
                ccsm[2:6],str(f1list[7]),lktype,t31,t33,t3txalarm,t3txload,t34,t35,t3rxalarm,t3rxload,t3txload+t3rxload))
				# update 20160706: tx/rx mis-exchanged, correct it
            Pointer_Period = [j]
            if lk_counter !=0:
                for lk in t3tx_arr:
                    if lk > t3txtol*1.5/len(t3tx_arr) or lk < t3txtol*0.75/len(t3tx_arr):
                        tx_imbalance = '@'
                for lk in t3rx_arr:
                    if lk > t3rxtol*1.5/len(t3rx_arr) or lk < t3rxtol*0.75/len(t3rx_arr):
                        rx_imbalance = '@'
                print >> f_3,("+----------------+------+---+----------------+--------+----+----------+----------+--------+----------+----------+--------+--------+")
                print >> f_3,("|%-16s|                                                              %s|%8.4f|                    %s|%8.4f|%8.4f|"%(lks_last,
                tx_imbalance,t3txtol,rx_imbalance,t3rxtol,t3txtol+t3rxtol))
                print >> f_3,("+----------------+------+---+----------------+--------+----+----------+----------+--------+----------+----------+--------+--------+")
                if plkset =='All':
                    print >> f_3,("|%-16s|                                                               |%8.4f|                     |%8.4f|%8.4f|"%(sgname,
                    txtol_sum,rxtol_sum,txtol_sum+rxtol_sum))
                    print >> f_3,("+=================================================================================================================================+")
            if j != len(f2)-1:   # update 20160113: update t3period too early, so move this to the end of this circle("for j in (f2)").
                # when new period meet, initiate these 4 variables
                t3period = int(f2list[3])
                t3start = str(f2list[1])[16:21]
                t3stop = str(f2list[1])[24:29] #update 20161121: stop time incorrectly displayed for a incomplete hour
                Indicator_H = str(f2list[1])[0:19]
    f_1.close()
    f_2.close()
    f_3.close()
    if lk_counter !=0:
        print "RESULT HAS BEEN OUTPUT TO %s%s"%(rsltdir,resultfile)
        print "Hint: you can check sign '*' for overload links, or sign '@' for imbalance in lkset."
        return 1
    else:
        print "NO LKSET DATA MATCH WITH YOUR INPUT, PLEASE CHECK."
        return 0

def f_help():
    print "\n\n# Examples:"
    print "# c                          : Collect link data(com241), if you had not collect recently, do it firstly"
    print "# a,64k,0.4                  : Alarm threshold setting, default values are 0.4erl for 64k/2m/pcr, 1.2erl for m2pa"
    print "# s,2015-03-21-2             : Show all meas_files you can decode with given time scope"
    print "# d,2015-03-21(,LKSETID)     : Decode meas files for a whole day, LKSET can be specified"
    print "# d,2015-03-21-21(,LKSETID)  : Decode meas files for a hour"
    print "# d,2015-03-21-2115(,LKSETID): Decode a certain meas file"
    print "# h                          : Help"
    print "# q                          : Quit"

f_help()
while 1:
    command = raw_input("\nEnter your command ('h' for Help, 'q' for Quit)--> ")
    if len(command) == 0:
        continue
    clist = command.split(',')
    if clist[0] == 'q':
        sys.exit()
    elif clist[0] == 'h':
        f_help()
    elif clist[0] == 'c':
        collectlinkdata()
        #managelinkinfo() #update 20161121, to ease debug
    elif clist[0] == 'a':
        if len(clist) < 3:
            print "Parameters' missing, please check ... "
            continue
        try:
            float(clist[2])
        except ValueError:
            print "Alarm threshold value must be a number(int or float)."
            continue
        if type(eval(clist[2])==type(1.0)) or type(eval(clist[2])==type(1)):
            if clist[1] == '2m':
                alarm_threshold['2m']=float(clist[2])
            elif clist[1] == '64k':
                alarm_threshold['64k']=float(clist[2])
            elif clist[1] == 'm2pa':
                alarm_threshold['m2pa']=float(clist[2])
            elif clist[1] == 'pcr':
                alarm_threshold['pcr']=float(clist[2])
#            elif clist[1] == 'm3ua':
#                alarm_threshold['m3ua']=float(clist[2])
            else:
                print "Only 4 link types can be set: 2m/64k/m2pa/pcr, please check your input."
                continue
            print "Alarm threshold set successfully."
    elif clist[0] == 's' or clist[0] == 'd':
        timescope = ''
        match = []
        if len(clist) > 1:
            timescope = clist[1]
        mlist = os.popen("ls -lF %s"%(n7measdir)).readlines()
        for i in range(0,len(mlist)):
            if mlist[i].find(timescope) != -1:
                match = match + [i]
        f_3 = open(tmpf3,'w')
        if len(match) == 1:# if one certain file is requested, decode this file;
            print >> f_3,("%s"%(mlist[match[0]].strip()))
        elif len(match) > 96:
            print "Too many files, please narrow your time scope to ONE DAY at most."
            continue
        elif len(match) == 0:
            print "No meas file match your input, please check time scope, or maybe you're on standby OAM?"
            continue
        else: #!!BUT: if not, here we should consider that meas output has a delay for one period
            for j in match:
                if j<len(mlist)-1:
                    print >> f_3,("%s"%(mlist[j+1].strip()))
        f_3.close()
        if clist[0] == 's':
            print "Here is measure files match your input:"
            os.system("more %s"%tmpf3)
        else:
            if not os.path.exists(lk_rawfile):  #update 20161121: to ease debug
                print "LINK DATA HAS NOT BEEN COLLECTED YET, PLEASE TRY 'c' FIRSTLY"
                continue
            managelinkinfo()  #update 20161121: to ease debug
            print "Please wait, this might take a while ... ... ...\n"
            decoden7meas(tmpf3)
            if len(clist) > 2:
                lkset=clist[2]
            else:
                lkset='All'
            if buildtable(lkset,"T3_Result_%s_%s"%(clist[1],lkset)):
                rsp = raw_input("Press ENTER to show the result file, 'n' to skip: (y/n|y)")
                if rsp != 'n':
                    os.system("more %sT3_Result_%s_%s"%(rsltdir,clist[1],lkset))
    else:
        print "Please check your input ..."

