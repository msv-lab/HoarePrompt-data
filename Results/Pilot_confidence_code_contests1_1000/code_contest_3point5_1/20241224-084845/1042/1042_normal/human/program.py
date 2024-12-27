n=int(raw_input())

count=n

while n!=1:
    i=2
    while divmod(n,i)[1]!=0:
        i+=1
    b=divmod(n,i)[0]
    count+=b
    n=b

print(count)