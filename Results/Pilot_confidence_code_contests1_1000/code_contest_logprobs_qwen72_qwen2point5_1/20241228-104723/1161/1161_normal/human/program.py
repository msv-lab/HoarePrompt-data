n = int(raw_input())
 
for i in range(n):
	columns = int(raw_input())
	blockColumn = [int(x) for x in raw_input().split(" ")]
	acc = 0
	allOdds = True
	doesntHaveZero = True
	for col in blockColumn:
		acc += col
		if (col == 0): doesntHaveZero = False
		if (col % 2 == 0): allOdds = False
	if ((n == 1) or (acc == 0) or (allOdds and doesntHaveZero)):
		print("YES")
	else:
		print("NO")