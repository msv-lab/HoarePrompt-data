l,r= map(int,raw_input().split())
if r-l<10:
	three = 0
	two = 0
	for i in range (l,r+1):
		if i%3 == 0:
			three += 1
		if i%2 == 0:
			two += 1
	if three==0 and two==0:
		print (l)
		exit()
	if three>=two:
		print (3)
	else :
		print (2)
else:
	print (2)