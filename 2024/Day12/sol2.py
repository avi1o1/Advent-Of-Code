grid = []
copy = []
with open("Day12/input1.txt") as file:
    for line in file:
        grid.append(list(line.strip()))
        copy.append(list(line.strip()))

def getNextIndex(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '.':
                return [i, j]
    return [-1, -1]

def getPS(grid, x, y):
    tmp = grid[x][y]
    grid[x][y] = '.'
    p = 4
    s = 1

    if x > 0:
        if copy[x-1][y] == copy[x][y]:
            p -= 1
        if grid[x-1][y] == tmp:
            pt, at = getPA(grid, x-1, y)
            a += at
            p += pt
    
    if x < len(grid) - 1:
        if copy[x+1][y] == copy[x][y]:
            p -= 1
        if grid[x+1][y] == tmp:
            pt, at = getPA(grid, x+1, y)
            a += at
            p += pt

    if y > 0:
        if copy[x][y-1] == copy[x][y]:
            p -= 1
        if grid[x][y-1] == tmp:
            pt, at = getPA(grid, x, y-1)
            a += at
            p += pt
    
    if y < len(grid[x]) - 1:
        if copy[x][y+1] == copy[x][y]:
            p -= 1
        if grid[x][y+1] == tmp:
            pt, at = getPA(grid, x, y+1)
            a += at
            p += pt
    
    return [p, a]


ans = 0
while True:
    x, y = getNextIndex(grid)
    if x == -1 == y:
        break

    p, a = getPA(grid, x, y)
    ans += p * a

print(ans)


 ##  #
######
##  # 

16 sides
16 corners