nums = []
with open("Day22/input1.txt") as f:
    for line in f:
        nums.append(int(line.strip()))

ans = 0
for num in nums:
    for _ in range(2000):
        num = ((num<<6) ^ num) % 16777216
        num = ((num>>5) ^ num) % 16777216
        num = ((num * 2048) ^ num) % 16777216
    ans += num
print(ans)