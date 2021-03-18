import time
import board
import busio
import adafruit_adxl34x
import matplotlib.pyplot as plt
import numpy as np
#import csv ~imports csv package

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)

#f = open("accelerometer_data.csv","w", newline="") ~names and opens csv file that would be written to
#c = csv.writer(f)

#c.writerow(["X-Value","Y-Value","Z-Value","Time"]) ~writes first row of csv file

#start_time = time.time ~function to start timing

while True:
    print("%f %f %f"%accelerometer.acceleration)
#   current_time = time.time ~assing in time measurement
#   elapsed_time = current_time - start_time
#   c.writerow([accelerometer.X, accelerometer.Y, accelerometer.Z,elapsed_time]) ~calls X,Y,& Z values from accelerometer and plots them into csv
    time.sleep(0.5) # i would change time to (.001) for better data


plt.plot(accelerometer)
plt.show()
