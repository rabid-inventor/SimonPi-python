


#Musical Note Notes
#A4	     440.00
#A#4/Bb4   466.16	
#B4	     493.88	
#C5	     523.25	
#C#5/Db5   554.37
#D5	     587.33
#D#5/Eb5   622.25
#E5	     659.25
#F5	     698.46
#F#5/Gb5   739.99
#G5	     783.99
#G#5/Ab5   830.61
import os
from socket import socket, AF_INET, SOCK_STREAM 
import threading
import RPi.GPIO as GPIO   
from time import sleep as delay


sck = socket(AF_INET, SOCK_STREAM)

gameActive = False


print(os.system("pd -nogui tonegenerator.pd &"))
print('now you wait ...........')
delay(1.5)

sck.connect(("127.0.0.1",3000))

#sck.send("power 1;")
#os.system('echo "power 1;" | pdsend 3000')
#delay(1)
#os.system('echo "power 0;" | pdsend 3000') 
#os.system('sudo killall pd') 

outputs = [22,23,24,25]
light_speed = 0.1
GPIO.setmode(GPIO.BCM)


Notes = {'a':440 , 'aSH':466.16 , 'b':493.88}

print(Notes.get('aSH'))

Tune1 = [('a',500),('aSH',500)]

def playNote((f,d)):
   sck.send("tone  " + str(f) + ";")
   sck.send("power 1;")
   delay(d)
   sck.send("power 0;")



#playNote((440,1))
#playNote((330,1))

def printFunction(channel):
   print("Button 1 pressed!")
   print("Note how the bouncetime affects the button press")



def button1(channel):
   print channel
   print("button 1 pressed")
   playNote((440,0.4))
   return

def button2(channel):
   print("button 2 pressed")
   playNote((330,0.4))
   return


def button3(channel): 
   gameActive = True
   fail()


def fail():
   playNote((220,3))
   gameActive = True
   #lights(0.2)



for i in range(len(outputs)):
   #GPIO.setup(outputs[i],GPIO.OUT)
   GPIO.setup(outputs[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)
   
#GPIO.output(22,True)
   
def attachInt(button,IOport):
   if ( button == 0):
      GPIO.add_event_detect(IOport, GPIO.FALLING, callback=button1, bouncetime=300)
   elif( button == 1):
      GPIO.add_event_detect(IOport, GPIO.FALLING, callback=button2, bouncetime=300)
   elif( button == 2):
      GPIO.add_event_detect(IOport, GPIO.FALLING, callback=button3, bouncetime=300)
   elif( button == 3):
      GPIO.add_event_detect(IOport, GPIO.FALLING, callback=button2, bouncetime=300)
   return 0



def lights(speed):
  
   while (gameActive == False):
      for i in range(len(outputs)):

         GPIO.remove_event_detect(outputs[i])
         GPIO.setup(outputs[i], GPIO.OUT)
         GPIO.output(outputs[i], True)
         delay(speed)
         GPIO.setup(outputs[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)
         attachInt(i,outputs[i]) 
         delay(speed)   

t = threading.Thread(target = lights, args = [light_speed])
t.deamon = False
t.start()


while 1:   
   try:

      print("stuff")
      
      delay(1)
      #GPIO.output(22,False)
      #GPIO.remove_event_detect(23)      
      #delay(1)
      #GPIO.output(22,True)
      #GPIO.add_event_detect(23, GPIO.FALLING, callback=printFunction, bouncetime=300)
      
   except KeyboardInterrupt:
        #t.stop()
        os.system('sudo killall pd')
        GPIO.cleanup()
        
        os.system('sudo killall pd')

        break
