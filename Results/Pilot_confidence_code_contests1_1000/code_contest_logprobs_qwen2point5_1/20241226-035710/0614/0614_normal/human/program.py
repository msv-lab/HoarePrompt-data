n = raw_input()
n = int(n)
contests = raw_input().split(' ')
contests = [int(i) for i in contests]

day = 1
idx = 0
while day < n+1:
	if idx >= n:
		break
	if contests[idx] >= day:
		idx += 1
		day += 1
	else:
		idx += 1

print(day)