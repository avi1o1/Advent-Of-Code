with open('Day3/input1.txt') as f:
    data = f.read()

ans = tmp = n1 = n2 = 0
for char in data:
    # print(char, tmp, n1, n2)
    if char == 'm':
        tmp = 1
    elif tmp == 1 and char == 'u':
        tmp = 2
    elif tmp == 2 and char == 'l':
        tmp = 3
    elif tmp == 3 and char == '(':
        tmp = 4
    elif (tmp == 4 or tmp == 5) and char in '0123456789':
        n1 = n1 * 10 + int(char)
        tmp = 5
    elif tmp == 5 and char == ',':
        tmp = 6
    elif (tmp == 6 or tmp == 7) and char in '0123456789':
        n2 = n2 * 10 + int(char)
        tmp = 7
    elif tmp == 7 and char == ')':
        # print(n1, n2)
        ans += n1 * n2
        n1 = n2 = tmp = 0
    else:
        n1 = n2 = tmp = 0

print(ans)

    




