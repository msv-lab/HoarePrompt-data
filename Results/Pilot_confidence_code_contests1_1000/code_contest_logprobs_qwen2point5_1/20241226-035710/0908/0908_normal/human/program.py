test = int(raw_input())
for k in range(test):
	n = raw_input()
	a = map(int, raw_input().split())
	even , odd = 0, 0
	for i in a:
		if(i % 2 == 0):
			even+=1
		else:
			odd +=1
	if(even % 2 == 0 == odd %2 == 0):
		print("YES")
		continue
	else:
		a = sorted(a)
		i = 0
		while(i < len(a)):
			if(i + 1 < len(a) and a[i+1] - a[i] == 1):
				even -=1
				odd -=1
				i+=2
			else:
				i+=1
		if(even %2 == 0 == odd %2==0):
			print("YES")
		else:
			print("NO")