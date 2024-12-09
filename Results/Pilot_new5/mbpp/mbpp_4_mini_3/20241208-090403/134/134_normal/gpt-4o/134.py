import math

def even_binomial_Coeff_Sum(n):
    # Sum of binomial coefficients at even indices is given by 2^(n-1)
    return 2**(n-1)

# Test cases
assert even_binomial_Coeff_Sum(4) == 8
assert even_binomial_Coeff_Sum(6) == 32
assert even_binomial_Coeff_Sum(2) == 2
