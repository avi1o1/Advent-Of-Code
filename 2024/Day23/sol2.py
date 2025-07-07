graph = {}
verts = set()
with open("Day23/input2.txt") as file:
    for line in file:
        a, b = line.strip().split('-')
        if a not in graph:
            graph[a] = []
            verts.add(a)
        if b not in graph:
            graph[b] = []
            verts.add(b)
        graph[a].append(b)
        graph[b].append(a)

memo = {}
def findSCC(curr, rem):
    if "".join(sorted(curr)) in memo:
        return memo["".join(sorted(curr))]

    ans = ""
    for i in range(len(rem)):
        flag = 1
        for c in curr:
            if rem[i] not in graph[c]:
                flag = 0
                break
        
        if flag:
            tmp = findSCC(curr + [rem[i]], rem[i+1:])
            if len(tmp) > len(ans):
                ans = tmp
    
    if ans == "":
        ans = ",".join(sorted(curr))
    
    memo["".join(sorted(curr))] = ans
    return ans


ans = ""
for v in verts:
    tmp = findSCC([v], list(verts - {v}))
    if len(tmp) > len(ans):
        ans = tmp
print(ans)
