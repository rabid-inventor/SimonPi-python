


import threading
import RPi.GPIO as GPIO   
from time import sleep as delay

outputs = [22,23,24,25]
light_speed = 0.1
GPIO.setmode(GPIO.BCM)

#Tunes = [

def printFunction(channel):
   print("Button 1 pressed!")
   print("Note how the bouncetime affects the button press")

def Beep():
   audio=file('/dev/audio', 'wb')
   count=0
   while count<250:
      beep=chr(63)+chr(63)+chr(63)+chr(63)
      audio.write(beep)
      beep=chr(0)+chr(0)+chr(0)+chr(0)
      audio.write(beep)
      count=count+1
   audio.close()

Beep()

for i in range(len(outputs)):
   #GPIO.setup(outputs[i],GPIO.OUT)
   GPIO.setup(outputs[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)
   GPIO.add_event_detect(outputs[i], GPIO.FALLING, callback=printFunction, bouncetime=300)   
#GPIO.output(22,True)
   
def lights(speed):
   while 1:
      for i in range(len(outputs)):
         Beep()
         GPIO.remove_event_detect(outputs[i])
         GPIO.setup(outputs[i], GPIO.OUT)
         GPIO.output(outputs[i], True)
         delay(speed)
         GPIO.setup(outputs[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)
         GPIO.add_event_detect(outputs[i], GPIO.FALLING, callback=printFunction, bouncetime=300)
         delay(speed)   


#GPIO.add_event_detect(23, GPIO.FALLING, callback=printFunction, bouncetime=300)
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
        GPIO.cleanup()
        break
