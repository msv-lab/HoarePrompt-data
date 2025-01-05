n=int(raw_input())

count=n

while n!=1:
    for i in range(2,n):
        if divmod(n,i)[1]==0:
            break
    b=n//i
    count+=b
    n-=b
    if b==1:
        break

print(count)