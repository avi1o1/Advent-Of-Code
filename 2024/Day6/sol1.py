grid = []
with open("Day6/input1.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        tmp = [char for char in line]
        grid.append(tmp[:-1])

def getAnswer(i, j):
    heading = 'N'
    ans = 1

    N, M = len(grid)-1, len(grid[0])-1
    while i > 0 and j > 0 and i < N and j < M:
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
    
    # for row in grid:
    #     print(row)
    return ans


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '^':
            print(getAnswer(i, j))
            exit()