for _ in range(int(input())):
	n = int(input())
	l = sorted(list(map(int, input().split())))
	score = 0
	for i in range(0,2*n,2):
		score+=l[i]
 
	print(score)