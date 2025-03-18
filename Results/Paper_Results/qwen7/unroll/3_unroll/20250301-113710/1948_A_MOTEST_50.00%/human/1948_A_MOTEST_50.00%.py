import os
import string
os.system('cls')
s = string.ascii_uppercase
t = int(input())
for i in range(t):
    n = int(input())
    if n == 1:
        print('NO')
    else:
        ans = ""
        x = 0
        if n % 2 == 0:
            for j in range(n//2):
                ans += (s[x]*2)
                x+=1
        else:
            ans , x = "AAA" , 1
            for j in range((n//2) - 1):
                ans += (s[x]*2)
                x+=1
        print("YES")
        print(ans)