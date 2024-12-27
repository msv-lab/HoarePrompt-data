def Payment (A,G):
	global Cheque
	global backlog
	global size
	if size ==2:
		for i in range (2):
			if min(A[i],G[i]) == A[i]:
				Cheque += 'A'
			else:
				Cheque += 'G'
	else:
		for i in range(size):
			a,g = abs(backlog-A[i]),abs(backlog-G[i])
			if i%2 != 0:
				if max(a,g) == g:
					if g<=500:
						Cheque += 'G'
						backlog = g
					elif a <=500:
						Cheque += 'A'
						backlog =a 
				elif a <=500:
					Cheque += 'A'
					backlog =a
				elif g <=500:
					Cheque += 'G'
					backlog = g
			else:
				if min(a,g) == a:
					if a<=500:
						Cheque += 'A'
						backlog = a
					elif g<=500:
						Cheque += 'G'
						backlog =g 
				elif g <=500:
					Cheque += 'G'
					backlog =g 
				elif a<=500:
					Cheque += 'A'
					backlog = a
	print(Cheque)

A,G =[],[]
size = input()
for i in range(size):
	a,b = map(int,raw_input().split())
	A.append(a);G.append(b)
backlog = 0
Cheque =''
Payment(A,G)