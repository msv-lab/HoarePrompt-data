def min_cost_to_arena(n, m, c, a):
    # Initialize the cost to make the n-th Pokémon stand in the arena
    min_cost = float('inf')
    
    # Iterate through all possible attributes to duel on
    for j in range(m):
        # Initialize the cost for this attribute
        cost = 0
        
        # Check if the current Pokémon in the arena can win against the n-th Pokémon
        current_pokemon = 1
        while current_pokemon < n:
            # If the current Pokémon's attribute is less than the n-th Pokémon's attribute,
            # we need to increase it or hire a new Pokémon
            if a[current_pokemon-1][j] < a[n-1][j]:
                # Find the cheapest way to increase the attribute or hire a new Pokémon
                min_increase_cost = float('inf')
                for i in range(1, n):
                    if i != current_pokemon and a[i-1][j] >= a[n-1][j]:
                        # Hiring this Pokémon is cheaper than increasing the attribute
                        min_increase_cost = min(min_increase_cost, c[i-1])
                    else:
                        # Calculate the cost to increase the attribute
                        increase_cost = a[n-1][j] - a[current_pokemon-1][j]
                        min_increase_cost = min(min_increase_cost, increase_cost)
                
                # Add the minimum cost to the total cost
                cost += min_increase_cost
            
            # Move to the next Pokémon in the arena
            current_pokemon += 1
        
        # Update the minimum cost if the current attribute's cost is lower
        min_cost = min(min_cost, cost)
    
    return min_cost

# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the number of Pokémon and attributes
    n, m = map(int, input().split())
    
    # Read the costs of hiring each Pokémon
    c = list(map(int, input().split()))
    
    # Read the attributes of each Pokémon
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    
    # Calculate and print the minimum cost to make the n-th Pokémon stand in the arena
    result = min_cost_to_arena(n, m, c, a)
    print(result)