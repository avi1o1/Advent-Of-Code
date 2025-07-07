with open("Day13/input2.txt", "r") as file:
    data = file.read().splitlines()

ans = 0
for i in range(len(data)//4 + 1):
    A = data[i*4][10:]
    B = data[i*4+1][10:]
    X = data[i*4+2][7:]

    Ax, Ay = [int(ele[1:]) for ele in A.split(", ")]
    Bx, By = [int(ele[1:]) for ele in B.split(", ")]
    Xx, Xy = [int(ele[2:])+10000000000000 for ele in X.split(", ")]

    A = (By*Xx - Bx*Xy)/(By*Ax - Bx*Ay)
    B = (Ay*Xx - Ax*Xy)/(Ay*Bx - Ax*By)

    if int(A) == A and int(B) == B:
        ans += 3*A + B

print(int(ans))