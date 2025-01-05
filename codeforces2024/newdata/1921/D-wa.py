cases = int(input())
for i in range(cases):
	n, m  = [int(a) for a in input().split()]
	arr1  =[int(a) for a in input().split()]
	arr2 = [int(a) for a in input().split()]
	arr1.sort()
	arr2.sort()
	s1, s2, e1, e2 = 0, 0 , n-1, m - 1
	d = 0
	while (s1 < e1 and s2 < e2):
		sum1 = abs(arr1[s1]- arr2[s2]) + abs(arr1[e1]- arr2[e2])
		sum2 = abs(arr1[s1]- arr2[e2]) + abs(arr1[e1]- arr2[s2])
		d += max(sum1, sum2)
		s1 += 1
		s2 +=1
		e1 -= 1
		e2 -= 1
	if s1 == e1:
		d += max(abs(arr1[s1]- arr2[s2]), abs(arr1[s1]- arr2[e2]))
	print(d)