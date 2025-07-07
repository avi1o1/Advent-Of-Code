X, Y = 101, 103

bots = []
with open("Day14/input2.txt", "r") as file:
    for line in file:
        tmp = line.split(" v=")
        px, py = [int(ele) for ele in tmp[0][2:].split(',')]
        vx, vy = [int(ele) for ele in tmp[1][:-1].split(',')]
        bots.append((px, py, vx, vy))

with open("Day14/output.txt", "w") as file:
    for t in range(167, 10000, 101):
        print("Time: ", t, file=file)
        grid = [['.']*X for _ in range(Y)]
        for bot in bots:
            px, py, vx, vy = bot
            posX, posY = (px + t*vx)%X, (py + t*vy)%Y
            grid[posY][posX] = '#'
        
        for row in grid:
            for char in row:
                print(char, end='', file=file)
            print(file=file)
        print(file=file)

# 7338