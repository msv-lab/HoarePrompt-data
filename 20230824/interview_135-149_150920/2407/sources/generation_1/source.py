q = int(input())
for _ in range(q):
    n, r = map(int, input().split())
    positions = list(map(int, input().split()))
    
    positions.sort()
    shots = 1
    max_pos = positions[-1]
    
    for i in range(n-2, -1, -1):
        if positions[i] <= max_pos:
            break
        else:
            shots += 1
    
    print(shots)