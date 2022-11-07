with open('input.txt') as data:
    entries = data.read().splitlines()

lanternfish = []

for row in entries:
    for char in row.split(","):
        lanternfish.append(int(char))

print(lanternfish)

for day in range(1,81):
    print(day)
    currentfish = 0
    for fish in lanternfish:
        if fish == 0:
            lanternfish[currentfish] = 6
            currentfish += 1
            lanternfish.append(9)
        else:
            lanternfish[currentfish] -= 1
            currentfish += 1

print(lanternfish)

print(len(lanternfish))