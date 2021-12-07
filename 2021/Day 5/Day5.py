import numpy as np
import re

with open('inputday5.txt') as f:
    input = f.readlines()
input = list([s.replace('\n', '') for s in input])

pos_input = []
for line in input:
    x1, y1, x2, y2 = map(int, re.findall(r'([-+]?\d+)', line))
    pos_input.append([x1, y1, x2, y2])

def create_line(x1, y1, x2, y2):
    if x2 < x1:
        tmp = x1
        x1 = x2
        x2 = tmp
    if y2 < y1:
        tmp = y1
        y1 = y2
        y2 = tmp
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            diagram[y][x] += 1

def create_diagonal(x1, y1, x2, y2):
    if x2 < x1:
        tmpx = x1
        tmpy = y1
        x1 = x2
        y1 = y2
        x2 = tmpx
        y2 = tmpy
    y = y1
    if y2 > y1:
        ydir = 1
    else:
        ydir = -1
    for x in range(x1, x2+1):
        diagram[y][x] += 1
        y += ydir

#PART 1

diagram = np.zeros([1000, 1000])

for i in range(len(pos_input)):
    x1, y1, x2, y2 = pos_input[i]
    if x1 == x2 or y1 == y2:
        create_line(x1, y1, x2, y2)

print(np.count_nonzero(diagram > 1))

#PART 2

diagram = np.zeros([1000, 1000])

for i in range(len(pos_input)):
    x1, y1, x2, y2 = pos_input[i]
    if x1 != x2 and y1 != y2:
        create_diagonal(x1, y1, x2, y2)
    else: 
        create_line(x1,y1,x2,y2)

print(np.count_nonzero(diagram > 1))
