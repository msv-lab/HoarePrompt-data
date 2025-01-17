def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    a = list(map(int, data[1:]))
    
    # Initialize positions
    positions = [(i + 1, i + 1) for i in range(n)]
    
    # Initialize the visit list
    visit = [-1] * n
    
    # We will use a dictionary to map distances to possible indices
    distance_map = {}
    
    for i in range(n):
        if a[i] not in distance_map:
            distance_map[a[i]] = []
        distance_map[a[i]].append(i)
    
    # Try to assign visits
    for i in range(n):
        if a[i] in distance_map and distance_map[a[i]]:
            visit[i] = distance_map[a[i]].pop()
        else:
            print("NO")
            return
    
    # If we have assigned all visits correctly
    print("YES")
    for x, y in positions:
        print(x, y)
    print(' '.join(str(v + 1) for v in visit))