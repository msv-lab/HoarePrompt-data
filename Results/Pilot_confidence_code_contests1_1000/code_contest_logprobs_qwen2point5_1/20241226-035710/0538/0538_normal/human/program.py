import sys
n, x = map(int, raw_input().split())
a, b, c = list(map(int, raw_input().split())), list(map(int, raw_input().split())), [0] * n
for i in range(n): c[i] = a[i] + b[i]
c.sort(); 
for i in range(n):
    if c[i] >= x:
        print('1 ' + str(n - i))
        break
    
