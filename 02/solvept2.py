with open('input.txt') as data:
    input = data.read().splitlines()
h = 0
d = 0
a = 0
for line in input:
    direction = line.split()[0]
    value = line.split()[1]
    if direction == "forward":
        h += int(value)
        d += (a * int(value))
    if direction == "down":
        a += int(value)
    if direction == "up":
        a -= int(value)
print(h)
print(d)
print(a)
print(h * d)