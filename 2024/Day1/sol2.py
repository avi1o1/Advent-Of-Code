from collections import defaultdict

left, right = defaultdict(int), defaultdict(int)

with open("Day1/input2.txt", "r") as f:
    data = f.read().splitlines()
    for pair in data:
        start, end = pair.split('  ')
        left[int(start)] += 1
        right[int(end)] += 1

ans = 0
for ele in left:
    print(ele, left[ele], right[ele])
    ans += left[ele] * right[ele] * ele
print(ans)