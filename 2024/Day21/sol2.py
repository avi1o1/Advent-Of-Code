from collections import defaultdict

paths1 = {
    'A': [('<', '0'), ('^', '3')],
    '0': [('^', '2'), ('>', 'A')],
    '1': [('>', '2'), ('^', '4')],
    '2': [('^', '5'), ('>', '3'), ('<', '1'), ('v', '0')],
    '3': [('^', '6'), ('<', '2'), ('v', 'A')],
    '4': [('^', '7'), ('>', '5'), ('v', '1')],
    '5': [('^', '8'), ('>', '6'), ('<', '4'), ('v', '2')],
    '6': [('^', '9'), ('<', '5'), ('v', '3')],
    '7': [('>', '8'), ('v', '4')],
    '8': [('>', '9'), ('<', '7'), ('v', '5')],
    '9': [('v', '6'), ('<', '8')]
}

paths2 = {
    'A': [('<', '^'), ('v', '>')],
    '^': [('>', 'A'), ('v', 'v')],
    'v': [('>', '>'), ('<', '<'), ('^', '^')],
    '<': [('>', 'v')],
    '>': [('<', 'v'), ('^', 'A')]
}

def firstKeypad(code, currPos):
    
    if code == currPos:
        return [""]
    
    queue = [(currPos, code, "")]
    visited = defaultdict(int)
    ans = []

    while queue:
        currPos, code, tmp = queue.pop(0)
        if code == '':
            ans.append(tmp)
            continue

        if visited[currPos] < 4:
            visited[currPos] += 1
            for path in paths1[currPos]:
                if path[1] == code[0]:
                    queue.append((path[1], code[1:], tmp+path[0]))
                else:
                    queue.append((path[1], code, tmp+path[0]))
    
    minLen = min(len(ele) for ele in ans)
    ans = [ele for ele in ans if len(ele) == minLen]
    return ans


memo = {}
def otherKeypad(code, currPos):
    k = code+currPos
    if k in memo:
        return memo[k]

    if code == currPos:
        return [""]
    
    queue = [(currPos, code, "")]
    visited = defaultdict(int)
    ans = []

    while queue:
        currPos, code, tmp = queue.pop(0)
        if code == '':
            ans.append(tmp)
            continue

        if visited[currPos] < 2:
            visited[currPos] += 1
            for path in paths2[currPos]:
                if path[1] == code[0]:
                    queue.append((path[1], code[1:], tmp+path[0]))
                else:
                    queue.append((path[1], code, tmp+path[0]))
    
    minLen = min(len(ele) for ele in ans)
    ans = [ele for ele in ans if len(ele) == minLen]
    memo[k] = ans
    return ans

with open("Day21/input1.txt", "r") as file:
    codes = file.read().splitlines()

ans = 0
for code in codes:
    start = "A"
    ans1 = [""]
    for letter in code:
        x = firstKeypad(letter, start)
        start = letter
        ans1 = [ele1+ele2+"A" for ele1 in ans1 for ele2 in x]

    results = ans1
    for i in range(2):
        new_results = []
        for each in results:
            start = "A"
            tmp = [""]
            for letter in each:
                x = otherKeypad(letter, start)
                start = letter
                tmp = [ele1+ele2+"A" for ele1 in tmp for ele2 in x]
            new_results.extend(tmp)
        results = new_results

    min_len = min(len(ele) for ele in results)
    ans += min_len * int(code[:-1])
print(ans)