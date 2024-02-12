import time
import io
import datetime

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


def file_output(test_name, data, *args): #pass a tuple for each arg= name and val, data = time and datapoint
    location = file_location
    location += test_name
    location += '.txt'
    file = io.open(location, 'a', encoding="locale")

    write_string = f'\n{test_name}'
    write_string += '\t'
    write_string += str(datetime.datetime.now())
    write_string += '\n'
    for arg in args:
        write_string += arg[0]
        write_string += ':'
        write_string += arg[1]
        write_string += '\n'
    write_string += 'Time \t DataPoint \n'
    for point in data:
        write_string += f'{point[0]} \t {point[1]} \n'
    file.write(write_string)
    file.close()

print('running')
data = [(1, 0), (2, 4), (3, 8.8)]
name = 'Testing'
file_output(name, data, ('voltage', '2'))
print('running2')
