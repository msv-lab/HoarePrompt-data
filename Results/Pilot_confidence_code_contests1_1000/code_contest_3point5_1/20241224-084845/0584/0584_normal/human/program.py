import math 

n = raw_input()
mod = 1000000007

cnt =0
l = len(n)
for x in range (l):
    if n[x] == '0':
        cnt=cnt+1
    else:
        if n[x] == '1':
            break

num = int(n,2)

if num != 0:
    npow=int(math.log(num,2))
else:
    npow = 0

if num != 0 and ((num & (num - 1)) == 0):
    if cnt != 0:
        print (num*(2**cnt))%mod
    else:
        print (2**num)%mod
else :
    if cnt != 0:
        print (num*(2**cnt)*(2**npow))%mod
    else:
        print (num*(2**npow))%mod


