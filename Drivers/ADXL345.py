import time
import board
import busio
import array
import math
import adafruit_adxl34x

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)

accel = []
upperthreshold = 5.0
lowerthreshold = -5.0
steps = 0
count = 0
height = 72
stride = 0
distance = 0
speed = 0
start = time.time()

#height = height * 0.0254

while True:
    StrideT = time.time() - start
    StrideTime = (int(StrideT))
    #print(StrideTime)
    x, y, z = accelerometer.acceleration
    mag = math.sqrt((x**2)+(y**2)+(z**2))
    accel.append(mag)
    mean = sum(accel) / len(accel)
    magzero = mag - mean
    print(magzero)
    #print(accelerometer.acceleration)
    time.sleep(0.25)

    if ( magzero > upperthreshold ):
        steps = steps + 1
        print(steps)
        count = count + 1
        #print(count)
        #distance = distance + (stride * steps)
        #print(distance)
    if ( magzero < lowerthreshold ):
        steps = steps + 1
        print(steps)
        count = count + 1
        #print(count)
        #distance = distance + (stride * steps)
        #print(distance)
    #else:
        #print( "No step detected" )

        if(StrideTime % 2 == 0):
            if (count == 1):
                stride = height / 5
                #print(stride)
                distance = distance + (steps * stride)
                #print(distance)
                speed = count * (stride / 2)
                print(speed)
            if (count == 2):
                stride = height / 4
                #print(stride)
                distance = distance + (steps * stride)
                #print(distance)
                speed = count * (stride / 2)
                print(speed)
            if (count == 3):
                stride = height / 3
                #print(stride)
                distance = distance + (steps * stride)
                #print(distance)
                speed = count * (stride / 2)
                print(speed)
            if (count == 4):
                stride = height / 2
                #print(stride)
                distance = distance + (steps * stride)
                #print(distance)
                speed = count * (stride / 2)
                print(speed)
            if (count == 5):
                stride = height / 1.2
                #print(stride)
                distance = distance + (steps * stride)
                #print(distance)
                speed = count * (stride / 2)
                print(speed)
            if (6 <= count < 8):
                stride = height
                #print(stride)
                distance = distance + (steps * stride)
                #print(distance)
                speed = count * (stride / 2)
                print(speed)
            if (count >= 8):
                stride = height * 1.2
                #print(stride)
                distance = distance + (steps * stride)
                #print(distance)
                speed = count * (stride / 2)
                print(speed)
        else:
            count = 0
