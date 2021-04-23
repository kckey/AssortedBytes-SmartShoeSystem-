import time
import board
import busio
import array
import math
import adafruit_adxl34x

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)

accel = []
threshold = 3.0
steps = 0
height = 72
stride = 0
start = time.time()

while True:
    StrideTime = time.time() - start
    print(StrideTime)
    x, y, z = accelerometer.acceleration
    mag = math.sqrt((x**2)+(y**2)+(z**2))
    accel.append(mag)
    mean = sum(accel) / len(accel)
    magzero = mag - mean
    #print(magzero)
    #print(accelerometer.acceleration)
    time.sleep(0.25)

    if ( magzero > threshold ):
        steps = steps + 1
        print(steps)
    else:
        print( "No step detected" )

        if (StrideTime <= 2) & (steps < 2):
            stride = height / 5
            print(stride)
        else:
            print("nothing happened")
        if (StrideTime <= 2) & (2 <= steps < 3):
            stride = height / 4
            print(stride)
        else:
            print("nothing happened")
        if (StrideTime <= 2) & (3 <= steps < 4):
            stride = height / 3
            print(stride)
        else:
            print("nothing happened")
        if (StrideTime <= 2) & (4 <= steps < 5):
            stride = height / 2
            print(stride)
        else:
            print("nothing happened")
        if (StrideTime <= 2) & (5 <= steps < 6):
            stride = height / 1.2
            print(stride)
        else:
            print("nothing happened")
        if (StrideTime <= 2) & (6 <= steps < 8):
            stride = height
            print(stride)
        else:
            print("nothing happened")
        if (StrideTime <= 2) & (steps >= 8):
            stride = height * 1.2
            print(stride)
        else:
            print("nothing happened")
            
