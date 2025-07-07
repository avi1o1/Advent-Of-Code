with open("Day17/input1.txt", "r") as file:
    A = int(file.readline().split()[-1])
    B = int(file.readline().split()[-1])
    C = int(file.readline().split()[-1])
    file.readline()
    ops = [int(ele) for ele in file.readline()[9:].split(",")]

def combo(val):
    if val < 4:
        return val
    elif val == 4:
        return A
    elif val == 5:
        return B
    elif val == 6:
        return C
    else:
        return -1

idx = 0
output = []
while idx < len(ops):
    if ops[idx] == 0:
        A //= (2**combo(ops[idx+1]))
    elif ops[idx] == 1:
        B ^= ops[idx+1]
    elif ops[idx] == 2:
        B = combo(ops[idx+1]) % 8
    elif ops[idx] == 3:
        if A != 0:
            print(A)
            idx = ops[idx+1]
            continue
    elif ops[idx] == 4:
        B ^= C
    elif ops[idx] == 5:
        output.append(str(combo(ops[idx+1]) % 8))
    elif ops[idx] == 6:
        B = A // (2**combo(ops[idx+1]))
    elif ops[idx] == 7:
        C = A // (2**combo(ops[idx+1]))
    idx += 2

print(",".join(output))
    
