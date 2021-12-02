with open('inputday1.txt') as f:
    input = f.readlines()


input = list(map(int,[s.replace('\n', '') for s in input]))

# PART 1
count = 0
i = 0
while i < (len(input)-1):
    if input[i+1] > input[i]:
        count += 1
    i += 1

print(count)

# PART 2

i = 0
sum = []
while i < (len(input)-2):
    sum.append(input[i] + input[i+1] + input[i+2])
    i += 1

count = 0
i = 0
while i < (len(sum)-1):
    if sum[i+1] > sum[i]:
        count += 1
    i += 1

print(count)