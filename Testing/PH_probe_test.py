import time

import test_func
import ph_probe

#probaly switch this to the other folder so it can access stuff
data = []
voltage = 1
iterations = 100
timeStep = 0.5
ph = ph_probe.PHProbe()
for count in range(iterations):
    data.append((count, ph.get_voltage()))
    time.sleep(timeStep)
test_func.file_output('PH voltage bias', data, ('voltage', voltage), ('iterations', iterations), ('timestep', timeStep))
