#!/usr/bin/python
import os

def state(gpio):
	gpio = str(gpio)
	try:
		os.system('cat /sys/class/gpio/gpio' + gpio + '/value')
	finally:
	    print "!" #to do!
	pass

state(17) #test pin
