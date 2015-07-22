#!/usr/bin/python
import os

def state(gpio):
	gpio = str(gpio)
	#Export pin number
	f= open ('/sys/class/gpio/export','w')
	f.write(str(gpio))
	f.close()
	durum = state_giden(gpio)
	#Unexport Pin 
	f= open ('/sys/class/gpio/unexport','w')
	f.write(str(gpio))
	f.close()
	return durum


def state_giden(gpio):
	

	try:
		x = os.popen('cat /sys/class/gpio/gpio' + gpio + '/value').read(1)
		#x = subprocess.check_output(['cat /sys/class/gpio/gpio' + gpio + '/value'])
		#print type(x)
	finally:
		pass

	return x

#state(26)#Test pin