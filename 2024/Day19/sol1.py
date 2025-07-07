with open("Day19/input1.txt") as f:
    towels = f.readline()[:-1].split(', ')
    f.readline()
    designs = f.read().splitlines()

memo = {'': True}

def check(design):
    if design in memo:
        return memo[design]
    
    for towel in towels:
        if towel == design[:len(towel)]:
            tmp = check(design[len(towel):])
            if tmp:
                memo[design] = True
                return True
    
    memo[design] = False
    return False

ans = 0
for design in designs:
    if check(design):
        ans += 1
print(ans)