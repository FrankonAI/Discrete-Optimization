#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])


def dynamic(items,item_count,capacity,lines):
    
    valuemap=[[0]*(capacity+1)]
    for item in items:
        coloum=[0]
        weight=item.weight
        if weight>capacity:
            valuemap.append(valuemap[-1])
        else:
            fore=valuemap[-1]
            coloum+=fore[1:weight]
            for ind,forevalue in enumerate(fore[0:capacity-weight+1]):
                coloum.append(max(fore[ind+weight],forevalue+item.value))
            valuemap.append(coloum)

    value=valuemap[-1][-1]
    taken=[0]*item_count
    pos=capacity
    for item_pos in range(item_count,0,-1):
        if valuemap[item_pos][pos]==valuemap[item_pos-1][pos]:
            continue
        else:
            pos-=items[item_pos-1].weight
            taken[item_pos-1]=1
    
    return value,taken


def solve_it(input_data):
    # Modify this code to run your optimization algorithm
    # parse the input
    lines = input_data.split('\n')
    firstLine = lines[0].split() 
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])
    items = []
    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))
    
    value,taken=dynamic(items,item_count,capacity,lines)

    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

