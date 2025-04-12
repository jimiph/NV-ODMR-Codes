import pulsestreamer
from pulsestreamer import PulseStreamer, TriggerStart, TriggerRearm, OutputState, Sequence
import numpy as np

"""
The pulse pattern is a sequence of levels, defining the signal to generate.
It is defined as an array of (duration, level) tuples, in other words, using Run-Length Encoding (RLE).
The duration is always specified in nanoseconds.
The level is either 0 or 1 for digital output or a real number between -1 and +1 in Volt
for analog outputs.
Before a pattern can be sent for streaming to the Pulse Streamer outputs,
they have to be mapped to the output channels. All these steps are performed with the Sequence object,
which is created with PulseStreamer.createSequence().
The digital and analog channel assignment is done with the setDigital() and setAnalog() methods, respectively.
"""

ip = '169.254.8.2'
pulser = PulseStreamer(ip)


"""
Relaxometry
"""

pulse_patt = [(50, 0), (100, 1), (200, 0), (400, 1)]
relax_seq = pulser.createSequence()
relax_seq.setDigital(3, pulse_patt)
final = OutputState.ZERO()
n_runs = int(1e8)

# start = TriggerStart.IMMEDIATE
# rearm = TriggerRearm.MANUAL

# pulser.setTrigger(start=start, rearm=rearm)

pulser.stream(relax_seq, n_runs, final)
