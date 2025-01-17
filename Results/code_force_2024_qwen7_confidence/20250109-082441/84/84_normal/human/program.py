import math

MOD = 998244353

def mod_inverse(a, p):
    # Using Fermat's little theorem to compute the modular inverse
    return pow(a, p - 2, p)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % MOD
    return result

def calculate_probability(a, b, c):
    total_cards = a + b + c + 5
    total_decks = factorial(total_cards)
    
    # Number of ways to arrange the top 5 cards as special cards
    winning_decks = factorial(5)
    
    # Compute the probability
    probability = (winning_decks * mod_inverse(total_decks, MOD)) % MOD
    return probability

def main():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        print(calculate_probability(a, b, c))

if __name__ == "__main__":
    main()