#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os.path
import datetime
from time import sleep 
import serial
from db.sql import sql
from parser.parser import parser
import logging
logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'hw3logger.log')

class hwlog():
    def __init__(self):
        self.serial_connect()
    
    def serial_connect(self):
        if self.check_port() == False:
            pass
        else:
            self.sc = serial.Serial(port=self.check_port(),baudrate=9600, timeout=3, writeTimeout=3)
    
    def serial_getdata(self):
        self.sc.write("g")
        data = self.sc.readall()
        return data



    def check_port(self):
	if os.path.exists("/dev/ttyACM0"):
	    return '/dev/ttyACM0'
	if os.path.exists("/dev/ttyACM1"):
	    return '/dev/ttyACM1'
	if os.path.exists("/dev/ttyACM2"):
	    return '/dev/ttyACM2'
	else:
	    return False   

log=hwlog()
#try:
log.serial_connect()
s=sql()
p=parser()

try:
    while True:
        if log.check_port() == False:
            logging.error( u'Устройство не подключено' )
            sleep(60)
        else:   
            s.insert(p.data_parser(log.serial_getdata()))
            sleep(60)
except Exception,e:
    print str(e)







