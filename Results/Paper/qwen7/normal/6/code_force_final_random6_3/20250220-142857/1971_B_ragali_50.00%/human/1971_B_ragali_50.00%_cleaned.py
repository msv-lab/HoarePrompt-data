t = int(input().strip(' '))
for i in range(t):
    s = input().strip(' ')
    a = set()
    for i in s:
        a.add(i)
    if len(a) > 1:
        print('YES')
        newstr = s[len(s) // 2:] + s[:len(s) // 2]
        isreverse = s[::-1]
        if newstr != s:
            print(s[len(s) // 2:] + s[:len(s) // 2])
        elif isreverse != s:
            print(isreverse)
        else:
            print(s[len(s) // 2:] + s[0:len(s) // 2])
    else:
        print('NO')