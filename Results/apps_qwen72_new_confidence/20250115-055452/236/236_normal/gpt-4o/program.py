def minimal_k_to_eat_half_candies(n):
    def can_vasya_eat_half(k):
        total = n
        vasya_eaten = 0
        
        while total > 0:
            # Vasya eats k candies
            if total < k:
                vasya_eaten += total
                total = 0
            else:
                vasya_eaten += k
                total -= k
            
            # Petya eats 10% of remaining candies (rounded down)
            total -= total // 10
        
        return vasya_eaten * 2 >= n
    
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if can_vasya_eat_half(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

if __name__ == "__main__":
    n = int(input().strip())
    print(minimal_k_to_eat_half_candies(n))
