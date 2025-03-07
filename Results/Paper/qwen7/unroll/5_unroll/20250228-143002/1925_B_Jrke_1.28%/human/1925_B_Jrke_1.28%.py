for _ in range(int(input())):
  x, n = map(int, input().split())
  k = x//n
  if k == 1:
    print(1)
    continue
  ans = 1
  for i in range(1 + (1 if x%2 == 0 else 0), int((x)**0.5)+1, 2):
    if x%i == 0:
      l = [ans]
      if i <= k:
        l.append(i)
      if x//i <= k:
        l.append(x//i)
      ans = max(l)
  print(ans)