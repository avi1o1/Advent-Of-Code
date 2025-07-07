X, Y = 101, 103
T = 100

a, b, c, d = 0, 0, 0, 0
with open("Day14/input1.txt", "r") as file:
    for line in file:
        tmp = line.split(" v=")
        px, py = [int(ele) for ele in tmp[0][2:].split(',')]
        vx, vy = [int(ele) for ele in tmp[1][:-1].split(',')]

        posX, posY = (px + T*vx)%X, (py + T*vy)%Y
        if posX < X // 2 and posY < Y // 2:
            a += 1
        elif posX < X // 2 and posY > Y // 2:
            b += 1
        elif posX > X // 2 and posY < Y // 2:
            c += 1
        elif posX > X // 2 and posY > Y // 2:
            d += 1

# print(a, b, c, d)
print(a*b*c*d)