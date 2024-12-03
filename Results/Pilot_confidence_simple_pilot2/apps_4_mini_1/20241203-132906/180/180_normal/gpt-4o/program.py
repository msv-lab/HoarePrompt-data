MOD = 10**9 + 7

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % MOD
    return result

def count_permutations(n, x, pos):
    less_than_x = x - 1
    greater_than_x = n - x
    
    left_size = pos
    right_size = n - pos - 1
    
    if left_size > less_than_x or right_size > greater_than_x:
        return 0
    
    less_pos = factorial(less_than_x) // factorial(less_than_x - left_size)
    greater_pos = factorial(greater_than_x) // factorial(greater_than_x - right_size)
    
    remaining = n - 1 - left_size - right_size
    remaining_factorial = factorial(remaining)
    
    result = (less_pos * greater_pos) % MOD
    result = (result * remaining_factorial) % MOD
    
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    n, x, pos = map(int, input().split())
    print(count_permutations(n, x, pos))
