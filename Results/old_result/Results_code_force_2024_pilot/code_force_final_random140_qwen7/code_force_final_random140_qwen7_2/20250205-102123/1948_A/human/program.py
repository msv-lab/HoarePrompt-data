import os
import string
os.system('cls')
s = string.ascii_uppercase
t = int(input())
for i in range(t):
    n = int(input())
    if n % 2 == 1:
        print('NO')
    else:
        ans,x = "" , 0
        x = 0
        for j in range(n//2):
            ans += (s[x]*2)
            x+=1
        print("YES")
        print(ans)