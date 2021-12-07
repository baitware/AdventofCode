import numpy as np

with open('inputday3.txt') as f:
    input = f.readlines()

input = [s.replace('\n', '') for s in input]
7
def split(word):
    return [char for char in word]

i = 0
binary_list = []
while i < len(input):
    binary_list.append(split(input[i]))
    i += 1

binary_array = np.array(binary_list)

gamma = []
epsilon = []
i = 0
while i < len(binary_array[0, :]):
    count0 = np.count_nonzero(binary_array[:, i] == '0')
    count1 = np.count_nonzero(binary_array[:, i] == '1')
    
    if count0 > count1:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)
    i += 1

i = 0
oxygen = np.array(binary_list)
while i < len(binary_array[0, :]):
    count0 = np.count_nonzero(oxygen[:, i] == '0')
    count1 = np.count_nonzero(oxygen[:, i] == '1')

    if count0 < count1:
        oxygen = np.delete(oxygen, np.where(oxygen[:, i] == '0'),0)
    elif count0 > count1:
        oxygen = np.delete(oxygen, np.where(oxygen[:, i] == '1'),0)
    else:
        oxygen = np.delete(oxygen, np.where(oxygen[:, i] == '0'),0)
    if len(oxygen) <= 1:
        break
    
    i += 1

i = 0
c02 = np.array(binary_list)
while i < len(binary_array[0, :]):
    count0 = np.count_nonzero(c02[:, i] == '0')
    count1 = np.count_nonzero(c02[:, i] == '1')

    if count0 < count1:
        c02 = np.delete(c02, np.where(c02[:, i] == '1'),0)
    elif count0 > count1:
        c02 = np.delete(c02, np.where(c02[:, i] == '0'),0)
    else:
        c02 = np.delete(c02, np.where(c02[:, i] == '1'),0)
    if len(c02) <= 1:
        break
    
    i += 1  

gamma = int((''.join([str(g) for g in gamma])),2)
epsilon = int((''.join([str(g) for g in epsilon])),2)

oxygen = int((''.join([str(g) for g in oxygen[0]])),2)
c02 = int((''.join([str(g) for g in c02[0]])),2)

print(oxygen, c02, oxygen*c02)