import serial
import time

ser = serial.Serial("com5")
print(ser.name)
print("Set output to 2 volts")
ser.write(b'VOLT050\r')
time.sleep(3)
ser.write(b'VOLT010\r')
