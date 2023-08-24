T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    points = list(map(int, input().split()))
    
    median_index = k
    median_point = points[median_index]
    
    print(median_point)