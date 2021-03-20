import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
from time import sleep  # Importing sleep from time library
led_pin = 21            # Initializing the GPIO pin 21 for vibration sensor
GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering
GPIO.setup(led_pin, GPIO.OUT)   # setting pin 21 as output pin
pwm = GPIO.PWM(led_pin, 100)    # PWM object is created
pwm.start(0)                    # Started PWM at 0% duty cycle
try:
    test_text = input ("Enter a number: ")
    test_text = int(test_text)
    while 1:                    # Loop will run forever
    
            pwm.ChangeDutyCycle(test_text) # Change duty cycle
            sleep(0.01)         # Delay of 10mS
            

# If keyboard Interrupt (CTRL-C) is pressed
except KeyboardInterrupt:
    pass        # Go to next line
pwm.stop()      # Stop the PWM
GPIO.cleanup()  # Make all the output pins LOW
