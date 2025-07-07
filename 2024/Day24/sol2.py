values = {}
find = {}
toDo = []
with open("Day24/input2.txt") as file:
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

print(find)

class TreeNode:
    def __init__(self, left, right, op, val):
        self.left = left
        self.right = right
        self.op = op
        self.value = val

def buildTree(node):
    if node in values:
        return TreeNode(None, None, None, values[node])

    left = buildTree(find[node][0])
    right = buildTree(find[node][2])

    if find[node][1] == "AND":
        newNode = TreeNode(left, right, find[node][1], left.value & right.value)
    elif find[node][1] == "OR":
        newNode = TreeNode(left, right, find[node][1], left.value | right.value)
    else:
        newNode = TreeNode(left, right, find[node][1], left.value ^ right.value)
    return newNode

ans = ""
for i in range(45):
    tmp = buildTree(f"z{str(i+1).zfill(2)}")
    print(tmp.value)
    ans += str(tmp.value)
print(int(ans, 2))