from sys import stdin,stdout
from sets import Set

def seive(max_num):
    newp = []
    max_num += 1 #include the number itself
    prime = [0]*max_num
    for i in range(2,max_num):
        if(prime[i] == 0):
            for j in range(i*i,max_num,i):
                prime[j] = i
    for i in range(2,max_num):
        if(prime[i] == 0):
            newp.append(i)
    return newp


def prime_factorize(spf,x):
    s = {}
    for i in spf:
        if(i <= x):
            if(x%i == 0):
                s[i] = 1
        else:
            break
    s[x] = 1
    return s


n = int(stdin.readline())
a = []
for i in range(n):
    x = map(int,stdin.readline().split())
    a.append(x)
spf = seive(20000000)
s1 = prime_factorize(spf,a[0][0])
s2 = prime_factorize(spf,a[0][1])
#print s1,s2
for i in s1:
    s2[i] = 1
flag = 1
for i in range(1,n):
    if(len(s2) == 0):
        flag = 0
        break
    else:
        kata = {}
        for j in s2:
            if(j<=a[i][0] and a[i][0]%j==0):
                kata[j] = 1
            if(j<=a[i][1] and a[i][1]%j==0):
                kata[j] = 1
        s2 = kata
if(flag==1 and len(s2)>=1):
    for i in s2:
        stdout.write(str(i))
        break
else:
    stdout.write(str(-1))



