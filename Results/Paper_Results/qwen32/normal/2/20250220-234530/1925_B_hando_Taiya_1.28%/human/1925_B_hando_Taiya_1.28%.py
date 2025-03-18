from math import * 
def main(): 
    x,n = list(map(int, input().split())) 
    ans = 0 
    for i in range(1, isqrt(x) + 1): 
        if x % i == 0: 
            if n <= (x//i):
                ans = max(ans , i) 
            elif (n <= i): ans = max(ans , x//i) 
    print(ans) 
 
tc = int(input()) 
for _ in range(tc): 
    main()