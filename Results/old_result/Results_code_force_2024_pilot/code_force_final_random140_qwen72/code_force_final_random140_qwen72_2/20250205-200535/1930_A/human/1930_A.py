t = int(input())
while(t):
	n = int(input())
	A = list(map(int, input().split()))
	print(sum(A[::2]))
	t = t - 1