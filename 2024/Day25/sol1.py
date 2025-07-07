locks, keys = [], []
with open("Day25/input1.txt", 'r') as f:
    data = f.readline().strip()
    while data:
        lock = 1
        if data[0] == '.':
            lock = 0
        
        tmp = [0] * len(data)
        for _ in range(7):
            for i in range(len(data)):
                if data[i] == '#':
                    tmp[i] += 1
            data = f.readline().strip()
        
        if lock:
            locks.append(tmp)
        else:
            keys.append(tmp)
        
        data = f.readline().strip()

ans = 0
for l in locks:
    for k in keys:
        flag = 1
        for i in range(len(l)):
            if l[i] + k[i] > 7:
                flag = 0
                break
        
        if flag:
            ans += 1
print(ans)
