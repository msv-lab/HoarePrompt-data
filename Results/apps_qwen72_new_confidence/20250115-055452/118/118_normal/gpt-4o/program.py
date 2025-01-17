def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    lines_ns = []
    lines_ew = []
    
    index = 2
    for _ in range(N):
        A = int(data[index])
        B = int(data[index+1])
        C = int(data[index+2])
        index += 3
        lines_ns.append((A, B, C))
    
    for _ in range(M):
        D = int(data[index])
        E = int(data[index+1])
        F = int(data[index+2])
        index += 3
        lines_ew.append((D, E, F))
    
    min_east = float('inf')
    max_west = float('-inf')
    min_north = float('inf')
    max_south = float('-inf')
    
    for (A, B, C) in lines_ns:
        if C == 0:
            if B < 0:
                max_west = max(max_west, B)
            else:
                min_east = min(min_east, A)
    
    for (D, E, F) in lines_ew:
        if D == 0:
            if F < 0:
                max_south = max(max_south, F)
            else:
                min_north = min(min_north, E)
    
    if min_east == float('inf') or max_west == float('-inf'):
        east_bound = float('inf')
    else:
        east_bound = min_east - max_west
    
    if min_north == float('inf') or max_south == float('-inf'):
        north_bound = float('inf')
    else:
        north_bound = min_north - max_south
    
    if east_bound == float('inf') or north_bound == float('inf'):
        print("INF")
    else:
        print(east_bound * north_bound)

if __name__ == "__main__":
    main()
