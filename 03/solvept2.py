import sys
  
sys.setrecursionlimit(10**5)

with open('input.txt') as data:
    lines = data.read().splitlines()
    count = len(lines)
    zero = [0,0,0,0,0,0,0,0,0,0,0,0]
    one = [0,0,0,0,0,0,0,0,0,0,0,0]

o2binary = ""
co2binary = ""

def o2(mylines, mycolumn):
    newlist = []
    one[mycolumn] = 0
    zero[mycolumn] = 0
    for item in mylines:
        if item[mycolumn] == "0":
            zero[mycolumn] += 1
        if item[mycolumn] == "1":
            one[mycolumn] += 1
    if one[mycolumn] > zero[mycolumn]:
        majority = "1"
    if one[mycolumn] < zero[mycolumn]:
        majority = "0"
    if one[mycolumn] == zero[mycolumn]:
        majority = "1"
    for myline in mylines:
        if myline[mycolumn] == majority:
            newlist.append(myline)
    if len(newlist) == 1:
        global o2binary
        o2binary = newlist[0]
        print(o2binary)
    if len(newlist) > 1: 
        o2(newlist, mycolumn + 1)

def co2(mylines, mycolumn):
    newlist = []
    one[mycolumn] = 0
    zero[mycolumn] = 0
    for item in mylines:
        if item[mycolumn] == "0":
            zero[mycolumn] += 1
        if item[mycolumn] == "1":
            one[mycolumn] += 1
    if one[mycolumn] < zero[mycolumn]:
        majority = "1"
    if one[mycolumn] > zero[mycolumn]:
        majority = "0"
    if one[mycolumn] == zero[mycolumn]:
        majority = "0"
    for myline in mylines:
        if myline[mycolumn] == majority:
            newlist.append(myline)
    if len(newlist) == 1:
        global co2binary
        co2binary = newlist[0]
        print(co2binary)
    if len(newlist) > 1: 
        co2(newlist, mycolumn + 1)

o2(lines, 0)
co2(lines, 0)

o2decimal = int(o2binary, 2)
co2decimal = int(co2binary, 2)

print(o2decimal * co2decimal)