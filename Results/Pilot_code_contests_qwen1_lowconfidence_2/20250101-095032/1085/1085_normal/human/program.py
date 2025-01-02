n = int(raw_input())

rows = {}
cols = {}
posi = {}
for i in range(n):
	x, y = [int(t) for t in raw_input().split(' ')]
	if(x in rows):
		rows[x] += 1
	else:
		rows[x] = 1
	if(y in cols):
		cols[y] += 1
	else:
		cols[y] = 1
	if((x, y) in posi):
		posi[(x, y)] += 1
	else:
		posi[(x, y)] = 1

ans = 0
for t in rows.keys():
	ans = ans + (rows[t] - 1) * rows[t] / 2

for t in cols.keys():
	ans = ans + (cols[t] - 1) * cols[t] / 2

for t in posi.keys():
	if(posi[t] > 1):
		ans -= (posi[t] - 1) * posi[t] / 2

print(ans)