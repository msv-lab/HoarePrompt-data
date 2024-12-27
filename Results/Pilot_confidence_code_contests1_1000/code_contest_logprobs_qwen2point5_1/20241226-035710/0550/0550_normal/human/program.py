n, m = map(int, raw_input().split())
g = [ raw_input().strip() for r in range(n) ]
row_count = [ 0 for r in range(n) ]
col_count = [ 0 for c in range(m) ]
total = 0
for r in range(n):
  for c in range(m):
    if g[r][c] == '*':
      row_count[r] += 1
      col_count[c] += 1
      total += 1
result = 'NO'
for r in range(n):
  for c in range(m):
    x = row_count[r] + col_count[c] + (-1 if g[r][c] == '*' else 0)
    if x == total:
      print('YES\n%d %d' % (r + 1, c + 1))
      import sys; sys.exit()
print(result)
