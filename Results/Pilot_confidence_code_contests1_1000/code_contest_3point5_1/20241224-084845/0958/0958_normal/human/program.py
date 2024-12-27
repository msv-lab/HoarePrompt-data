d=input()
n=input()
string=raw_input()
sum=0
for i in range(0,n-1):
	a=d-int(string.split(" ")[i])
	sum=sum+a
print(sum)