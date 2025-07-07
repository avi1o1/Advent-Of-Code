from collections import defaultdict

nums = []
with open("Day22/input2.txt") as f:
    for line in f:
        nums.append(int(line.strip()))

data = defaultdict(int)
for num in nums:
    a = b = c = d = 999
    tmp = []
    done = []
    for _ in range(2000-1):
        last = num % 10
        num = ((num<<6) ^ num) % 16777216
        num = ((num>>5) ^ num) % 16777216
        num = ((num * 2048) ^ num) % 16777216
        
        if a == 999:
            a = num%10-last
        elif b == 999:
            b = num%10-last
        elif c == 999:
            c = num%10-last
        elif d == 999:
            d = num%10-last
        else:
            a, b, c, d = b, c, d, num%10-last

            if [a, b, c, d] not in done:
                key = "".join(map(str, [a, b, c, d]))
                data[key] += num%10
                done.append([a, b, c, d])

ans = 0
for ele in data:
    ans = max(ans, data[ele])
print(ans)