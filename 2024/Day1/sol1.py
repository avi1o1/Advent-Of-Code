left, right = [], []

with open("Day1/input1.txt", "r") as f:
    data = f.read().splitlines()
    for pair in data:
        start, end = pair.split('  ')
        left.append(int(start))
        right.append(int(end))

left.sort()
right.sort()
ans = 0
for i in range(len(left)):
    if left[i] < right[i]:
        ans += right[i] - left[i]
    else:
        ans += left[i] - right[i]
print(ans)