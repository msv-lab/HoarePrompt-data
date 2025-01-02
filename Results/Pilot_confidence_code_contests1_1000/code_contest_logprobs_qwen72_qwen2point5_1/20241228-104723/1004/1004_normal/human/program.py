
n, q = map(int, raw_input().split());

arr = list(map(int, raw_input().split()));

c = [0 for _ in range(n + 3)];

while q:

	l, r = map(int, raw_input().split())
	c[l - 1] += 1;
	c[r] -= 1;
	q -= 1;

for i in range(len(c)):
	if i == 0:
		continue;
	c[i] += c[i - 1];

c.sort(reverse = True)
arr.sort(reverse = True)

res = 0
for i in range(len(arr)):
	res += arr[i] * c[i];

print('{}'.format(res));