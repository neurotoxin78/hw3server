#!/usr/bin/python2.7 
import SOAPpy
from db.mtsql import sql
import logging
logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'hw3logger.log')

def get_all():
    s=sql()
    return s.get_all()

def get_last():
    s=sql()
    return s.get_last()

def get_hourly():
    s=sql()
    return s.get_hourly()

def get_dayly():
    s=sql()
    return s.get_dayly()

def get_last_3h():
    s=sql()
    return s.get_last_3h()
def get_last_24h():
    s=sql()
    return s.get_last_24h()

if __name__ == "__main__":
    try:
        SOAPpy.Config.debug = 0
        server = SOAPpy.SOAPServer(("0.0.0.0", 7777))
        server.registerFunction(get_all)
        server.registerFunction(get_last)
        server.registerFunction(get_hourly)
        server.registerFunction(get_dayly)
        server.registerFunction(get_last_3h)
        server.registerFunction(get_last_24h)
        server.serve_forever()
    except KeyboardInterrupt:
        exit(0)

