number_of_clocks = int ( raw_input() )
clocks_pos = [ [] for i in range ( number_of_clocks ) ]
for i in range (number_of_clocks) :
	clocks_pos[i] = [int(j) for j in raw_input().split()]

def number_of_diff_coord ( clocks_pos, coord):
	l = [0 for i in range (101) ]
	for pos in clocks_pos :
		l[ pos[coord] ] += 1
	res = 0
	for i in l :
		if i > 0 :
			res += 1
	return res

x = number_of_diff_coord( clocks_pos, 0)
y = number_of_diff_coord( clocks_pos, 1)
print (min (x,y))