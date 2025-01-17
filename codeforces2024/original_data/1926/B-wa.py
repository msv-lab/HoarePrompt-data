t = int(input())
res = []
for i in range(t):
	arr = []
	n = int(input())
	count = 0
	flag = 0
	last = 0
	flaga = 0
	ans = 0
	for j in range(n):
		temp = []
		temp = input()
		temp = list(temp)

		if temp.count("1") != 0 and flaga == 0:
			last = temp.count("1")
			flaga = 1

		count = temp.count("1")

		if count != last and flaga == 1 and ans == 0:
			flag  = 1
			ans = 1
			res.append("TRIANGLE")

	if flag == 0:
		res.append("SQUARE")
for i in res:
	print(i)
