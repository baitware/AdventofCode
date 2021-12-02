with open('inputday2.txt') as f:
    input = f.readlines()

input = list([s.replace('\n', '') for s in input])

input_nr = []
for item in input:
    for subitem in item.split():
        if(subitem.isdigit()):
            input_nr.append(int(subitem))

position = [0,0,0]
forward = "forward"
up = "up"
down = "down"

i = 0
while i < len(input):
    if forward in input[i]:
        position[0] = position[0] + input_nr[i]
        position[1] = position[1] + (position[2] * input_nr[i])
    
    elif up in input[i]:
        position[2] = position[2] - input_nr[i]

    elif down in input[i]:
        position[2] = position[2] + input_nr[i]

    i += 1

print(position)

print(position[0]*position[1])