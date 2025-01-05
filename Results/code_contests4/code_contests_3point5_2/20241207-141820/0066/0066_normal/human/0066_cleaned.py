n = int(raw_input())
s = raw_input().strip()

def func_1(s):
    for j in xrange(1, len(s)):
        for i in xrange(len(s)):
            if i + 4 * j < len(s) and s[i] == s[i + j] == s[i + 2 * j] == s[i + 3 * j] == s[i + 4 * j] == '*':
                return True
    return False
if func_1(s):
    print('yes')
else:
    print('no')