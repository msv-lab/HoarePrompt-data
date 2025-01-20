MOD = 1000000009

def func_1(n, m, k):
    max_full_sets = m // k
    remaining_correct = m % k
    if m <= n - n // k:
        score = m % MOD
    else:
        excess_full_sets = max_full_sets - (n - m) // (k - 1)
        remaining_correct_answers = m - excess_full_sets * k
        score = (remaining_correct_answers + k * (pow(2, excess_full_sets, MOD) - 1) * pow(2, MOD - 2, MOD)) % MOD
    return score
(n, m, k) = map(int, input().split())
print(func_1(n, m, k))