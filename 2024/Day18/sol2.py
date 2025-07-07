grid = [[9999]*71 for _ in range(71)]
rem = []
with open("Day18/input2.txt") as f:
    for _ in range(1024):
        x, y = map(int, f.readline().split(','))
        grid[x][y] = -1
    
    while True:
        line = f.readline()
        if not line:
            break
        rem.append(tuple(map(int, line.split(','))))

def checkPath():
    tmp = [[9999]*71 for _ in range(71)]
    tmp[0][0] = 0
    queue = [(0, 0)]
    while queue:
        x, y = queue.pop(0)
        
        if x > 0 and grid[x-1][y] != -1 and tmp[x-1][y] > tmp[x][y] + 1:
            tmp[x-1][y] = tmp[x][y] + 1
            queue.append((x-1, y))
        if x < 70 and grid[x+1][y] != -1 and tmp[x+1][y] > tmp[x][y] + 1:
            tmp[x+1][y] = tmp[x][y] + 1
            queue.append((x+1, y))
        if y > 0 and grid[x][y-1] != -1 and tmp[x][y-1] > tmp[x][y] + 1:
            tmp[x][y-1] = tmp[x][y] + 1
            queue.append((x, y-1))
        if y < 70 and grid[x][y+1] != -1 and tmp[x][y+1] > tmp[x][y] + 1:
            tmp[x][y+1] = tmp[x][y] + 1
            queue.append((x, y+1))
    
    if tmp[70][70] == 9999 or tmp[70][70] == -1:
        return True
    return False

for x, y in rem:
    grid[x][y] = -1
    
    if checkPath():
        print(x, y)
        break
