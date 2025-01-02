N=int(raw_input())
A=raw_input().split(" ")
B=raw_input().split(" ")

A = map(int, A)
B = map(int, B)

maxim=0
for i in xrange(1,N+1):
	temp=sum(A[0:i]) + sum(B[i-1:N])
	print(sum(A[0:i]),sum(B[i-1:N]))
	if maxim < temp:
		maxim = temp
print(maxim)