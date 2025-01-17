MOD = 10**9 + 7

def matrix_mult(A, B, mod):
    # Multiplies two matrices A and B under modulo
    return [[sum(x * y for x, y in zip(A_row, B_col)) % mod for B_col in zip(*B)] for A_row in A]

def matrix_exponentiation(matrix, power, mod):
    # Exponentiates a matrix to the given power under modulo
    size = len(matrix)
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    base = matrix
    
    while power:
        if power % 2 == 1:
            result = matrix_mult(result, base, mod)
        base = matrix_mult(base, base, mod)
        power //= 2
    
    return result

def solve(m, n, s, l):
    total_short = sum(s)
    total_long = sum(l)
    
    # Calculate the transition matrix
    transition_matrix = [[0] * m for _ in range(m)]
    
    for i in range(m):
        for j in range(m):
            if i == j:
                transition_matrix[i][j] = s[i] * (total_short + total_long) + l[i] * total_short
            else:
                transition_matrix[i][j] = l[i] * s[j]
    
    # Exponentiate the transition matrix to the power of n
    result_matrix = matrix_exponentiation(transition_matrix, n, MOD)
    
    # The answer is the number of ways to end up at any cabin starting from cabin 1
    answer = sum(result_matrix[0]) % MOD
    return answer

# Read input
import sys
input = sys.stdin.read
data = input().split()

m = int(data[0])
n = int(data[1])
s = list(map(int, data[2:m+2]))
l = list(map(int, data[m+2:2*m+2]))

# Solve the problem
print(solve(m, n, s, l))