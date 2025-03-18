t = int(input())
for i in range(t):
    string = input()
    s = list(string)
    n = len(s)
    done = False
    if n == 1:
        print('NO')
        continue
    x = s[0]
    if x != s[-1]:
        print('YES')
        print(1)
        print(string)
        continue
    if s.count(x) == n:
        print('NO')
        continue
    elif s.count(x) == n - 1:
        if n % 2 == 1 and s[(n - 1) // 2] != x:
            print('NO')
        else:
            print('YES')
            print(1)
            print(string)
        continue
    count = 0
    count2 = 0
    for j in range(n):
        if s[j] != s[n - 1 - j]:
            print('YES')
            print(1)
            print(string)
            done = True
            break
        if s[j] != x and count < 1:
            count = j
            continue
        if count > 0:
            if s[j] != x:
                if count2 < count:
                    print('YES')
                    print(2)
                    print(string[:j], string[j:])
                    done = True
                    break
                elif count2 == count:
                    if count > 1:
                        print('YES')
                        print(2)
                        print(string[:j - 1], string[j - 1:])
                        done = True
                        break
                    else:
                        count2 = 0
                        continue
                elif count2 > count:
                    print('YES')
                    print(2)
                    print(string[:j], string[j:])
                    done = True
                    break
            else:
                count2 += 1
    if not done:
        print('NO')