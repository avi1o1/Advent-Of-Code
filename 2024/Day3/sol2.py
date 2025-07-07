with open('Day3/input2.txt') as f:
    data = f.read()

ans = check = kcehc = dont = tmp = n1 = n2 = 0
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
        if dont == 0:
            # print(n1, n2)
            ans += n1 * n2
        n1 = n2 = tmp = 0
    else:
        n1 = n2 = tmp = 0
    
    # print(char, dont)
    if char == 'd':
        check = 1
    elif check == 1 and char == 'o':
        check = 2
    elif check == 2 and char == 'n':
        check = 3
    elif check == 3 and char == "'":
        check = 4
    elif check == 4 and char == 't':
        check = 5
    elif check == 5 and char == '(':
        check = 6
    elif check == 6 and char == ')':
        dont = 1
    else:
        check = 0
    
    if char == 'd':
        kcehc = 1
    elif kcehc == 1 and char == 'o':
        kcehc = 2
    elif kcehc == 2 and char == '(':
        kcehc = 3
    elif kcehc == 3 and char == ')':
        dont = 0
    else:
        kcehc = 0

print(ans)

    




