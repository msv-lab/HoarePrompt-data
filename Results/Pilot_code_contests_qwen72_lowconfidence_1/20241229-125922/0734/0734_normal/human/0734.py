n, a, b, c, d = map(int, raw_input().split())
dd = b - a
if dd < 0:
  dd = -dd

def get(n, c, d):
  l = -1
  r = n
  while l + 1 < r:
    mid = (l + r) / 2
    if mid * c - (n - mid) * d >= 0:
      r = mid
    else:
      l = mid
  return r

l = get(n, c, d)

ok = False
for i in range(l, n + 1):
  ll = i * c - (n - i) * d
  rr = i * d - (n - i) * c
  if ll <= dd and rr >= dd:
    ok = True
  if ll > dd:
    break

if ok:
  print('YES')
else:
  print('NO')
