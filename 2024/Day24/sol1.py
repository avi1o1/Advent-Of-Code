values = {}
find = {}
toDo = []
with open("Day24/input1.txt") as file:
    data = file.readline()
    while data != "\n":
        k, v = data.strip().split(": ")
        values[k] = int(v)
        data = file.readline()
    
    while data:
        data = file.readline()
        if data:
            l, r = data.strip().split(" -> ")
            find[r] = l.split(" ")
            toDo.append(r)

while len(toDo) > 0:
    for pairs in toDo:
        if find[pairs][0] in values and find[pairs][2] in values:
            if find[pairs][1] == "AND":
                values[pairs] = values[find[pairs][0]] & values[find[pairs][2]]
            elif find[pairs][1] == "OR":
                values[pairs] = values[find[pairs][0]] | values[find[pairs][2]]
            else:
                values[pairs] = values[find[pairs][0]] ^ values[find[pairs][2]]
            toDo.remove(pairs)

ans = ''
for val in sorted(values):
    if val[0] == 'z':
        ans = str(values[val]) + ans
print(int(ans, 2))