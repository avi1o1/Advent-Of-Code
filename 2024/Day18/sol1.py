grid = [[9999]*71 for _ in range(71)]
with open("Day18/input1.txt") as f:
    for _ in range(1024):
        x, y = map(int, f.readline().split(','))
        grid[x][y] = -1

grid[0][0] = 0
queue = [(0, 0)]
while queue:
    x, y = queue.pop(0)
    
    if x > 0 and grid[x-1][y] != -1 and grid[x-1][y] > grid[x][y] + 1:
        grid[x-1][y] = grid[x][y] + 1
        queue.append((x-1, y))
    if y > 0 and grid[x][y-1] != -1 and grid[x][y-1] > grid[x][y] + 1:
        grid[x][y-1] = grid[x][y] + 1
        queue.append((x, y-1))
    if x < 70 and grid[x+1][y] != -1 and grid[x+1][y] > grid[x][y] + 1:
        grid[x+1][y] = grid[x][y] + 1
        queue.append((x+1, y))
    if y < 70 and grid[x][y+1] != -1 and grid[x][y+1] > grid[x][y] + 1:
        grid[x][y+1] = grid[x][y] + 1
        queue.append((x, y+1))

print(grid[70][70])
