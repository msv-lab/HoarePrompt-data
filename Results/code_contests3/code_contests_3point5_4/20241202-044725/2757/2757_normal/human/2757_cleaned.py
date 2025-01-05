def func_1(ch):
    return not ch in 'aeiou'
s = raw_input()
n = len(s)
i = 0
while i < n - 2:
    if func_1(s[i]) and func_1(s[i + 1]) and func_1(s[i + 2]) and (s[i] != s[i + 1] or s[i + 1] != s[i + 2]):
        sys.stdout.write(s[i] + '' + s[i + 1] + ' ')
        i += 2
    else:
        sys.stdout.write(s[i])
        i += 1
while i < n:
    sys.stdout.write(s[i])
    i += 1