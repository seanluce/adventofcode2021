import sys

sys.setrecursionlimit(10**5)

with open('input.txt') as data:
    entries = data.read().splitlines()

lanternfish = []
totalfishcount = 0

for row in entries:
    for char in row.split(","):
        lanternfish.append(int(char))

totalfish = len(lanternfish)

print(lanternfish)

column = len(lanternfish)

def fishcount(currentfish, days):
    global totalfish
    print("TOTAL FISH!!!!" + str(totalfish))
    for day in range(days):
        print("Day " + str(day))
        print(currentfish)
        currentfish -= 1
        if currentfish == 0:
            totalfish += 1
            currentfish = 6
            fishcount(8, days - day)
    return(totalfish)
    
for fish in lanternfish:
    fishcount(fish, 0)

print(lanternfish)
print(totalfish)