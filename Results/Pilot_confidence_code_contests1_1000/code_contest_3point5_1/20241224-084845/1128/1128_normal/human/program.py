cnt = 0
sim = 0
c = raw_input

c()
list = map(int, c().split(" "))

for i in list:
	sim += i
	if sim < 0:
		cnt += 1		
		sim = 0
print(cnt)