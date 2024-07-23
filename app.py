from pyModbusTCP.server import ModbusServer, DataBank, DataHandler
from time import sleep
import serial

def main():
    serv = ModbusServer("0.0.0.0", 502, no_block=True)
    ser = serial.Serial("COM2", 15200)

    test = [0x3A,0x54,0x31,0x30,0x30,0x30,0x6F,0x0D,0x0A]
    read = [0x3A,0x52,0x32,0x31,0x30,0x30,0x6B,0x0D,0x0A]
    recall = [0x3A,0x52,0x32,0x34,0x30,0x30,0x6E,0x0D,0x0A]

    try:
        print("Open serial port...")
        if ser.is_open:
            print("Serial port openned")
        else:
            ser.open()
        print("Start server...")
        serv.start()
        print("Server online")
        while True:
            ret_wr = ser.write(read)
            print('Sending', ret_wr)
            ret_rd = ser.read(1024).decode('utf-8')
            print(ret_rd)
            r = DataBank.set_holding_registers(self=serv.data_bank, address=0, word_list=[int(ret_rd)])
            sleep(6)
    except Exception as e:
        print(e)

if __name__=="__main__":
    main()