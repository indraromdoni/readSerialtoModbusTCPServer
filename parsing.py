txt1 = ":D21002024082102145203000100000000000000000100000001000000000159018B014700000000000000000000000000000000000000000000000000000000000000000000A853000002750000A7D400004E7D0064000002260226012C000000000212023001FE03A0001800000000000000000000000000000000t"
txt2 = ":D210020240821031615180001000103010302120219053D00910000000001AB000001B5000000DB0066000000000000000000000000021201A803E80000000000000000000135B9000002760001351700000C290064000002260226012C000000000212023001EA06B8040F00000000000000000000000000000000"
start_bit = [6,10,12,14,16,18,20,22,24,26,28,30,32,34,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100,104,108,112,116,120,124,128,132,136,144,152,160,168,172,176,180,184,188,192,196,200,204,208,212,216,220,222,224,232,240]
bit_length = [4,2,2,2,2,2,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,8,8,8,8,4,4,4,4,4,4,4,4,4,4,4,4,4,2,2,8,8,8]
data_type = ['dec','dec','dec','dec','dec','dec','dec','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex','hex']
key = ['year','month ','day','week day','hour','minute','second','comp type','operation place','IGV auto/manual','blow off open/close','comp status','loading status','ready to run','Discharge pressure (System press)','Discharge pressure (comp outlet)','Main motor current','Lube oil pressure','Reserve','reserve','Lube oil temp','reserve','final stage inlet air temp','Reserve','2nd stage shaft vib','3rd stage shaft vib','Air Flow','Reserve','Reserve','Reserve','Reserve','Reserve','Reserve','IGV position','BV position','Remote const. press. Set point','Reserve','Reserve','Reserve','Running hour','Start time','Loading hour','loading time','lube oil press. Low limit','Reserve','lube oil temp. High limit','Each stage inlet air temp high limit','each stage vib high limit','Reserve','Reserve','const press control set point','Unloading discharge press (H) set point','loading discharge press (L) set point','motor anti overload current control SP','anti-surge lower limit current','anti-surge press control SP','Reserve','aux eq status','heavy trouble','light trouble','maintain']
val1 = list()
val2 = list()
for s, l, d in zip(start_bit, bit_length, data_type):
    if d == 'dec':
        val1.append(int(txt1[s:s+l]))
        val2.append(int(txt2[s:s+l]))
    elif d == 'hex':
        vtxt1 = int(txt1[s:s+l], 16)
        vtxt2 = int(txt2[s:s+l], 16)
        val1.append(vtxt1)
        val2.append(vtxt2)
v1 = dict(zip(key, val1))
v2 = dict(zip(key, val2))
for var, val in zip(key, val1):
    print(var,val)
for var, val in zip(key, val2):
    print(var,val)