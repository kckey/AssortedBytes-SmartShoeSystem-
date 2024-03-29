import RPi.GPIO as GPIO     
from time import sleep  
led_pin = 21            # Initializing the GPIO pin 21 for vibration sensor
GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering
GPIO.setup(led_pin, GPIO.OUT)   # setting pin 21 as output pin
pwm = GPIO.PWM(led_pin, 100)    # PWM object is created at 100Hz
pwm.start(0)                    # Started PWM at 0% duty cycle
try:
    test_text = input ("Enter a number between 1 and 100: ")
    test_text = int(test_text)
    while 1:                    # Loop will run forever
      if ((test_text>=1)and(test_text<=30)):
       pwm.ChangeDutyCycle(60) # Change duty cycle
       sleep(.10)
      elif ((test_text>=31)and(test_text<=60)):
       pwm.ChangeDutyCycle(90)
       sleep(.10)
      elif((test_text>=61)and (test_text<=100)):
       pwm.ChangeDutyCycle(100) # Change duty cycle
       sleep(.10)
      else:
       print('enter an accepetable value')
       pwm.ChangeDutyCycle(0) 
        
# If keyboard Interrupt (CTRL-C) is pressed
except KeyboardInterrupt:
    pass        
pwm.stop()     
GPIO.cleanup()  # Make all the output pins LOW
