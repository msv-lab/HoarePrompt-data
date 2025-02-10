for _ in range(int(input())):
    len = int(input())
    s = list(input())
    ret = 0
    thorn = 0
    for i in s:
        if i == '@':
            thorn = 0
            ret += 1
        elif i == '*':
            thorn += 1
            if thorn == 2:
                break
        else:
            thorn = 0
    print(ret)