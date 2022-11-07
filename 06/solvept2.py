import math
with open('input.txt') as data:
    entries = data.read().splitlines()

lanternfish = []

fishcreated = 0
newfisharray = []

days = 18

for row in entries:
    for char in row.split(","):
        lanternfish.append(int(char))

totalfish = len(lanternfish)
print("Starting Fish: + " + str(lanternfish))

def manyfish(newfishes, daysremaining):
    print("Days Remaining: " + str(daysremaining))
    global totalfish
    for f in range(newfishes):
        fishcreated = math.trunc(((daysremaining) / 7) + 1)
        #print("Fish Created this run: " + str(fishcreated))
        totalfish = totalfish + fishcreated
        #print(totalfish)
        newfisharray = []
        for i in range(fishcreated):
            newfisharray.append(0)
        if daysremaining == 1:
            exit()
        else:
            daysremaining -= 1
            manyfish(newfisharray, daysremaining)

print(totalfish)
manyfish(totalfish, days)
