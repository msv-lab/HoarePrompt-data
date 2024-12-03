import sys
input = sys.stdin.read
from functools import lru_cache

MOD = 998244353

def mod_inv(a, mod):
    return pow(a, mod - 2, mod)

def calculate_probability(n, ranges):
    total_probability = 1
    for i in range(n):
        li, ri = ranges[i]
        for j in range(i+1, n):
            lj, rj = ranges[j]
            # Calculate the probability that there is no inversion between i and j
            prob_no_inversion = 0
            count_i = ri - li + 1
            count_j = rj - lj + 1
            total_count = count_i * count_j

            for x in range(li, ri + 1):
                if x > rj:
                    prob_no_inversion += count_j
                elif x >= lj:
                    prob_no_inversion += rj - x + 1

            prob_no_inversion %= MOD
            total_count %= MOD

            prob_no_inversion = prob_no_inversion * mod_inv(total_count, MOD) % MOD
            total_probability = total_probability * prob_no_inversion % MOD

    return total_probability

def main():
    data = input().strip().split()
    n = int(data[0])
    ranges = []
    index = 1
    for _ in range(n):
        l = int(data[index])
        r = int(data[index + 1])
        ranges.append((l, r))
        index += 2
    
    result = calculate_probability(n, ranges)
    print(result)

if __name__ == "__main__":
    main()
