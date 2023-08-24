def calculate_winners(n, k):
    if k == 0: # handle division by zero
        return 0, 0, n

    max_diplomas = n // (k + 1)
    max_certificates = k * max_diplomas
    non_winners = n - (max_diplomas + max_certificates)

    return max_diplomas, max_certificates, non_winners

# Input parsing
try:
    n, k = map(int, input().split())
    diplomas, certificates, non_winners = calculate_winners(n, k)
    # Output formatting
    print("{} {} {}".format(diplomas, certificates, non_winners))
except ValueError:
    print("Invalid input")