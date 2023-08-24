q = int(input())

for _ in range(q):
    l1, r1, l2, r2 = map(int, input().split())
    
    # Choose two distinct integer points that satisfy the conditions
    a = l1
    b = l2 + (l1 == l2)
    
    print(b, a)