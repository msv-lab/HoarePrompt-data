n = int(raw_input()) + 1
a = [0] + [int(i) for i in raw_input().strip().split(' ')]
head = 1
ans = 0
while (head < n):
	m = a[head]
	while head < m:
		head += 1
		if head == n:
			break
		if a[head] > m:
			m = a[head]
	ans += 1
	head += 1
print (ans)