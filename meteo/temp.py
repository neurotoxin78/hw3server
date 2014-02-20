#! /bin/env python2.7
def ambitemp():
    f=open("/sys/bus/w1/devices/28-000004f62e31/w1_slave","r")
    rawdata =  f.read()
    tmp=rawdata.split()
    tmpa=tmp[21]
    tmpdigit=tmpa[2:]
    cis,znam = tmpdigit[:2],tmpdigit[2:]
    temp=float(cis+"."+znam)
    deg = u'\N{DEGREE SIGN}'
    t = "%2.1f " % (temp)
    return str(t) + deg + "C"
    
