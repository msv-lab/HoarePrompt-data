def func_1(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True
s = input().strip()
if func_1(s):
    print('TAK')
else:
    print('NIE')