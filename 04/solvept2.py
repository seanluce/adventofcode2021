import array as arr
import re

with open('input.txt') as data:
    input = data.read().splitlines()

numbers = input[0].split(",")
rawboards = input[2::]
boardarray = []
boardcount = 0
boardhits = []
boardnumber = 0
wintracker = [0]

def checkwin(board, winnumber):
    boardstartrow = int(board) * 5
    boardendrow = boardstartrow + 5
    unmarkedsum = 0
    for i in range(boardstartrow,boardendrow):
        if boardhits[i][1] == 1 and boardhits[i][2] == 1 and boardhits[i][3] == 1 and boardhits[i][4] == 1 and boardhits[i][5] == 1:
            if wintracker[int(board)] != 1:
                print("We have a row winner on board " + board + "!")
                wintracker[int(board)] += 1
                numberlosers = sum(1 for i in wintracker if i == 0)
                if numberlosers == 0:
                    print("No. of Losers: " + str(numberlosers))
                    for j in range(boardstartrow,boardendrow):
                        columncheck = 1
                        for column in boardarray[j][1::]:
                            if boardhits[j][columncheck] == 0:
                                unmarkedsum += int(boardarray[j][columncheck])
                            columncheck += 1
                    print(unmarkedsum*int(winnumber))
                    exit()        
    for m in range(1,6):
        if boardhits[boardstartrow][m] == 1 and boardhits[boardstartrow + 1][m] == 1 and boardhits[boardstartrow + 2][m] == 1  and boardhits[boardstartrow + 3][m] == 1 and boardhits[boardstartrow + 4][m] == 1:
            if wintracker[int(board)] != 1:
                print("We have a column winner on board " + board + "!")
                wintracker[int(board)] += 1
                numberlosers = sum(1 for i in wintracker if i == 0)
                if numberlosers == 0:
                    print("No. of Losers: " + str(numberlosers))
                    for k in range(boardstartrow,boardendrow):
                        columncheck = 1
                        for column in boardarray[k][1::]:
                            if boardhits[k][columncheck] == 0:
                                unmarkedsum += int(boardarray[k][columncheck])
                            columncheck += 1
                    print(unmarkedsum*int(winnumber))
                    exit()
for row in rawboards:
    if len(row) == 0:
        boardnumber += 1
        wintracker.append(0)
    else:
        rowarray = re.split(' +', row.lstrip())
        rowarray.insert(0,str(boardnumber))
        boardarray.append(rowarray)
        boardhits.append([boardnumber, 0, 0, 0, 0, 0])
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
