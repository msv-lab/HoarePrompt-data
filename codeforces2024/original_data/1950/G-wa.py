def is_exciting(playlist):
    n = len(playlist)
    for i in range(n - 1):
        if playlist[i][0] != playlist[i + 1][0] and playlist[i][1] != playlist[i + 1][1]:
            return False
    return True

def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        songs = []
        for _ in range(n):
            g, w = data[index].split()
            songs.append((g, w))
            index += 1
        
        max_size = 0
        # Check all subsets
        for mask in range(1 << n):
            subset = [songs[i] for i in range(n) if (mask & (1 << i))]
            if is_exciting(subset):
                max_size = max(max_size, len(subset))
        
        # Minimum removals is n - size of largest exciting subset
        results.append(n - max_size)
    
    for result in results:
        print(result)