import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 

GPIO_TRIGGER = 23
GPIO_ECHO = 24                             #Associate pin 14 to Echo

print ("Posture Test in progress")

GPIO.setup(GPIO_TRIGGER,GPIO.OUT)          #Set pin as GPIO out
GPIO.setup(GPIO_ECHO,GPIO.IN)              #Set pin as GPIO in

while True:

  GPIO.output(GPIO_TRIGGER, False)         #Set TRIG as LOW
  print ("Checking Stance")                #Checking the User stance
  time.sleep(30)                           #Checking the user stance for 30 Seconds

  GPIO.output(GPIO_TRIGGER, True)          #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(GPIO_TRIGGER, False)         #Set TRIG as LOW

  while GPIO.input(GPIO_ECHO)==0:          #Check if Echo is LOW
    pulse_start = time.time()              #Time of the last  LOW pulse
 
  while GPIO.input(GPIO_ECHO)==1:          #Check whether Echo is HIGH
    pulse_end = time.time()                #Time of the last HIGH pulse 

  pulse_duration = pulse_end - pulse_start #pulse duration to a variable

  distance = pulse_duration * 17150        #Calculate distance
  distance = round(distance, 2)            #Round to two decimal points

  if distance > 8 and distance < 10:       #Testing the Stance of the user within shoulder length which is on average 8-10cm apart
    print (":",distance - 0.5,"cm")        #Distance with calibration
  else:
    print ("User not standing correctly")  #User was not standing at 8-10cm apart
