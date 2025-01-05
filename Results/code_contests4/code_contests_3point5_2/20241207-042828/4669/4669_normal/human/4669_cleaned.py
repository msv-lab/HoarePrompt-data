N = input()
ss = raw_input()
s = ss.split('()')
while len(s) > 1:
    s = ''.join(s)
    print(s)
    s = s.split('()')
a = ''
b = ''
s = s[0]
N = len(s)
for i in range(N):
    if s[i] == '(':
        a += ')'
    if s[i] == ')':
        b += '('
print(b + ss + a)