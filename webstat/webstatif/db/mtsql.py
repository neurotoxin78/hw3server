#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys
import datetime


#con = lite.connect('/home/neuro/hw3-logger/hwdata.db')

con = lite.connect('/var/hwdata/hwdata.db')

class sql():
	def __init__(self):
		pass
        def connect(self):
            self.con = lite.connect('/var/hwdata/hwdata.db')
            return self.con

	def insert(self,parced_data):
		d = parced_data
		#print d
                self.connect()
		with self.con:
			# id day mon year hour min sec sid temp humi pres lowbat
			cur = self.con.cursor()
			values = "'"+d['day']+"','"+d['mon']+"','"+d['year']+"','"+d['hour']+"','"+d['min']+"','"+d['sec']+"','"+d['humidity']+"','"+d['btemp']+"','"+d['htemp']+"','"+d['pressure']+"'"
			#print values
			cur.execute("insert into weather (day, mon,year,hour,min,sec,humidity,btemp,htemp,pressure) values ("+values+");")

	def get_all(self):
                self.connect()
		with self.con:
			cur = self.con.cursor()
			cur.execute('''SELECT id, day, mon,year,hour,min,sec,humidity,btemp,htemp,pressure FROM weather;''')
			return cur.fetchall()

	def get_last(self):
                self.connect()
		cur = self.con.cursor()
		cur.execute('SELECT id, day, mon,year,hour,min,sec,humidity,btemp,htemp,pressure FROM weather order by rowid desc limit 1  ;')
		return cur.fetchall()

        def get_last_3h(self):
                self.connect()
                cur = self.con.cursor()
                cur.execute('select * from weather order by rowid desc limit 180;')
                return cur.fetchall()
        def get_hourly(self):
                self.connect()
		ftime = datetime.datetime.now().time()
                fdate = datetime.datetime.now().date()
		cday = fdate.strftime("%d")
                chour = ftime.strftime("%H")
                cur = self.con.cursor()
                cur.execute('select * from weather where day="'+cday+'" and hour="'+chour+'";')
                return cur.fetchall()
        
        def get_dayly(self):
                self.connect()
                fdate = datetime.datetime.now().date()
                day = fdate.strftime("%d")
                cur = self.con.cursor()
                cur.execute('select * from weather where day="'+day+'";')
                return cur.fetchall()







