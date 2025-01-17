t = int(input())

for i in range(t):
	size = int(input())
	string = input()
	total = 0
	repeat = 0
	sub1 = "map"
	for j in range(size-2):
		if string[j:j+3] == sub1:
			total+=1
	sub1 = "pie"
	for j in range(size-2):
		if string[j:j+3] == sub1:
			total+=1
	sub1 = "mapie"
	for j in range(size-2):
		if string[j:j+5] == sub1:
			total-=1
	print(total)
