def gcd(a, b):
	if a < b:
		a, b = b, a
	while b != 0:
		temp = a % b
		a = b
		b = temp
	return a

n = int(input("n:"))
data = []
for i in range(n):
	data.append(int(input("data:")))
def getSum(a):
	temp = a
	t = 0
	while temp:
		t += temp%10
		temp /=10
	if gcd(a,t)>1:
		return True,gcd(a,t)
	else:
		return False,0

for i in data:
	j = i
	while not getSum(j)[0]:
		j += 1
	print(j)
