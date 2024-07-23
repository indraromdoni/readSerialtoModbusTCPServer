import serial
import time

ser = serial.Serial("COM1", 9600)
while True:
    rd = ser.read(1024).decode('utf-8').rstrip()
    print("read", rd)
    if rd == ":T1000o":
        #return
        print("Test")
        ser.write("Testing code".encode("utf-8"))
    elif rd == ":R2100k":
        #return
        print("Read")
        ser.write("Read code".encode("utf-8"))
    elif rd == ":R2400n":
        #return
        print("Recall")
        ser.write("Recall code".encode("utf-8"))

    time.sleep(1)