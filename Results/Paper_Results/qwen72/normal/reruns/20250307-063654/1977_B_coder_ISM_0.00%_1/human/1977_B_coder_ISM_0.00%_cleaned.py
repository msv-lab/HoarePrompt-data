t = int(input())
for nalla in range(t):
    x = int(input())
    s = []
    length = 30
    for i in range(30):
        if x & pow(2, i):
            s.append('1')
        else:
            s.append('0')
    print(*s)
    flag = 0
    for i in range(0, 29):
        if flag and s[i] == '0':
            s[i] = '1'
            flag = 0
        if flag == 0 and s[i] == s[i + 1] and (s[i] == '1'):
            s[i] = '-1'
            flag = 1
        elif flag == 1:
            s[i] = '0'
        else:
            pass
    if flag and s[29] == '0':
        s[29] = '1'
    elif flag:
        s[29] = '0'
        s.append('1')
        length += 1
    for i in range(1, length):
        if (s[i] == '-1') & (s[i - 1] == '1'):
            s[i] = '0'
            s[i - 1] = '-1'
    print(length)
    print(*s)