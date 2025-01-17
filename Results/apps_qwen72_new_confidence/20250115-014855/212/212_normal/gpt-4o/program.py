MOD = 1000000009

def min_possible_score(n, m, k):
    # Calculate the maximum number of times we can achieve k consecutive correct answers
    max_full_sets = m // k
    remaining_correct = m % k
    
    # Calculate the minimum possible score
    if m <= n - n // k:
        # If we can avoid doubling
        score = m % MOD
    else:
        # We need to calculate the minimum score with doubling
        excess_full_sets = max_full_sets - (n - m) // (k - 1)
        remaining_correct_answers = m - excess_full_sets * k
        
        # Calculate the score with the excess full sets causing doubling
        score = (remaining_correct_answers + k * (pow(2, excess_full_sets, MOD) - 1) * pow(2, MOD-2, MOD)) % MOD
    
    return score

# Read input values
n, m, k = map(int, input().split())

# Print the minimum possible score
print(min_possible_score(n, m, k))
