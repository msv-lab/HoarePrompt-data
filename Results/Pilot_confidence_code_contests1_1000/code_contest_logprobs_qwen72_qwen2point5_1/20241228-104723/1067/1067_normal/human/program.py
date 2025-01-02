n, m = map(int,raw_input().split(" "))
quant = 0
cont = 0
if (n == m):
	print(0)
elif (m % n == 0 and (m % 2 == 0 or m % 3 == 0 or m % 6)):
	while True:
		if (m % 6 == 0):
			if (quant % 2 == 0):
				n *=2
			else:
				n *=3
			quant+=1
		elif (m %2 == 0):
			n *=2
		else:
			n*=3	
		cont+=1
		
		if (n>=m):
			break
	if(n == m):
		print(cont)
	else:
		print(-1)
else:
	print(-1)
