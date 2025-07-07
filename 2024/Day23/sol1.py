graph = {}
with open("Day23/input1.txt") as file:
    for line in file:
        a, b = line.strip().split('-')
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

# print(graph)
sets = set()
for node in graph:
    if node[0] == 't':
        for n1 in graph[node]:
            for n2 in graph[node]:
                if n2 in graph[n1] and n1 in graph[n2]:
                    tmp = {node, n1, n2}
                    sets.add(frozenset(tmp))

# print(sets)
print(len(sets))
