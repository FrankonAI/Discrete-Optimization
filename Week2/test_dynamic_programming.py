#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight']) 
#定义Item函数,输出形式为Item(index=xxx,value=xxx,weight=xxx)

capacity=11 
item_count=4
lines=['4 11','8 4','10 5','15 8','4 3']
items=[]
for i in range(1, item_count+1):
	line = lines[i]
	parts = line.split()
	items.append(Item(i-1, int(parts[0]), int(parts[1])))
#四个传入参数


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
#传出taken、value

output_data = str(value) + ' ' + str(0) + '\n'
output_data += ' '.join(map(str, taken))
print(output_data)