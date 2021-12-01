with open('input.txt') as data:
    entries = data.read().splitlines()
total = 0
for i in range(len(entries)-3):
    if int(entries[i])+int(entries[i+1])+int(entries[i+2]) < int(entries[i+1])+int(entries[i+2])+int(entries[i+3]):
        total += 1
        print(str(int(entries[i+1])+int(entries[i+2])+int(entries[i+3])) + " is greater than " + str(int(entries[i])+int(entries[i+1])+int(entries[i+2])) + "!         " + str(total))
    else:
        print(str(int(entries[i+1])+int(entries[i+2])+int(entries[i+3])) + " is not greater than " + str(int(entries[i])+int(entries[i+1])+int(entries[i+2])) + "!     " + str(total))
print(total)