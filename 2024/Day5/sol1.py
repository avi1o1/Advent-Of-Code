dat = {}
ans = 0
with open("Day5/input1.txt") as f:
    for line in f:
        if '|' in line:
            line = line[:-1].split('|')
            if int(line[0]) not in dat:
                dat[int(line[0])] = [int(line[1])]
            else:
                dat[int(line[0])].append(int(line[1]))
            if int(line[1]) not in dat:
                dat[int(line[1])] = []
        
        elif line == '\n':
            continue
        
        else:
            arr = [int(ele) for ele in line.split(',')]

            isIt = 1
            for i in range(len(arr)):
                for j in range(i):
                    if arr[j] in dat[arr[i]]:
                        isIt = 0
            
            if isIt == 1:
                # print(arr)
                ans += arr[len(arr)//2]

print(ans)