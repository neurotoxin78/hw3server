#!/usr/bin/env python2.7
import SOAPpy
import time
start_time = time.time()
from db.mtsql import sql

s = sql()

server = SOAPpy.SOAPProxy("http://127.0.0.1:7777/")
resp = server.get_last_3h()
print resp
print time.time() - start_time, "seconds"

start_time = time.time()
print s.get_last_3h()
print time.time() - start_time, "seconds"


#for item in resp:
#    print item.data





#server.hello()
