with open('input.txt') as data:
    lines = data.read().splitlines()
    count = len(lines)
    zero = [0,0,0,0,0,0,0,0,0,0,0,0]
    one = [0,0,0,0,0,0,0,0,0,0,0,0]
    gamma = [0,0,0,0,0,0,0,0,0,0,0,0]
    epsilon = [0,0,0,0,0,0,0,0,0,0,0,0]
for line in lines:
    column = 0
    for char in line:
        if int(char) == 0:
            zero[column] += 1
        if int(char) == 1:
            one[column] += 1
        column += 1
print(zero)
print(one)
count = 0

for element in zero:
    print(count)
    print(element)
    print(one[count])
    if element < one[count]:
        gamma[count] = 1
        epsilon[count] = 0
    if element > one[count]:
        gamma[count] = 0
        epsilon[count] = 1
    count += 1
print(gamma)
print(epsilon)

gammabin = ""
epsilonbin = ""

for g in gamma:
    gammabin += str(g)

for e in epsilon:
    epsilonbin += str(e)

print(int(gammabin, 2) * int(epsilonbin, 2))