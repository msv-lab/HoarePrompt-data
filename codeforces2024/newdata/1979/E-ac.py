def solve():
  n, d = map(int, input().split())
  X = [0 for _ in range(n)]
  Y = [0 for _ in range(n)]
  
  for i in range(n):
    x, y = map(int, input().split())
    X[i], Y[i] = x - y, x + y
    
  for _ in range(2):
    hach = {}
    for i in range(n):
      if X[i] not in hach:
        hach[X[i]] = {}
      hach[X[i]][Y[i]] = i
    
    for i in range(n):
      x = X[i]
      y = Y[i]
      if y + d in hach.get(x, {}):
        edge = hach[x][y + d]
        for point in [x - d, x + d]:
          if point in hach:
            for key in sorted(hach[point]):
              if y <= key <= y + d:
                print(i + 1, edge + 1, hach[point][key] + 1)
                return 0
    X, Y = Y, X
      
  print("0 0 0")
 
for _ in range(int(input())):
  solve()
    