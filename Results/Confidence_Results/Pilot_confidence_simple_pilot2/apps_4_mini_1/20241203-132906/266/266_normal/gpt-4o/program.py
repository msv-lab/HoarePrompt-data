def max_pleased_friends(n, m, friends, pizzas):
    from itertools import combinations
    from collections import defaultdict

    # Convert each friend's favorite ingredients to a set
    friend_favorites = [set(fav) for fav in friends]
    
    # Convert each pizza's ingredients to a set
    pizza_ingredients = [set(ing) for ing in pizzas]

    # Function to count how many friends are pleased with the given two pizzas
    def count_pleased(p1, p2):
        combined_ingredients = pizza_ingredients[p1] | pizza_ingredients[p2]
        return sum(1 for fav in friend_favorites if fav <= combined_ingredients)

    # Initialize the best solution
    best_count = 0
    best_cost = float('inf')
    best_pair = None

    # Iterate over all combinations of two pizzas
    for (i, pi), (j, pj) in combinations(enumerate(pizzas), 2):
        pleased_count = count_pleased(i, j)
        total_cost = pi[0] + pj[0]
        if (pleased_count > best_count) or (pleased_count == best_count and total_cost < best_cost):
            best_count = pleased_count
            best_cost = total_cost
            best_pair = (i + 1, j + 1)

    return best_pair

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    index = 2
    friends = []
    for _ in range(n):
        f_i = int(data[index])
        b_i = list(map(int, data[index+1:index+1+f_i]))
        friends.append(b_i)
        index += 1 + f_i
    
    pizzas = []
    for _ in range(m):
        c_j = int(data[index])
        r_j = int(data[index+1])
        a_j = list(map(int, data[index+2:index+2+r_j]))
        pizzas.append((c_j, a_j))
        index += 2 + r_j
    
    result = max_pleased_friends(n, m, friends, pizzas)
    print(result[0], result[1])
