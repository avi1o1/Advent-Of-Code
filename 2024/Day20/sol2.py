from collections import defaultdict

grid = []
with open("Day20/input1.txt", "r") as file:
    for line in file:
        grid.append(list(line.strip()))


one, two, none = [], [], []
def findPath(x, y, cheats, cost):
    if grid[x][y] == "X":
        return
    
    if grid[x][y] == "#":
        if cheats == 0:
            return
        cheats -= 1
    
    if grid[x][y] == "E":
        if cheats == 0:
            two.append(cost)
        elif cheats == 1:
            one.append(cost)
        else:
            none.append(cost)
    
    tmp = grid[x][y]
    grid[x][y] = "X"
    if x > 0 and (x-1, y):
        findPath(x-1, y, cheats, cost+1)
    if y > 0 and (x, y-1):
        findPath(x, y-1, cheats, cost+1)
    if x < len(grid)-1 and (x+1, y):
        findPath(x+1, y, cheats, cost+1)
    if y < len(grid[x])-1 and (x, y+1):
        findPath(x, y+1, cheats, cost+1)
    grid[x][y] = tmp
    return

saves = defaultdict(int)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            findPath(i, j, 2, 0)
            print(none)
            print(one)
            print(two)

            comp = min(none)
            for ele in one:
                saves[comp-ele] += 1
            for ele in two:
                saves[comp-ele] += 1

            for save in saves:
                print(save, saves[save])
                
            exit()