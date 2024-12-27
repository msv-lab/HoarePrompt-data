input = raw_input
N,X,Y = map(int, input().split())

arr = [[int(x) for x in input().split()] for _ in range(N)]

a = b = c = d = 0
for x in arr:
  if x[0] <= X-1: a += 1
  elif x[0] >= X+1: b += 1

  if x[1] <= Y-1: c += 1
  else: d += 1

if X == 0: a = 0
if Y == 0: c = 0
m = max(a,b,c,d)

print(m)
if m == a:
  print(X-1,Y)
elif m == b:
  print(X+1, Y)
elif m == c:
  print(X, Y-1)
else:
  print(X, Y+1)
