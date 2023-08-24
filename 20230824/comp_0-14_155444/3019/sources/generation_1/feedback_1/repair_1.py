from itertools import combinations
from math import isqrt


def calculate_prime_factors(n):
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n = n // 2
    for i in range(3, isqrt(n) + 1, 2):
        while n % i == 0:
            prime_factors.append(i)
            n = n // i
    if n > 2:
        prime_factors.append(n)
    return prime_factors


def calculate_revenue(N, data):
    max_revenue = 0
    for r in range(N, 0, -1):
        for subset in combinations(data, r):
            subset_sum = sum(subset)
            unique_prime_factors = set()
            for s in subset:
                unique_prime_factors.update(calculate_prime_factors(s))
            revenue = len(unique_prime_factors)
            max_revenue = max(max_revenue, revenue)
    return max_revenue


def main():
    N = int(input())
    data = list(map(int, input().split()))
    max_revenue = calculate_revenue(N, data)
    print(max_revenue)


if __name__ == '__main__':
    main()