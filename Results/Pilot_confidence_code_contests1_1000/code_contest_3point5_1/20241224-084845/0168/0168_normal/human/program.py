for _ in range(int(raw_input())):
	a,b=map(str,raw_input().split())
	flag=True
	if a==b:
		print("---")
	else:
		for i in range(min(len(a),len(b))):
			if a[i]<b[i] :
				break

			elif a[i]>b[i]:
				flag=False
				break

		if flag:
			print(a)

		else:
			flag=True
			for j in range(i+1,min(len(a),len(b))):
				if a[j]<b[i]:
					flag=False
					break

			if flag:
				print("---")

			else:
				print(a[:i]+a[j]+a[i+1:j]+a[i]+a[j+1:])

