with open("Day11/input1.txt", "r") as file:
    data = file.read().split()

def blink(data):
    tmp = []
    for ele in data:
        if ele == '0':
            tmp.append('1')
        elif len(ele) % 2:
            tmp.append(str(int(ele) * 2024))
        else:
            tmp.append(ele[:len(ele)//2])
            tmp.append(str(int(ele[len(ele)//2:])))
    return tmp

for _ in range(25):
    data = blink(data)
    # print(data)

print(len(data))