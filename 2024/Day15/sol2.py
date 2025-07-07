grid = []
with open("Day15/input2.txt", "r") as file:
    x = file.readline()[:-1]
    while x != "":
        tmp = []
        for ele in x:
            if ele  == '.':
                tmp.append('.')
                tmp.append('.')
            elif ele == '#':
                tmp.append('#')
                tmp.append('#')
            elif ele == 'O':
                tmp.append('[')
                tmp.append(']')
            else:
                tmp.append('@')
                tmp.append('.')
        grid.append(tmp)
        x = file.readline()[:-1]
    
    moves = "".join([ele[:-1] for ele in file.readlines()])

for row in grid:
    print("".join(row))

# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if grid[i][j] == "@":
#             x, y = j, i

# for move in moves:
#     if move == '^':
#         tmpY = y-1
#         while grid[tmpY][x] == "O":
#             tmpY -= 1
#         if grid[tmpY][x] == "#":
#             continue
#         else:
#             while grid[tmpY][x] != '@':
#                 grid[tmpY][x] = "O"
#                 tmpY += 1
#             grid[tmpY][x] = "."
#             y = tmpY-1
#             grid[y][x] = "@"
    
#     elif move == 'v':
#         tmpY = y+1
#         while grid[tmpY][x] == "O":
#             tmpY += 1
#         if grid[tmpY][x] == "#":
#             continue
#         else:
#             while grid[tmpY][x] != '@':
#                 grid[tmpY][x] = "O"
#                 tmpY -= 1
#             grid[tmpY][x] = "."
#             y = tmpY+1
#             grid[y][x] = "@"
    
#     elif move == '<':
#         tmpX = x-1
#         while grid[y][tmpX] == "O":
#             tmpX -= 1

#         if grid[y][tmpX] == "#":
#             continue
#         else:
#             while grid[y][tmpX] != '@':
#                 grid[y][tmpX] = "O"
#                 tmpX += 1
#             grid[y][tmpX] = "."
#             x = tmpX-1
#             grid[y][x] = "@"
        
#     elif move == '>':
#         tmpX = x+1
#         while grid[y][tmpX] == "O":
#             tmpX += 1
#         if grid[y][tmpX] == "#":
#             continue
#         else:
#             while grid[y][tmpX] != '@':
#                 grid[y][tmpX] = "O"
#                 tmpX -= 1
#             grid[y][tmpX] = "."
#             x = tmpX+1
#             grid[y][x] = "@"

# # for row in grid:
# #     print("".join(row))

# ans = 0
# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if grid[i][j] == "O":
#             ans += 100*i + j
# print(ans)
