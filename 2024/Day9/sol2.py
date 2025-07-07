from collections import defaultdict

with open("Day9/input2.txt", "r") as file:
    data = list(map(int, file.read()))

presum = [0]*len(data)
for i in range(1, len(data)):
    presum[i] = presum[i-1] + data[i-1]

f, l = 0, len(data)-1
moved = defaultdict(list)
for i in range(len(data)-1, -1, -2):
    for j in range(1, i, 2):
        if data[j] >= data[i]:
            moved[j].append((i//2, data[i]))
            data[j] -= data[i]
            data[i] = 0
            break

ans = 0
for i in range(0, len(data), 2):
    for j in range(presum[i], presum[i]+data[i]):
        ans += i//2 * j

for i in moved:
    idx = presum[i]
    for j, k in moved[i]:
        for l in range(idx, idx+k):
            ans += j * l
        idx += k

print(ans)