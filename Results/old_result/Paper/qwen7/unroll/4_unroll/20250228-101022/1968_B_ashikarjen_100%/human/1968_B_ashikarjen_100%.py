def solve():
    n, m = map(int, input().split())
    a = input()
    b = input()
    
    k = 0
    j = 0  # Pointer in b
 
    for i in range(n):
        while j < m and b[j] != a[i]:
            j += 1
        
        # If a[i] is matched, increment k and j
        if j < m:
            k += 1
            j += 1
        else:
            break
 
    print(k)
    return
 
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()