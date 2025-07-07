with open("Day9/input1.txt", "r") as file:
    data = list(map(int, file.read()))

ans = idx = 0
f, l = 0, len(data)-1
fVal, lVal = 0, len(data)//2

while f <= l:
    for _ in range(data[f]):
        ans += fVal * idx
        # print(fVal, idx)
        idx += 1
    fVal += 1

    if f < l:
        spaces = data[f+1]
        while spaces > 0 and f < l:
            if data[l] > spaces:
                data[l] -= spaces
                for _ in range(spaces):
                    ans += lVal * idx
                    # print(lVal, idx)
                    idx += 1
                break

            for _ in range(data[l]):
                spaces -= 1
                ans += lVal * idx
                # print(lVal, idx)
                idx += 1
            
            lVal -= 1
            l -= 2
        
    f += 2

print(ans)
