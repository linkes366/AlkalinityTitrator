import time
import io

file_location = './test_output'
cached = 0.0  # seconds


def mark_wait():
    cached = time.time()
    return


def wait_delta(x):
    delta = time.time() - cached
    if (delta <= 0.01):
        return
    else:
        time.sleep(delta)
        return


def file_output(testname, data, *args): #pass a tuple for each arg
    location = file_location
    location += testname
    file = io.open(location, 'a')

    file.close()
