import math

def find_sequence(n):
    if n <= 2:
        return "NO"
    
    divisors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    
    if not divisors:
        return "NO"
    
    k = len(divisors)
    fractions = [(1, d) for d in divisors]
    
    return f"YES\n{k}\n" + "\n".join(f"{a} {b}" for a, b in fractions)

# Reading input
n = int(input().strip())
result = find_sequence(n)
print(result)
