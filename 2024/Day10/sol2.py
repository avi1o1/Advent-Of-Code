grid = []
with open("Day10/input2.txt") as f:
    for line in f:
        grid.append(list(int(ele) for ele in line.strip()))

N, M = len(grid), len(grid[0])
tmp = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            tmp[i][j] = 10

for i in range(1, 10):
    for j in range(N):
        for k in range(M):
            if grid[j][k] == i:
                if j > 0 and tmp[j-1][k] % 10 == i-1:
                    tmp[j][k] += tmp[j-1][k] // 10
                if j < N-1 and tmp[j+1][k] % 10 == i-1:
                    tmp[j][k] += tmp[j+1][k] // 10
                if k > 0 and tmp[j][k-1] % 10 == i-1:
                    tmp[j][k] += tmp[j][k-1] // 10
                if k < M-1 and tmp[j][k+1] % 10 == i-1:
                    tmp[j][k] += tmp[j][k+1] // 10
                tmp[j][k] = tmp[j][k]*10 + i

ans = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 9:
            ans += tmp[i][j] // 10
print(ans)