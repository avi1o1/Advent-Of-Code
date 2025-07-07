grid = []
with open('Day4/input2.txt') as f:
    for line in f:
        grid.append(line.strip())

ans = 0
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
        if grid[i][j] == 'A':
                if (grid[i-1][j-1] == 'M' and grid[i+1][j+1] == 'S') or (grid[i-1][j-1] == 'S' and grid[i+1][j+1] == 'M'):
                    if (grid[i-1][j+1] == 'M' and grid[i+1][j-1] == 'S') or (grid[i-1][j+1] == 'S' and grid[i+1][j-1] == 'M'):
                        ans += 1

print(ans)
