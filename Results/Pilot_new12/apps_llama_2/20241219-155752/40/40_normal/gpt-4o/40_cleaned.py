def func_1(s):
    return s == s[::-1]
s = input().strip()
if len(s) <= 1:
    print(0)
elif not func_1(s):
    print(len(s))
elif not func_1(s[1:]):
    print(len(s) - 1)
elif not func_1(s[:-1]):
    print(len(s) - 1)
else:
    print(0)