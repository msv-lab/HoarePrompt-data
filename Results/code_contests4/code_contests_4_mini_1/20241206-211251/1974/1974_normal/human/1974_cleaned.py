n = input()
f = ' ' + raw_input() + ' '
f = f.replace(' 0 ', ' ')
s = ' ' + raw_input() + ' '
s = s.replace(' 0 ', ' ')
ff = f[1]
ss = s.find(ff)
s = ' ' + s[ss:-1] + s[:ss]
if s == f:
    print('YES')
else:
    print('NO')