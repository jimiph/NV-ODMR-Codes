# rm = pyvisa.ResourceManager()
# rm.list_resources()
# print(rm.list_resources())
# inst = rm.open_resource('GPIB0::1::INSTR')
# print(inst.query("*IDN?"))
# inst.write(":FREQ 2500000000.0;")
# #inst.query("HS,AG2.")
# inst.write(":POW -0.10DBM;")

# inst.write(":OUTP ON;")
# for i in range(0, 4):
#     #print(i)
#     a = str(2500000000.0+10000000*i)
#     #print(a)
#     inst.write(":FREQ "+a+";")
#     time.sleep(2)

# inst.write(":OUTP OFF;")


# ":FREQ:SWE:MODE SING;STAR 1000000000.0;STOP 3000000000.0;POIN 20;DWEL 1.000;"
# ":FREQ:SWE:STAT ON;"
# ":FREQ:SWE:STAT OFF;"
#":OUTP ON;"
#":OUTP OFF;"
# ":FREQ:SWE:STAT ON;"
# ":FREQ:SWE:STAT OFF;"
#":POW:SWE:MODE SING;STAR -115.0DBM;STOP -110.0DBM;POIN 20;DWEL 1.000;"
# ":POW:SWE:STAT ON;"
# ":POW:SWE:STAT OFF;"
#inst.close()
#":OUTP:MOD OFF;"
#":OUTP:MOD ON;"
#":AM:STAT EXT;"
#":AM:STAT INT;"
#":AM:STAT ON;"
#":AM:STAT OFF;"


import time
import pyvisa

def dev_connect():
    rm = pyvisa.ResourceManager()
    rm.list_resources()
    print(rm.list_resources())
    inst = rm.open_resource('GPIB0::1::INSTR')
    print(inst.query("*IDN?"))
    
def output_ON():
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource('GPIB0::1::INSTR')
    inst.write(":OUTP ON;")
    
def output_OFF():
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource('GPIB0::1::INSTR')
    inst.write(":OUTP OFF;")
    
def output_Mod_ON():
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource('GPIB0::1::INSTR')
    inst.write(":OUTP:MOD ON;")
    
def output_Mod_OFF():
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource('GPIB0::1::INSTR')
    inst.write(":OUTP:MOD OFF;")
    
def AM_Mod():
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource('GPIB0::1::INSTR')
    inst.write(":AM:STAT EXT;")
    
def set_freq(frequency:2800000000.0):
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource('GPIB0::1::INSTR')
    freq=str(frequency)
    inst.write(":FREQ "+freq+";")
    
def set_power(power:-115.00):
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource('GPIB0::1::INSTR')
    pow=str(power)
    inst.write(":POW "+pow+"DBM;")
    #inst.write(":POW -0.10DBM;")

name="SING"
def freq_sweep(mode:name,start:1000000000.0,stop:3000000000.0,points:20,step:1.000):
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource('GPIB0::1::INSTR')
    start=str(start)
    stop=str(stop)
    points=str(points)
    step=str(step)
    inst.write(":FREQ:SWE:MODE "+mode+";STAR "+start+";STOP "+stop+";POIN "+points+";DWEL "+step+";")
    inst.write(":FREQ:SWE:STAT ON;")

def freq_sweepoff():
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource('GPIB0::1::INSTR')
    inst.write(":FREQ:SWE:STAT OFF;")
    
def power_sweep(mode:name,start:-115.0,stop:-110.0,points:20,step:1.000):
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource('GPIB0::1::INSTR')
    start=str(start)
    stop=str(stop)
    points=str(points)
    step=str(step)
    inst.write(":POW:SWE:MODE "+mode+";STAR "+start+"DBM;STOP "+stop+"DBM;POIN "+points+";DWEL "+step+";")
    inst.write(":POW:SWE:STAT ON;")
    

def power_sweepoff():
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource('GPIB0::1::INSTR')
    inst.write(":POW:SWE:STAT OFF;")

    
# dev_connect()
#output_OFF()
# set_freq(2700000000.0)
# set_power(-110.0)
#freq_sweep(name,1000000000.0,3000000000.0,20,1.000)
#output_OFF()
#power_sweep(name,-115.0,-110.0,20,1.000)



