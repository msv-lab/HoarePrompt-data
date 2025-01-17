def max_elixir_strength(n, v, p):
    # Sort the mushrooms by their magic power
    v_sorted = sorted(v, reverse=True)
    
    # Initialize variables to store the maximum strength and the minimum number of mushrooms
    max_strength = 0
    min_mushrooms = n
    
    # Iterate through the sorted mushrooms
    for i in range(1, n+1):
        # Calculate the strength of the elixir if we pick i mushrooms
        strength = i * v_sorted[i-1]
        
        # Update the maximum strength and the minimum number of mushrooms if necessary
        if strength > max_strength:
            max_strength = strength
            min_mushrooms = i
        elif strength == max_strength:
            min_mushrooms = min(min_mushrooms, i)
    
    return max_strength, min_mushrooms

# Input reading and processing
t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    p = list(map(int, input().split()))
    
    # Calculate and print the result
    result = max_elixir_strength(n, v, p)
    print(*result)