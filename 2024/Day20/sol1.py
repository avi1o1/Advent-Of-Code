from collections import defaultdict

grid = []
with open("Day20/input1.txt", "r") as file:
    for line in file:
        grid.append(list(line.strip()))


used, none = [], []
def findPath(x, y, cheats, cost):
    if grid[x][y] == "X":
        return
    
    if grid[x][y] == "#":
        if cheats == 0:
            return
        cheats -= 1
    elif cheats == 1:
        cheats = 0
    
    if grid[x][y] == "E":
        if cheats == 0:
            used.append(cost)
        else:
            none.append(cost)
        
        print(cost)
        for row in grid:
            print("".join(row))
        print()
        return
    
    tmp = grid[x][y]
    grid[x][y] = "X"
    if x > 0:
        findPath(x-1, y, cheats, cost+1)
    if y > 0:
        findPath(x, y-1, cheats, cost+1)
    if x < len(grid)-1:
        findPath(x+1, y, cheats, cost+1)
    if y < len(grid[0])-1: 
        findPath(x, y+1, cheats, cost+1)
    grid[x][y] = tmp
    return

saves = defaultdict(int)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            findPath(i, j, 2, 0)

            print(none)
            print(used)

            comp = min(none)
            for ele in used:
                if comp-ele > 0:
                    saves[comp-ele] += 1

            for save in saves:
                print(save, saves[save])
                
            exit()