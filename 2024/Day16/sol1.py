grid = []
with open("Day16/input1.txt") as file:
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

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "E":
                return visited[i][j]

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            print(bfs(i, j))
            break