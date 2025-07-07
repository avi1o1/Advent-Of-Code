grid = []
with open("Day8/input2.txt", "r") as file:
    data = file.read().splitlines()
    for line in data:
        grid.append(list(line))

for row in grid:
    for char in row:
        print(char, end="")
    print()
print()

freq = {}
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != ".":
            if grid[i][j] not in freq:
                freq[grid[i][j]] = [(i, j)]
            else:
                freq[grid[i][j]].append((i, j))

print(freq)

for each in freq:
    for i in range(len(freq[each])):
        for j in range(i):
            y1, x1 = freq[each][j]
            y2, x2 = freq[each][i]

            if x1 < x2:
                xd, yd = x2 - x1, y2 - y1

                tmpX, tmpY = x1-xd, y1-yd
                while tmpX >= 0 and tmpY >= 0:
                    grid[tmpY][tmpX] = '#'
                    tmpX -= xd
                    tmpY -= yd
                
                tmpX, tmpY = x2+xd, y2+yd
                while tmpX < len(grid) and tmpY < len(grid[0]):
                    grid[tmpY][tmpX] = '#'
                    tmpX += xd
                    tmpY += yd

            else:
                xd, yd = x1 - x2, y2 - y1

                tmpX, tmpY = x1+xd, y1-yd
                while tmpX < len(grid) and tmpY >= 0:
                    grid[tmpY][tmpX] = '#'
                    tmpX += xd
                    tmpY -= yd

                tmpX, tmpY = x2-xd, y2+yd
                while tmpX >= 0 and tmpY < len(grid[0]):
                    grid[tmpY][tmpX] = '#'
                    tmpX -= xd
                    tmpY += yd

ans = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            ans += 1

for each in freq:
    if len(freq[each]) > 1:
        for x, y in freq[each]:
            if grid[x][y] != "#":
                ans += 1

for row in grid:
    for char in row:
        print(char, end="")
    print()     

print(ans)


            
            
            