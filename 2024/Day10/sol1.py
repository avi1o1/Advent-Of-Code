grid = []
with open("Day10/input1.txt") as f:
    for line in f:
        grid.append([int(ele) if ele != '.' else -1 for ele in line.strip()])

N, M = len(grid), len(grid[0])

def checkCount(x, y):
    tmp = [[0]*M for _ in range(N)]
    tmp[x][y] = 1
    for i in range(1, 10):
        for j in range(N):
            for k in range(M):
                if j > 0 and tmp[j-1][k] == i and grid[j][k] == i:
                    tmp[j][k] = i+1
                if j < N-1 and tmp[j+1][k] == i and grid[j][k] == i:
                    tmp[j][k] = i+1
                if k > 0 and tmp[j][k-1] == i and grid[j][k] == i:
                    tmp[j][k] = i+1
                if k < M-1 and tmp[j][k+1] == i and grid[j][k] == i:
                    tmp[j][k] = i+1
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 9 and tmp[i][j] > 0:
                cnt += 1
    return cnt

ans = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            ans += checkCount(i, j)
print(ans)
