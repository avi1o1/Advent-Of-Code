grid = []
with open("Day16/input2.txt") as file:
    for line in file:
        grid.append(list(line.strip()))

def bfs(x, y):
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    queue = [(x, y, 0, 'R')]
    visited = [[-1]*len(grid[0]) for _ in range(len(grid))]
    visited[x][y] = 0

    while queue:
        x, y, steps, dir = queue.pop(0)

        for d, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != "#":
                new_steps = steps + 1
                if d != dir:
                    new_steps += 1000

                if visited[nx][ny] == -1 or visited[nx][ny] > new_steps:
                    visited[nx][ny] = new_steps
                    queue.append((nx, ny, new_steps, d))

    for i in range(1, len(visited)-1):
        for j in range(1, len(visited[i])-1):
            if visited[i][j] != -1:
                cnt = 0
                val = visited[i][j]
                if visited[i-1][j] != -1:
                    cnt += 1
                    val = min(val, visited[i-1][j])
                if visited[i+1][j] != -1:
                    cnt += 1
                    val = min(val, visited[i+1][j])
                if visited[i][j-1] != -1:
                    cnt += 1
                    val = min(val, visited[i][j-1])
                if visited[i][j+1] != -1:
                    cnt += 1
                    val = min(val, visited[i][j+1])
                
                if cnt > 2:
                    visited[i][j] = val+1001

    return visited

def countPos(arr):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "E":
                endX, endY = i, j
    count = 0
    queue = [(endX, endY)]

    while queue:
        x, y = queue.pop(0)
        flag = 0
        if x-1 > 0 and (arr[x-1][y] == arr[x][y]-1 or arr[x-1][y] == arr[x][y]-1001):
            count += 1
            flag = 1
            queue.append((x-1, y))
        if x+1 < len(grid) and (arr[x+1][y] == arr[x][y]-1 or arr[x+1][y] == arr[x][y]-1001):
            count += 1
            flag = 1
            queue.append((x+1, y))
        if y-1 > 0 and (arr[x][y-1] == arr[x][y]-1 or arr[x][y-1] == arr[x][y]-1001):
            count += 1
            flag = 1
            queue.append((x, y-1))
        if y+1 < len(grid[0]) and (arr[x][y+1] == arr[x][y]-1 or arr[x][y+1] == arr[x][y]-1001):
            count += 1
            flag = 1
            queue.append((x, y+1))
        
        if flag:
            arr[x][y] = 0

    for row in arr:
        print(" ".join(f"{elem:5}" for elem in row))

    print(count)
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                count += 1
    
    return count

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            tmp = bfs(i, j)
            print(countPos(tmp))
            exit()