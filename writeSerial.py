import serial

ser = serial.Serial("COM2", 9600)

test = [0x3A,0x54,0x31,0x30,0x30,0x30,0x6F,0x0D,0x0A]
read = [0x3A,0x52,0x32,0x31,0x30,0x30,0x6B,0x0D,0x0A]
recall = [0x3A,0x52,0x32,0x34,0x30,0x30,0x6E,0x0D,0x0A]

ret = ser.write(recall)
print(ret)
rd = ser.read(1024).decode("utf-8")
print(rd)