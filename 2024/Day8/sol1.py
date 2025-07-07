grid = []
with open("Day8/input1.txt", "r") as file:
    data = file.read().splitlines()
    for line in data:
        grid.append(list(line))

freq = {}
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != ".":
            if grid[i][j] not in freq:
                freq[grid[i][j]] = [(i, j)]
            else:
                freq[grid[i][j]].append((i, j))

for each in freq:
    for i in range(len(freq[each])):
        for j in range(i):
            y1, x1 = freq[each][j]
            y2, x2 = freq[each][i]

            if x1 < x2:
                xd, yd = x2 - x1, y2 - y1
                if x1-xd >= 0 and y1-yd >= 0:
                    grid[y1-yd][x1-xd] = '#'
                if x2+xd < len(grid) and y2+yd < len(grid[0]):
                    grid[y2+yd][x2+xd] = '#'
            else:
                xd, yd = x1 - x2, y2 - y1
                if x1+xd < len(grid) and y1-yd >= 0:
                    grid[y1-yd][x1+xd] = '#'
                if x2-xd >= 0 and y2+yd < len(grid[0]):
                    grid[y2+yd][x2-xd] = '#'

ans = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            ans += 1
print(ans)


            
            
            