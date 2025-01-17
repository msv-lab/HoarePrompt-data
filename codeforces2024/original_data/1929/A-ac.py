for _ in range(int(input())):
	n=int(input())
	vec=sorted([int(x) for x in input().split()])
	print(vec[n-1]-vec[0])
