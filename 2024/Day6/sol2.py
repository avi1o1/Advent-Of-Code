# Optimise

grid = []
with open("Day6/input2.txt", "r") as file:
    for line in file:
        grid.append(list(line.strip()))

gridHardCopy = [row.copy() for row in grid]

def getAnswer(i, j):
    heading = 'N'
    ans = 1

    N, M = len(grid)-1, len(grid[0])-1
    O = M*N
    cnt = 0
    while i > 0 and j > 0 and i < N and j < M:
        cnt += 1
        grid[i][j] = 'X'
        if heading == 'N':
            if grid[i-1][j] == '.':
                i -= 1
                ans += 1
            elif grid[i-1][j] == 'X':
                i -= 1
            else:
                heading = 'E'
        
        elif heading == 'E':
            if grid[i][j+1] == '.':
                j += 1
                ans += 1
            elif grid[i][j+1] == 'X':
                j += 1
            else:
                heading = 'S'
        
        elif heading == 'S':
            if grid[i+1][j] == '.':
                i += 1
                ans += 1
            elif grid[i+1][j] == 'X':
                i += 1
            else:
                heading = 'W'
        
        elif heading == 'W':
            if grid[i][j-1] == '.':
                j -= 1
                ans += 1
            elif grid[i][j-1] == 'X':
                j -= 1
            else:
                heading = 'N'

        if cnt > O:
            return -1
    return ans


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '^':
            x, y = i, j

ans = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        # print(i, j)
        if grid[i][j] == '.' :
            tmp = grid[i][j]
            grid[i][j] = '#'
            if getAnswer(x, y) == -1:
                ans += 1
            grid = [row.copy() for row in gridHardCopy]
print(ans)