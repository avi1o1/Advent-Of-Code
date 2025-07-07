# Needed hint for dictionary

from collections import defaultdict

with open("Day11/input2.txt", "r") as file:
    tmp = file.read().split()

data = defaultdict(int)
for ele in tmp:
    data[ele] += 1

def blink(data):
    tmp = defaultdict(int)
    for ele in data:
        if ele == '0':
            tmp['1'] += data[ele]
        elif len(ele) % 2:
            tmp[str(int(ele) * 2024)] += data[ele]
        else:
            tmp[ele[:len(ele)//2]] += data[ele]
            tmp[str(int(ele[len(ele)//2:]))] += data[ele]
    return tmp

for _ in range(75):
    data = blink(data)

ans = 0
for ele in data:
    ans += data[ele]
print(ans)