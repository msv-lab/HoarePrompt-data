def solve(n, k, a):
    l, r = 0, n - 1
    sunks = 0
    while l <= r:
        if k == 0:
            break
        if l == r:
            if k >= a[r]:
                sunks += 1
                break
            break
            
        if a[l] <= a[r]:
            if k >= a[l] * 2:
                k -= a[l] * 2
                a[r] -= a[l]
                if a[r] == 0:
                    sunks += 1
                    r -= 1
                sunks += 1
                l += 1
                continue
            else:
                if a[l] * 2 - 1 == k:
                    sunks += 1
                    break
                else:
                    break
                
        if k == 0:
            break
                
        if a[r] < a[l]:
            if k >= a[r] * 2:
                k -= a[r] * 2
                a[l] -= a[r]
                if a[l] == 0:
                    sunks += 1
                    l += 1
                sunks += 1
                r -= 1
                continue
            else:
                if a[r] * 2 - 1 == k:
                    sunks += 1
                    break
                else:
                    break
            
        
    return sunks
    
# Read input
t = int(input())  # Number of test cases
for _ in range(t):
    n, k = map(int, input().split())
    a = map(int, input().split())
    print(solve(n, k, list(a)))