#!/usr/bin/python2.7
import datetime

class parser():
	def data_parser(self,data):
		pdata = {}
		packet = data.split(" ")
		date = datetime.datetime.now().date()
		time = datetime.datetime.now().time()
		#help(date)
		pdata['day'] = str(date.day)
		pdata['mon'] = str(date.month)
		pdata['year'] = str(date.year)
		pdata['hour'] = time.strftime("%H")
		pdata['min'] = time.strftime("%M")
		pdata['sec'] = time.strftime("%S")
                try:
                    pdata['humidity'] = packet[0]
                except:
                    pdata['humidity'] = "0"
                try:    
		    pdata['btemp'] = packet[1]
                except:
                    pdata['btemp'] = "0"
                try:
		    pdata['htemp'] = packet[2]
                except:
                    pdata['htemp'] = "0"
                try:
                    pdata['pressure'] = packet[3]
                except:
                    pdata['pressure'] = "0"
		return pdata
