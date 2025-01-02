k = int(raw_input())
for i in range(k):
	l = raw_input()
	str1 = ""
	flag = False
	if l == l[::-1]:
		for j in range(1,len(l)):
			if l[j] != l[0]:
				flag = True
				str1 = l[j] + l[1:j] + l[0] + l[j+1:]
				break
	else:
		flag = True
		str1 = l
	if flag == False:
		print(-1)
	else:
		print(str1)


			