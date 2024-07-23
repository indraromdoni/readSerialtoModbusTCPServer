import serial
import time

ser = serial.Serial("COM1", 15200)
while True:
    rd = ser.read(1024).decode('utf-8').rstrip()
    print("read", rd)
    if rd == ":T1000o":
        #return
        print("Test")
        ser.write("100".encode("utf-8"))
    elif rd == ":R2100k":
        #return
        print("Read")
        ser.write("200".encode("utf-8"))
    elif rd == ":R2400n":
        #return
        print("Recall")
        ser.write("300".encode("utf-8"))

    time.sleep(3)