



import RPi.GPIO as GPIO   
from time import sleep as delay

GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)
   
GPIO.output(22,True)
   

while 1:   
   try:
      print("stuff")
      delay(1)
      GPIO.output(22,False)
      delay(1)
      GPIO.output(22,True)
      
   except KeyboardInterrupt:
        GPIO.cleanup()
        break
