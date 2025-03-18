def func_1(s) -> bool:
    return s == s[::-1]

def func_2():
    s = input()
    (n, x) = (len(s), -1)
    if func_1(s[0:]) == False:
        print('YES')
        print(1)
        print(s)
        return
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
    if x == -1:
        print('NO')
        return
    if func_1(s[x + 1:]) == False:
        print('YES')
        print(2)
        print(s[:x + 1], ' ', s[x + 1:])
    elif x == 1 or x == n // 2:
        print('NO')
    else:
        print('YES')
        print(2)
        print(s[:x + 2], ' ', s[x + 2:])
for _ in range(int(input())):
    func_2()