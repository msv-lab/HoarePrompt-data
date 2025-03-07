t = int(input())
 
for _ in range(t):
    n = int(input())
 
    sum = 1
    for i in range(2, n + 1):
        sum += (i * i - (i - 1) * (i - 1)) * i
 
    print(sum, n + n)
    for j in range(1, n + 1):
        print(1, n - j + 1, *range(1, n + 1))
        print(2, n - j + 1, *range(1, n + 1))