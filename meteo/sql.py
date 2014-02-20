#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys
import datetime


con = lite.connect('meteo.db')

class sql():
	def __init__(self):
		pass

	def insert(self,parced_data):
		d = parced_data
		#print d
		with con:
			# id day mon year hour min sec sid temp humi pres lowbat
			cur = con.cursor()
			values = "'"+d['day']+"','"+d['mon']+"','"+d['year']+"','"+d['hour']+"','"+d['min']+"','"+d['sec']+"','"+d['sid']+"','"+d['temp']+"','"+d['humi']+"','"+d['pres']+"','"+d['lowbat']+"'"
			#print values
			cur.execute("insert into meteo (day, mon,year,hour,min,sec,sid,temp,humi,pres,lowbat) values ("+values+");")

	def get_all(self):

		with con:
			cur = con.cursor()
			cur.execute('''SELECT id, day, mon,year,hour,min,sec,sid,temp,humi,pres,lowbat FROM meteo;''')
			return cur.fetchall()

	def get_last(self,sid):
		cur = con.cursor()
		cur.execute('SELECT id, day, mon,year,hour,min,sec,sid,temp,humi,pres,lowbat FROM meteo WHERE sid="'+sid+'" order by rowid desc limit 1  ;')
		return cur.fetchall()

	def get_hourly(self,sid):
		ftime = datetime.datetime.now().time()
		chour = ftime.strftime("%H")
		cmin = ftime.strftime("%M")
		ihour = int(chour) - 1
		phour = str(ihour)
		ptime = phour + ":" + cmin
		print chour + ":" + cmin + " - " + ptime

