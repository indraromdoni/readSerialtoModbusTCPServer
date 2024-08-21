from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
import random

server = ModbusServer("0.0.0.0", 502, no_block=True)
try:
    print("Start server...")
    server.start()
    print("Server online")
    while True:
        r = random.randint(0, 100)
        print(r)
        ret = DataBank.set_holding_registers(self=server.data_bank, address=0, word_list=[r,1,2,3])
        #ret = DataBank.set_words(address=0, word_list=[r,1,2,3])
        sleep(1)
except Exception as e:
    print("Shutdown server:", e)
    server.stop()
    print("Server is offline")