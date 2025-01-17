def factorial(n, mod):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % mod
    return result

def binomial_coefficient(n, k, mod):
    numerator = factorial(n, mod)
    denominator = (factorial(k, mod) * factorial(n - k, mod)) % mod
    return (numerator * pow(denominator, mod - 2, mod)) % mod

def count_configurations(l, n, mod):
    # Total number of ways to place 2n cows in l positions
    total_ways = binomial_coefficient(l - 1, 2 * n - 1, mod)
    # Number of ways to place n cows of FJ and n cows of FN such that no two cows of the same farmer are adjacent
    valid_ways = binomial_coefficient(l - n, n, mod)
    return (total_ways - valid_ways) % mod

def main():
    mod = 998244353
    t = int(input())
    for _ in range(t):
        l, n = map(int, input().split())
        result = count_configurations(l, n, mod)
        print(result)

if __name__ == "__main__":
    main()