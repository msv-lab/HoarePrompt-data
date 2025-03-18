def func_1(ch):
    if len(ch) % 2 == 0:
        x = len(ch) // 2
    else:
        x = len(ch) // 2 + 1
    if ch[:len(ch) // 2] == ch[x:][::-1]:
        return True
    else:
        return False

def func_2(ch):
    b = len(ch) // 2
    if len(ch) % 2 == 0:
        if func_1(ch[:b]):
            a = 3
        else:
            a = 4
    elif func_1(ch[:b]):
        a = 1
    else:
        a = 2
    return a
t = int(input())
for _ in range(t):
    s = input()
    T1 = True
    T2 = True
    a = 0
    x = 2
    if s == s[0] * len(s):
        T1 = False
    elif len(s) > 2 and s == s[:2] * (len(s) // 2) + s[0]:
        T1 = False
    if T1 and func_1(s):
        if len(s) > 3:
            a = func_2(s)
        else:
            T1 = False
    if T1:
        if a == 0:
            s = [s]
            x = 1
        elif a == 1:
            z = len(s) // 2 + 1
            if s[z + 1:] == s[z + 1] * len(s[z + 1:]):
                T1 = False
            else:
                s = [s[:z + 1], s[z + 1:]]
        elif a == 2:
            z = len(s) // 2 + 1
            for k in range(len(s) // 2):
                if not (func_1(s[z + k:]) or func_1(s[:z + k])):
                    s = [s[:z + k], s[z + k:]]
                    T2 = False
                    break
            if T2:
                T1 = False
        elif a == 3:
            z = len(s) // 2
            s = [s[:z + 1], s[z + 1:]]
        else:
            z = len(s) // 2
            s = [s[:z], s[z:]]
        if T1:
            print('YES')
            print(x)
            print(' '.join(s))
        else:
            print('NO')
    else:
        print('NO')