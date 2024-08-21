import serial

def parse(start_bit: list, bit_length: list, data_type: list, value: str):
    val = list()
    for s, l, d in zip(start_bit, bit_length, data_type):
        if d == 'dec':
            val.append(int(value[s:s+l]))
        elif d == 'hex':
            val.append(int(value[s:s+l], 16))
    return val

test = [0x3A,0x54,0x31,0x30,0x30,0x30,0x6F,0x0D,0x0A]
read = [0x3A,0x52,0x32,0x31,0x30,0x30,0x6B,0x0D,0x0A]
recall = [0x3A,0x52,0x32,0x34,0x30,0x30,0x6E,0x0D,0x0A]

start_bit = [6,10,12,14,16,18,20,22,24,26,28,30,32,34,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100,104,108,112,116,120,124,128,132,136,144,152,160,168,172,176,180,184,188,192,196,200,204,208,212,216,220,222,224,232,240]
bit_length = [4,2,2,2,2,2,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,8,8,8,8,4,4,4,4,4,4,4,4,4,4,4,4,4,2,2,8,8,8]
data_type = ['dec','dec','dec','dec','dec','dec','dec','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex']
key = ['year','month ','day','week day','hour','minute','second','comp type','operation place','IGV auto/manual','blow off open/close','comp status','loading status','ready to run','Discharge pressure (System press)','Discharge pressure (comp outlet)','Main motor current','Lube oil pressure','Reserve','reserve','Lube oil temp','reserve','final stage inlet air temp','Reserve','2nd stage shaft vib','3rd stage shaft vib','Air Flow','Reserve','Reserve','Reserve','Reserve','Reserve','Reserve','IGV position','BV position','Remote const. press. Set point','Reserve','Reserve','Reserve','Running hour','Start time','Loading hour','loading time','lube oil press. Low limit','Reserve','lube oil temp. High limit','Each stage inlet air temp high limit','each stage vib high limit','Reserve','Reserve','const press control set point','Unloading discharge press (H) set point','loading discharge press (L) set point','motor anti overload current control SP','anti-surge lower limit current','anti-surge press control SP','Reserve','aux eq status','heavy trouble','light trouble','maintain']

try:
    ser = serial.Serial(port="/dev/ttyO1", baudrate=9600, bytesize=8, parity=serial.PARITY_EVEN, stopbits=2, timeout=6, write_timeout=5)
    ret = ser.write(read)
    print(ret)
    rd = ser.read(1024).decode("utf-8")
    print(rd)
    res = parse(start_bit, bit_length, data_type, rd)
    print(dict(zip(key, res)))
except Exception as e:
    print(e)
finally:
    ser.close()