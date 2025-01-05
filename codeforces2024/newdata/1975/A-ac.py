t = int(input())


for _ in range(t):
	n = int(input())
	
	a = list(map(int, input().split()))
	
	check_all = all([ a[i-1]<= a[i] for i in range(1 , n)])
	
	if check_all:
		print("YES")
	else:
		for i in range(1, n):
			if a[i-1] > a[i]:
				new = a[i:]
				check_all_new = all([ a[0]>= new[i] for i in range(len(new))])
				new_all = all([ new[i-1]<= new[i] for i in range(1, len(new))])
				
				if check_all_new and new_all:
					print("YES")
					break
				else:
					print("NO")
					break
				
				
		
