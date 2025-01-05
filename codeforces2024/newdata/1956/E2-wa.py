def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        
        # Find monsters with non-zero energy after infinite spells
        non_zero_monsters = []
        
        for i in range(n):
            if a[i] > a[i - 1]:
                non_zero_monsters.append(i + 1)  # +1 for 1-based index
        
        results.append(f"{len(non_zero_monsters)}")
        if non_zero_monsters:
            results.append(" ".join(map(str, non_zero_monsters)))
    
    print("\n".join(results))