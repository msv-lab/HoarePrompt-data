def read_test():
	n = int(raw_input())
	line = raw_input()
	return (
		n,
		[int(x) for x in line.split(" ")]
	)
	
def solve(a, n):
	for i in range(n - 1):
		for j in range(i + 1, n):
			if a[j] < a[i]:
				a[i], a[j] = a[j], a[i]
				
	result = []
	prev = None
	for x in a:
		if x != prev:
			result.append(x)
		prev = x

	return result
	
n = int(raw_input())
for i in range(n):
	n, a = read_test()
	result = solve(a, n)
	print(" ".join([str(x) for x in result]))
	