def wine_factory(n, q, a, b, c, updates):
    results = []
    
    def compute_wine():
        wine = 0
        water = a[0]
        for i in range(n):
            # Convert water to wine
            wine += min(water, b[i])
            water -= min(water, b[i])
            # Flow water to the next tower
            if i < n - 1:
                water = min(water, c[i])
                water += a[i + 1]
        return wine
    
    # Initial wine computation
    current_wine = compute_wine()
    results.append(current_wine)
    
    for p, x, y, z in updates:
        p -= 1  # Convert to 0-based index
        a[p] = x
        b[p] = y
        if p < n - 1:
            c[p] = z
        
        # Recompute wine from tower p to n
        current_wine = 0
        water = a[0]
        for i in range(n):
            if i >= p:
                # Convert water to wine
                current_wine += min(water, b[i])
                water -= min(water, b[i])
            # Flow water to the next tower
            if i < n - 1:
                if i >= p:
                    water = min(water, c[i])
                water += a[i + 1]
        
        results.append(current_wine)
    
    return results

# Example usage:
n = 4
q = 3
a = [3, 5, 3, 3]
b = [1, 4, 2, 8]
c = [5, 1, 1]
updates = [
    (1, 3, 1, 5),
    (2, 5, 1, 1),
    (3, 0, 0, 0)
]

results = wine_factory(n, q, a, b, c, updates)
for result in results:
    print(result)