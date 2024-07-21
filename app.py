from pyModbusTCP.server import ModbusServer, DataBank, DataHandler
from time import sleep
import serial
import threading

response = list()
exit_ = 0

def readSerial(ser,serv):
    global response, exit_
    print("Start server...")
    serv.start()
    print("Server online")
    while True:
        ret = ser.read(1024).decode('utf-8')
        response = ret
        sleep(1)
        if exit_==1:
            break

def main(ser):
    global response, exit_

    test = [0x3A,0x54,0x31,0x30,0x30,0x30,0x6F,0x0D,0x0A]
    read = [0x3A,0x52,0x32,0x31,0x30,0x30,0x6B,0x0D,0x0A]
    recall = [0x3A,0x52,0x32,0x34,0x30,0x30,0x6E,0x0D,0x0A]

    while True:
        ret_wr = ser.write(read)
        ret = DataBank.set_holding_registers(self=serv.data_bank, address=0, word_list=response)
        sleep(1)
        if exit_==1:
            break

if __name__=="__main__":
    serv = ModbusServer("0.0.0.0", 502, no_block=True)
    ser = serial.Serial("COM2", 9600)
    t1 = threading.Thread(target=readSerial, args=[ser,serv], daemon=True)
    t2 = threading.Thread(target=main, args=[ser,], daemon=True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()