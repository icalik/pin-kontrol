
def switch(gpio,state):
    state = str(state)
    gpio = str(gpio)
    

    #Export pin number
    f= open ('/sys/class/gpio/export','w')
    f.write(str(gpio))
    f.close()

    #Define Pin Direction as Output for LED

    path = '/sys/class/gpio/gpio' + gpio + '/direction'
    f= open (path,'w')
    f.write('out')
    f.close()

    path = '/sys/class/gpio/gpio' + gpio + '/value'
    f= open (path,'w')
    f.write(state)
    f.close()

       
    #Unexport Pin 
    f= open ('/sys/class/gpio/unexport','w')
    f.write(str(gpio))
    f.close()
    pass

#switch(26,1) #Test pin


