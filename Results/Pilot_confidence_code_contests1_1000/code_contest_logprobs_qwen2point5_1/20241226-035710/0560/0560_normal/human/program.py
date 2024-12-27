#El Patron
S = list(input())

pre_list = []
tar_list = [S[0]]
count = 1
a = 1
try:
	while a < len(S):
		pre_list = tar_list 
		tar_list = []
		tar_list.append(S[i])
		a += 1
	
		while tar_list == pre_list:
			tar_list.append(S[i])
			a += 1
	
		count += 1

except IndexError:
	pass
print(count)
