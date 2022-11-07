with open('input.txt') as data:
    entries = data.read().splitlines()

gridrows = []
column = []
total = 0

for x in range(1000):
    column = []
    for y in range(1000):
        column.append(0)
    gridrows.append(column)

for row in entries:

    first  = row.split(" -> ")[0]
    first_x = int(first.split(",")[0])
    first_y = int(first.split(",")[1])

    second = row.split(" -> ")[1]
    second_x = int(second.split(",")[0])
    second_y = int(second.split(",")[1])

    if first_x == second_x: # this line is vertical
        if first_y < second_y:
            ystart = first_y
            yend = second_y
        else: 
            ystart = second_y
            yend = first_y
        while ystart <= yend:
            gridrows[ystart][first_x] += 1
            ystart += 1
    elif first_y == second_y: # this line is horizontal
        if first_x < second_x:
            xstart = first_x
            xend = second_x
        else: 
            xstart = second_x
            xend = first_x
        while xstart <= xend:
            gridrows[first_y][xstart] += 1
            xstart += 1
    else:
        if first_x < second_x:
            xstart = first_x
            ystart = first_y
            xend = second_x
            yend = second_y
        else: 
            xstart = second_x
            ystart = second_y
            xend = first_x
            yend = first_y
        while xstart <= xend:
            if ystart <= yend:
                gridrows[ystart][xstart] += 1
                ystart += 1
                xstart += 1
            else: 
                gridrows[ystart][xstart] += 1
                ystart -= 1
                xstart += 1
        
for gridrow in gridrows:
    print(gridrow)
    for count in gridrow:
        if count >= 2:
            total += 1

print(total)