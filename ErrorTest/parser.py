import io
import copy

#  This is broken but the other one works for now
def get_all_values(filename):
    sets = []
    data = []
    path = './'
    path += filename
    file = io.open(filename, 'r')
    for line in file.readline():
        if '(' in line:
            data.append((int(line[0]), float(line[2])))
        if len(data) > 0:
            sets.append(copy.copy(data))
            data = []
    return sets


def get_output_values(filename):
    sets = []
    data = []
    path = './'
    path += filename
    file = io.open(filename, 'r')
    for line in file:
        print('loop')
        if '|' in line:
            data.append(float(line[line.find('|')+1:-1]))
            print(f'data:{data}')
        else:
            if len(data) > 0:
                sets.append(copy.copy(data))
                print(sets)
                data = []
    return sets
