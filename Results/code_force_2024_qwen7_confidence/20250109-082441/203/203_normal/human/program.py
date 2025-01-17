def count_ways(n, counts):
	total_ways = 0
	sum_ = 0
	prev_m = None
	lengths = sorted(counts.keys())

	for m in lengths:
		total_ways += (counts[m] * (counts[m] - 1) * (counts[m] - 2)) // 6
		if prev_m:
			total_ways += sum_ * ((counts[m] * counts[prev_m]) // 2)
		sum_ += counts[m]
		prev_m = m

	return total_ways
 
def solve_single_test_case():
	n = int(input())
	L = list(map(int, input().split()))
 
	counts = {}
	for i in range(n):
		if L[i] not in counts:
			counts[L[i]] = 0
		counts[L[i]] += 1
 
	ways = count_ways(n, counts)
	print(ways)
 
def main():
	t = int(input())
	for _ in range(t):
		solve_single_test_case()
 
if __name__ == "__main__":
	main()