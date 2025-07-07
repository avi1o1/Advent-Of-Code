with open("Day13/input1.txt", "r") as file:
    data = file.read().splitlines()

ans = 0
for i in range(len(data)//4 + 1):
    A = data[i*4][10:]
    B = data[i*4+1][10:]
    X = data[i*4+2][7:]

    Ax, Ay = [int(ele[1:]) for ele in A.split(", ")]
    Bx, By = [int(ele[1:]) for ele in B.split(", ")]
    Xx, Xy = [int(ele[2:]) for ele in X.split(", ")]

    # Solve for A and B : A*Ax + B*Bx = Xx and A*Ay + B*By = Xy
    # A = (Xx - B*Bx)/Ax
    # A = (Xy - B*By)/Ay
    # (Xx - B*Bx)/Ax = (Xy - B*By)/Ay
    # Ay*(Xx - B*Bx) = Ax*(Xy - B*By)
    # Ay*Xx - Ay*B*Bx = Ax*Xy - Ax*B*By
    # B*(Ay*Bx - Ax*By) = Ay*Xx - Ax*Xy
    # B = (Ay*Xx - Ax*Xy)/(Ay*Bx - Ax*By)
    # Similarly, A = (By*Xx - Bx*Xy)/(By*Ax - Bx*Ay)

    A = (By*Xx - Bx*Xy)/(By*Ax - Bx*Ay)
    B = (Ay*Xx - Ax*Xy)/(Ay*Bx - Ax*By)

    if int(A) == A and int(B) == B:
        ans += 3*A + B

print(int(ans))