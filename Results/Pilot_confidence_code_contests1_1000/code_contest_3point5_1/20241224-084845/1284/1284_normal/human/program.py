n = int(raw_input())
source, destination = [], []
minusCost, totalcost =0,0
for i in range(n):
	
	s, d, wt = map(int ,raw_input().split())
	if s in source or d in destination:
		s, d = d, s
		minusCost +=wt
	totalcost +=wt
	source.append(s)
	destination.append(d)
# print(source, destination, minusCost, totalcost)
print(min(minusCost, totalcost - minusCost))