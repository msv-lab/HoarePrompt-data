import sys
input = sys.stdin.read

def min_norm(A):
    a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]
    det = a * d - b * c
    
    if det == 0:
        return 0.0
    
    # Calculate the minimum adjustments
    if abs(a) >= max(abs(b), abs(c), abs(d)):
        # Adjust a
        a_prime = (b * c) / d if d != 0 else 0
        min_norm_value = abs(a - a_prime)
    elif abs(b) >= max(abs(a), abs(c), abs(d)):
        # Adjust b
        b_prime = (a * d) / c if c != 0 else 0
        min_norm_value = abs(b - b_prime)
    elif abs(c) >= max(abs(a), abs(b), abs(d)):
        # Adjust c
        c_prime = (a * d) / b if b != 0 else 0
        min_norm_value = abs(c - c_prime)
    else:
        # Adjust d
        d_prime = (b * c) / a if a != 0 else 0
        min_norm_value = abs(d - d_prime)
    
    return min_norm_value

def main():
    data = input().split()
    a, b = int(data[0]), int(data[1])
    c, d = int(data[2]), int(data[3])
    
    A = [[a, b], [c, d]]
    result = min_norm(A)
    print(f"{result:.10f}")

if __name__ == "__main__":
    main()
