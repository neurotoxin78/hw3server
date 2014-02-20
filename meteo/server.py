#!/usr/bin/python2.7
import datetime

class server():
	def data_parser(self,data):
		pdata = {}
		packet = data.split(":")
		date = datetime.datetime.now().date()
		time = datetime.datetime.now().time()
		#help(date)
		pdata['day'] = str(date.day)
		pdata['mon'] = str(date.month)
		pdata['year'] = str(date.year)
		pdata['hour'] = time.strftime("%H")
		pdata['min'] = time.strftime("%M")
		pdata['sec'] = time.strftime("%S")
		pdata['sid'] = packet[1]
		pdata['temp'] = packet[2]
		pdata['humi'] = packet[3]
		pdata['pres'] = packet[4]
		pdata['lowbat'] = packet[5]
		return pdata
