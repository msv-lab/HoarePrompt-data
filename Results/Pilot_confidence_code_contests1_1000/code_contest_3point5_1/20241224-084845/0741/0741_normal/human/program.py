a = raw_input()

def fun(k,n):
    x = n
    for i in range(k,k+9):
        for j in range(1,5):
            if (i+2*j)<n and a[i]==a[i+j] and a[i+j] == a[i+2*j]:
                x = min(x,i+2*j)
    return x
    
    
ans = 0
n = len(a)
for i in range(n):
    ans += n-fun(i,n)
    
print (ans)