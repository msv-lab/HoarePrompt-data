count=0
st=raw_input()
num=st.split()
n=int(num[0])
m=int(num[1])
z=int(num[2])
for i in range(1,z+1):
	if(i%n==0 and i%m==0):
		count=count+1
print(count)
