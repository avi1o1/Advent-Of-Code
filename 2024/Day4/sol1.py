grid = []
with open('Day4/input1.txt') as f:
    for line in f:
        grid.append(line.strip())

ans = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'X':
            # Check Rows/Columns
            if j > 2 and grid[i][j-1] == 'M' and grid[i][j-2] == 'A' and grid[i][j-3] == 'S':
                ans += 1
            if i > 2 and grid[i-1][j] == 'M' and grid[i-2][j] == 'A' and grid[i-3][j] == 'S':
                ans += 1
            if i < len(grid)-3 and grid[i+1][j] == 'M' and grid[i+2][j] == 'A' and grid[i+3][j] == 'S':
                ans += 1
            if j < len(grid[0])-3 and grid[i][j+1] == 'M' and grid[i][j+2] == 'A' and grid[i][j+3] == 'S':
                ans += 1

            # Check Diagonals
            if i > 2 and j > 2 and grid[i-1][j-1] == 'M' and grid[i-2][j-2] == 'A' and grid[i-3][j-3] == 'S':
                ans += 1
            if i > 2 and j < len(grid[0])-3 and grid[i-1][j+1] == 'M' and grid[i-2][j+2] == 'A' and grid[i-3][j+3] == 'S':
                ans += 1
            if i < len(grid)-3 and j > 2 and grid[i+1][j-1] == 'M' and grid[i+2][j-2] == 'A' and grid[i+3][j-3] == 'S':
                ans += 1
            if i < len(grid)-3 and j < len(grid[0])-3 and grid[i+1][j+1] == 'M' and grid[i+2][j+2] == 'A' and grid[i+3][j+3] == 'S':
                ans += 1

print(ans)
