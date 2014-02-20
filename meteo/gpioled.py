#!/usr/bin/python2.7
from time import sleep
class leds():
    def led_on(self,led):
	f=open("/sys/class/gpio/gpio"+str(led)+"/value","w")
	f.write("1")
	f.close()

    def led_off(self,led):
	f=open("/sys/class/gpio/gpio"+str(led)+"/value","w")
	f.write("0")
	f.close()

    def blink(self,led,ontime,offtime):
	self.led_on(led)
	sleep(ontime)
	self.led_off(led)
	sleep(offtime)

    def blink3(self,led):
	i=0
	while (i < 3):
	    self.blink(led,0.02,0.02)
	    i = i + 1

    def blink5(self,led):
	i=0
	while (i < 5):
	    self.blink(led,0.03,0.03)
	    i = i + 1