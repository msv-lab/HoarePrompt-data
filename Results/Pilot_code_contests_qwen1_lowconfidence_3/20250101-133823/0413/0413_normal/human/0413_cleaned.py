s = raw_input().split(' ')
n = int(s[0])
bx = int(s[1])
x = 0
xs = raw_input().split(' ')
for i in range(n - 1, -1, -1):
    a = int(xs[n - 1 - i])
    x = x + bx ** i * a
s = raw_input().split(' ')
m = int(s[0])
by = int(s[1])
y = 0
ys = raw_input().split(' ')
for i in range(m - 1, -1, -1):
    a = int(ys[m - 1 - i])
    y = y + by ** i * a
if x == y:
    ans = '='
elif x > y:
    ans = '>'
else:
    ans = '<'
print(ans)