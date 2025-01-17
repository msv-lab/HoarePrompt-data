import sys
import math

def main():
    input = sys.stdin.readline
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Precompute the initial f values
    f = [0] * n
    f[0] = math.sqrt(a[0])
    for i in range(1, n):
        f[i] = math.sqrt(f[i-1] + a[i])
    
    # Process each update
    for _ in range(q):
        k, x = map(int, input().split())
        k -= 1  # Convert to 0-based index
        
        # Update the array
        a[k] = x
        
        # Recompute f from index k to n-1
        if k == 0:
            f[k] = math.sqrt(a[k])
        else:
            f[k] = math.sqrt(f[k-1] + a[k])
        
        for i in range(k + 1, n):
            f[i] = math.sqrt(f[i-1] + a[i])
        
        # Output the floor of f(n)
        print(math.floor(f[n-1]))

if __name__ == "__main__":
    main()