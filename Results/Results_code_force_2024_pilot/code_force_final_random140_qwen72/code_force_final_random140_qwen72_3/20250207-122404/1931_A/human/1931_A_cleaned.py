def func_1(num):
    if 1 <= num <= 26:
        return chr(num + 96)
t = int(input())
for _ in range(t):
    n = int(input())
    a = ''
    b = ''
    c = ''
    if n // 26 == 0:
        a = chr(96 + 1)
        b = chr(96 + 1)
        c = chr(96 + (n - 2))
    elif n // 26 == 1:
        a = chr(96 + 1)
        b = chr(96 + (n - 27))
        c = chr(96 + 26)
    elif n // 26 == 2:
        a = chr(96 + (n - 52))
        b = chr(96 + 26)
        c = chr(96 + 26)
    print(a + '' + b + '' + c)