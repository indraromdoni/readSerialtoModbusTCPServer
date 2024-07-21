import serial
import time

ser = serial.Serial("COM1", 9600)
while True:
    print("read", ser.read(1024).decode('utf-8'))
    time.sleep(1)
    if KeyboardInterrupt:
        break