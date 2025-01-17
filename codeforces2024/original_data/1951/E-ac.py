for _ in range(int(input())):
    s = input()
    if s != s[::-1]:
        print('YES\n1')
        print(s)
        continue
    z = -1
    for i in range(len(s)-1,-1,-1):
        if s[i] != s[-1]:
            z = i
            break
    if z == -1:
        print('NO')
        continue
    if s[:z] != s[z-1::-1]:
        print('YES\n2')
        print(s[:z],s[z:])
        continue
    if z == len(s)-2:
        print('NO')
        continue
    if 2*z+1==len(s):
        print('NO')
        continue
    print('YES\n2')
    print(s[:z-1],s[z-1:])