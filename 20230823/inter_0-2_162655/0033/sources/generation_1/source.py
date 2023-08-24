def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solution(a1, b1, a2, b2, L, R):
    # Find the common difference of each arithmetic progression
    d1 = gcd(a1, a2)
    d2 = gcd(a1, a2)
    
    # Calculate the remainders when dividing b1 and b2 by d1 and d2 respectively
    r1 = b1 % d1
    r2 = b2 % d2
    
    # Check if there exists an integer x such that L ≤ x ≤ R and x = a1k' + b1 = a2l' + b2
    count = 0
    x = L
    while x <= R:
        # Check if x is congruent to r1 modulo d1 and congruent to r2 modulo d2
        if (x - r1) % d1 == 0 and (x - r2) % d2 == 0:
            count += 1
        x += 1
    
    return count

# Read input
a1, b1, a2, b2, L, R = map(int, input().split())

# Call the solution function and print the result
result = solution(a1, b1, a2, b2, L, R)
print(result)