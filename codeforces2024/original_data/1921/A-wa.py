n = int(input())
for i in range(n):
	lst1 = input().split()
	lst2 = input().split()
	lst3 = input().split()
	_ = input()
	if lst1[0] == lst2[0]: print(abs((int(lst1[0]) - int(lst3[0]))*(int(lst1[1]) - int(lst2[1]))))
	else: print(abs((int(lst1[0]) - int(lst2[0]))**2 + (int(lst1[1]) - int(lst2[1]))**2) // 2)