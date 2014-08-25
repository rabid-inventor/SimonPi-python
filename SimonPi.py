#import  os
#import RPi.GPIO as GPIO


try:
   
   
   GPIO.setmode(BCM)
   GPIO.setup(22, GPIO.OUT)
   
   GPIO.output(22,HIGH)
   
   
   
   
 except (KeyboardInterrupt, SystemExit):
    GPIO.cleanup()
    print '\nkeyboardinterrupt found!'
    print '\n...Program Stopped Manually!'
    raise
