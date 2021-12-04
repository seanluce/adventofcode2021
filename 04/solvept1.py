import array as arr
import re

with open('input.txt') as data:
    input = data.read().splitlines()

numbers = input[0].split(",")
print(numbers)

rawboards = input[2::]

boardarray = []
boardhits = []
boardnumber = 0

def checkwin(board, winnumber):
    #print("Hit on board " + board)
    #check rows on board
    # 0 = 0 - 4
    # 1 = 5 - 9
    # 2 = 10 - 14
    boardstartrow = int(board) * 5
    print(boardstartrow)
    boardendrow = boardstartrow + 5
    print(boardendrow)
    unmarkedsum = 0

    for i in range(boardstartrow,boardendrow):
        if boardhits[i][1] == 1 and boardhits[i][2] == 1 and boardhits[i][3] == 1 and boardhits[i][4] == 1 and boardhits[i][5] == 1:
            print("We have a row winner on board " + board + "!")
            for j in range(boardstartrow,boardendrow):
                print(boardarray[j])
                columncheck = 1
                for column in boardarray[j][1::]:
                    if boardhits[j][columncheck] == 0:
                        #print(boardarray[j][columncheck])
                        unmarkedsum += int(boardarray[j][columncheck])
                    columncheck += 1
            for k in range(boardstartrow,boardendrow):
                print(boardhits[k])
            print(unmarkedsum * int(winnumber))
            exit()
    for m in range(1,5):
        if boardhits[boardstartrow][m] == 1 and boardhits[boardstartrow + 1][m] == 1 and boardhits[boardstartrow + 2][m] == 1  and boardhits[boardstartrow + 3][m] == 1 and boardhits[boardstartrow + 4][m] == 1 and boardhits[boardstartrow + 5][m] == 1:
            print("We have a column winner on board " + board + "!")
            for p in range(boardstartrow,boardendrow):
                print(boardarray[p])
                columncheck = 1
                for column in boardarray[p][1::]:
                    if boardhits[p][columncheck] == 0:
                        #print(boardarray[p][columncheck])
                        unmarkedsum += int(boardarray[p][columncheck])
                    columncheck += 1
            for n in range(boardstartrow,boardendrow):
                print(boardhits[n])
            print(unmarkedsum * int(winnumber))
            exit()

for row in rawboards:
    if len(row) == 0:
        boardnumber += 1
    else:
        rowarray = re.split(' +', row.lstrip())
        rowarray.insert(0,str(boardnumber))
        boardarray.append(rowarray)
        boardhits.append([boardnumber, 0, 0, 0, 0, 0])

print(boardarray[270])

for number in numbers:
    rownumber = 0
    for row in boardarray:
        columnnumber = 1
        for column in row[1::]:
            if int(number) == int(column):
                boardhits[rownumber][columnnumber] = 1
                checkwin(row[0], number)
            columnnumber += 1
        rownumber += 1


