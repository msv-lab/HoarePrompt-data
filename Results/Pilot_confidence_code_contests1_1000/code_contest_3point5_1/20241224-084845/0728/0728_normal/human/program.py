def func(a):
  for i in range(a - 1, 0, -1):
    tf = True
    for j in range(2, i // 2):
      if (i % j == 0):
        tf = False
        break 
    if (tf): return i

n = int(input())

c = func(n)
if (not c): c = 1

print(int((n + 1) * (n + 2) * (n + 3) / 6) - c * (c - 1))