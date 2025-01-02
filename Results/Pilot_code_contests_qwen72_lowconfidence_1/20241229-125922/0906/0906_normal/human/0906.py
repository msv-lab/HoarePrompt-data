t = int(input())
for i in range(t):
  s = int(input())
  total = 0
  while s > 0:
    ss = str(s)
    spend = int(ss[0]) * (10 ** (len(ss)-1))
    back = spend // 10
    total += spend
    s = s - spend + back
  print(total)
