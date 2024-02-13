import time
import test_func

'#probaly switch this to the other folder so it can access stuff'


ph_gains = 1


def ph_test(ph_probe):
    data = []
    voltage = 1
    iterations = 100
    time_step = 0.5
    ph = ph_probe
    for count in range(iterations):
        data.append((count, ph.get_voltage()))
        time.sleep(time_step)
    test_func.file_output('PH voltage bias', data, ('voltage', voltage), ('iterations', iterations),
                          ('timestep', time_step))
