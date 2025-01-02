import sys
input = sys.stdin.readline

def sum1n(n):
    return (n*(n+1))//2
def count_max(n):
    k1 = n//2
    k2 = n - k1
    return 2*sum1n(n) - sum1n(k1) - sum1n(k2)
    
n, k = map(int, input().split())

mn = n*(n+1) // 2
if k < mn:
    print("-1")
else:
    mx = count_max(n)
    target = min(k, mx)
    print(str(target)+"\n")

    a = [i for i in range(1, n+1)]
    b = [i for i in range(1, n+1)]
    cur = mn
    i = n-1
    while cur != target:
        f = a[i]
        s = n+1-a[i]
        if f-s < target-cur:
##            print(i)
##            print(a)
##            print(b)
            b[i], b[n-1-i] = b[n-1-i], b[i]
            cur += f-s
            i -= 1
        else:
            j = a[i] - (target-cur) - 1
            b[i], b[j] = b[j], b[i]
            cur = target
##    print("11")
    print(" ".join(map(str, a)))
    print(" ".join(map(str, b)))
