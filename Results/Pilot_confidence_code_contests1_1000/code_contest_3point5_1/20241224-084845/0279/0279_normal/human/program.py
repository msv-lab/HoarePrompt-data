import re
import sys

ans = [0, 0]
s = raw_input()
n = len(s)

for i in xrange(n):
    j = 0
    while j <= min(i, n - i - 1):
        t = ''
        t = re.sub(r'[^\w\s]|(.)(?=\1)', '', s[i - j:i + j + 1])
        if t[::-1] != t:
            if not (i - j > 0 and i + j < n - 1 and s[i - j - 1] == s[i + j + 1]):
                break
        else:
            ans[1] += 1
            #print 'ODD %s %s %s' % (s[i - j:i + j + 1], i + j, n)
        j += 1

for i in xrange(n):
    j = 0
    while j <= min(i, n - i - 2):
        t = re.sub(r'[^\w\s]|(.)(?=\1)', '', s[i - j:i + j + 2])
        if t[::-1] != t:
            if not (i - j > 0 and i + j < n - 2 and s[i - j - 1] == s[i + j + 2]):
                break
        else:
            ans[0] += 1
            #print 'EVEN ' + s[i - j:i + j + 2]
        j += 1

'''

for i in xrange(n):
    j = 0
    while i - j >= 0 and i + j < n:
        t = re.sub(r'[^\w\s]|(.)(?=\1)', '', s[i - j:i + j + 1])
        if t[::-1] != t:
            break
        if i + j < n - 1:
            t = re.sub(r'[^\w\s]|(.)(?=\1)', '', s[i - j:i + j + 2])
            if t[::-1] != t:
                break
        j += 1
        ans[
'''

sys.stdout.write('%s %s' % tuple(ans))
