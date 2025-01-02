i = input()
for j in range(0,i):
	dic = {}
	q = raw_input()
	a = q.split(" ")
	ma = False
	for k in a:
		if (int(k) == i-1):
			print(q.replace(" 0 "," "+str(i)+" "))
			ma = True
			break
	if (ma):
		break