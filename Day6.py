import numpy as np
import re
from collections import deque

with open('inputday6.txt') as f:
    input = f.readline()
    
fish = [int(i) for i in re.findall(r'\d+', input)]

for i in range(80):
    for j in range(len(fish)):
        if fish[j] == 0:
            fish[j] = 6
            fish.append(8)
        else:
            fish[j] -= 1

print(len(fish))

fish_input = [int(i) for i in re.findall(r'\d+', input)]
fish = deque([0]*9)

for i in fish_input:
    fish[i] += 1

def fish_func(fish, days):
    for i in range(days):
        new = fish[0]
        fish.rotate(-1)
        fish[6] += new
    return sum(fish)

print(fish_func(fish, 256))