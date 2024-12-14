import sys
import math
input = sys.stdin.read

def max_cake_volume(n, cakes):
    volumes = [(math.pi * r * r * h) for r, h in cakes]
    dp = [0] * n
    
    for i in range(n):
        dp[i] = volumes[i]
        for j in range(i):
            if volumes[j] < volumes[i]:
                dp[i] = max(dp[i], dp[j] + volumes[i])
                
    return max(dp)

def main():
    data = input().split()
    n = int(data[0])
    cakes = [(int(data[2 * i + 1]), int(data[2 * i + 2])) for i in range(n)]
    result = max_cake_volume(n, cakes)
    print(f"{result:.6f}")

if __name__ == "__main__":
    main()
