import numpy as np, re, math

with open('inputday7.txt') as f:
    input = f.readline()
    
crab_pos = np.array([int(i) for i in re.findall(r'\d+', input)])

def fuel_cost(crab_pos, align):
    fuel = 0
    for i in range(len(crab_pos)):
        fuel = fuel + abs(crab_pos[i] - align)
    return fuel

def fuel_cost2(crab_pos, align):
    fuel = 0
    for i in range(len(crab_pos)):
        for j in range(abs(crab_pos[i] - align) + 1):
            fuel = fuel + j
    return fuel

#PART 1

align = int(np.median(crab_pos))

min_fuel = fuel_cost(crab_pos, align)

print(min_fuel)

#PART 2

fuel_list = []
for i in range(np.amax(crab_pos)):
    align = i
    fuel_list.append(fuel_cost2(crab_pos, align))

fuel_list = np.array(fuel_list)
min_fuel = np.amin(fuel_list)

print(min_fuel)
