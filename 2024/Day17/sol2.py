"""
Lets start with A
2, 4 -> B = combo(4) % 8 = A%8
1, 1 -> B = B^1 = (A%8)^1
7, 5 -> C = A//(2**combo(5)) = A//(2**B) = A//(2**((A%8)^1))
1, 5 -> B = B^5 = (A%8)^1^5 = (A%8)^4
4, 2 -> B = B^C = ((A%8)^4)^(A//(2**((A%8)^1)))
5, 5 -> output=(combo(5) % 8) = output=((((A%8)^4)^(A//(2**((A%8)^1))))%8)
0, 3 -> A = A//(2**combo(3)) = A//8
3, 0 -> if A!=0: repeat from start

Thus, in each loop,
A = A//8
output -> (((A%8)^4)^(A//(2**((A%8)^1))))%8 = ((A^4)^(A//(2**(A^1))))%8 = ((A^4)^(A//2^(A^1)))%8
"""
# Now, since output should be 2,4,1,1,7,5,1,5,4,2,5,5,0,3,3,0
# (((A%8)^4)^(A//(2**((A%8)^1))))%8 == 2
# A //= 8
# (((A%8)^4)^(A//(2**((A%8)^1))))%8 == 4
# A //= 8
# (((A%8)^4)^(A//(2**((A%8)^1))))%8 == 1
# ...
# ...
# ...
# (((A%8)^4)^(A//(2**((A%8)^1))))%8 == 3
# A //= 8
# (((A%8)^4)^(A//(2**((A%8)^1))))%8 == 0
# A //= 8
# A == 0

with open("Day17/input2.txt", "r") as file:
    A = int(file.readline().split()[-1])
    B = int(file.readline().split()[-1])
    C = int(file.readline().split()[-1])
    file.readline()
    ops = [int(ele) for ele in file.readline()[9:].split(",")]

def check(A, tmp):
    print(A, tmp)
    if tmp == []:
        return A
    
    ans = 999999999999999999
    A *= 8
    for _ in range(8):
        if (((A%8)^4)^(A//(2**((A%8)^1))))%8 == tmp[0]:
            x = check(A, tmp[1:])
            if x != -1:
                ans = min(ans, x)
        A += 1
    
    if ans == 999999999999999999:
        return -1
    return ans

print(check(0, ops))

# 14680
# 1835
# 229
# 28
# 3