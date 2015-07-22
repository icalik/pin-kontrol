#!/usr/bin/python
import os

def state(gpio):
	gpio = str(gpio)
	#Export pin number
	f= open ('/sys/class/gpio/export','w')
	f.write(str(gpio))
	f.close()
	state_giden(gpio)
	#Unexport Pin 
	f= open ('/sys/class/gpio/unexport','w')
	f.write(str(gpio))
	f.close()


def state_giden(gpio):
	

	try:
		k = os.system('cat /sys/class/gpio/gpio' + gpio + '/value')
		if k==0:
			print "OFF"
			pass
	finally:
	    print "!" #to do!
	pass

state(26) #test pin
