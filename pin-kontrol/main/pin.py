#!/usr/bin/python

#Make sure resource is available
try:
    f= open ('/sys/class/gpio/unexport','w')
    f.write(str(gpio))
    f.close()
except IOError as e:
    lol=0

def switch(gpio,state):
    #Export pin number
    f= open ('/sys/class/gpio/export','w')
    f.write(str(gpio))
    f.close()


    #Define Pin Direction as Output for LED
    path = '/sys/class/gpio/gpio' + gpio + '/direction'
    f= open (path,'w')
    f.write('out')
    f.close()

    #Loop through LED 'ON' and 'OFF' for the number of times specified
    path = '/sys/class/gpio/gpio' + gpio + '/value'
    f= open (path,'w')
    f.write(str(gpio))
    f.close()

switch(gpio,state)

#Unexport Pin 
#f= open ('/sys/class/gpio/unexport','w')
#f.write(str(gpio))
#f.close()