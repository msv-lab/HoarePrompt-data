def process_test_case(n, a, d):
    results = []
    
    for round_number in range(n):
        # Initialize damage received array
        damage_received = [0] * n
        
        # Calculate damage received for each monster
        for i in range(n):
            if i > 0:  # Monster to the left
                damage_received[i-1] += a[i]
            if i < n-1:  # Monster to the right
                damage_received[i+1] += a[i]
        
        # Count how many monsters die this round
        deaths_this_round = 0
        for j in range(n):
            if damage_received[j] > d[j]:
                deaths_this_round += 1
        
        results.append(deaths_this_round)
        
        # Update the alive status of monsters
        alive = [damage_received[k] <= d[k] for k in range(n)]
        a = [a[k] for k in range(n) if alive[k]]
        d = [d[k] for k in range(n) if alive[k]]
        n = len(a)
        
        if n == 0:
            # All subsequent rounds will have zero deaths since no monsters are left
            results.extend([0] * (n - round_number - 1))
            break
    
    return results

def main():
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
        a = list(map(int, data[index:index+n]))
        index += n
        d = list(map(int, data[index:index+n]))
        index += n
        
        result = process_test_case(n, a, d)
        results.append(result)
    
    for result in results:
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()