T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    points = list(map(int, input().split()))
    
    result = points[k]
    
    print(result)