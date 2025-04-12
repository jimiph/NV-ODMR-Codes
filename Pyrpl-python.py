import sys
import redpitaya_scpi as scpi
import matplotlib.pyplot as plot
import numpy as np
IP = 'rp-f0a8d0.local'

rp_s = scpi.scpi(IP)

rp_s.tx_txt('ACQ:RST')

rp_s.tx_txt('ACQ:DEC 64')
rp_s.tx_txt('ACQ:START')
# rp_s.tx_txt('ACQ:TRig:LEV 0.400 V')
rp_s.tx_txt('ACQ:TRig NOW')

while 1:
    rp_s.tx_txt('ACQ:TRig:STAT?')
    if rp_s.rx_txt() == 'TD':
        break

## ! OS 2.00 or higher only ! ##
while 1:
    rp_s.tx_txt('ACQ:TRig:FILL?')
    if rp_s.rx_txt() == '1':
        break

rp_s.tx_txt('ACQ:SOUR1:DATA?')
buff_string = rp_s.rx_txt()
buff_string = buff_string.strip('{}\n\r').replace("  ", "").split(',')
buff = list(map(float, buff_string))

voltage=np.array(buff)
print(np.average(voltage))

plot.plot(buff)
plot.ylabel('Voltage')
plot.show()