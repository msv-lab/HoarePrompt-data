n = int(input())
vs = map(int, raw_input().split())

minO = -1
res = 0
for e in vs:
	res += e
	if minO == -1 or minO > e:
		minO = e

if res % 2 == 1:
	res -= minO

print(res)

