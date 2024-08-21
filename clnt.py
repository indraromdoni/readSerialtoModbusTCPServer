from pyModbusTCP.client import ModbusClient
from time import sleep

try:
    client = ModbusClient("192.168.137.20",502)
    ret = client.open()
    print(ret)
    while ret:
        data = client.read_holding_registers(0, 4)
        print(data)
        sleep(1)
except Exception as e:
    print(e)
finally:
    client.close()