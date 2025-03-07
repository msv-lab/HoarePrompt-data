def solve():
    n, m = map(int, input().split())
    a = input()
    b = input()
    
    k = 0
    j = 0  # Pointer in b
 
    for i in range(n):  # Iterate over a
        while j < m and b[j] != a[i]:
            j += 1
        if j < m:
            k += 1
            j += 1
        else:
            break
    print(k)