with open("Day19/input2.txt") as f:
    towels = f.readline()[:-1].split(', ')
    f.readline()
    designs = f.read().splitlines()

memo = {'': 1}

def check(design):
    if design in memo:
        return memo[design]
    
    cnt = 0
    for towel in towels:
        if towel == design[:len(towel)]:
            tmp = check(design[len(towel):])
            if tmp != -1:
                cnt += tmp
    
    if cnt == 0:
        memo[design] = -1
        return -1
    memo[design] = cnt
    return cnt

ans = 0
for design in designs:
    tmp = check(design)
    if tmp != -1:
        ans += tmp
print(ans)