with open('input.txt') as data:
    entries = data.read().splitlines()
total = 0
for i in range(len(entries)-1):
    if int(entries[i]) < int(entries[i+1]):
        total += 1
        print(entries[i + 1] + " is greater than " + entries[i] + "!         " + str(total))
    else:
        print(entries[i + 1] + " is not greater than " + entries[i] + "!     " + str(total))
print(total)
