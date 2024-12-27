s = raw_input()
l = raw_input()

b=0
r=0

for idx in range (0, (int)(s)-1):
	if (l[idx] == 'R'):
		r = r+1
	else: 
		b = b+1

if (r>b):
	print("Yes")
else:
	print("No")