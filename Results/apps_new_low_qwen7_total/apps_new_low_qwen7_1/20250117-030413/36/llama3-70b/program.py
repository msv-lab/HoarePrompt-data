n, m = map(int, input().split())
field = [input() for _ in range(n)]

rows = len(set(''.join(field[i::n//3]) for i in range(n//3)))
cols = len(set(''.join(row[i*m//3:(i+1)*m//3] for row in field)) for i in range(3))

print("YES" if rows == 3 and cols == 3 else "NO")
