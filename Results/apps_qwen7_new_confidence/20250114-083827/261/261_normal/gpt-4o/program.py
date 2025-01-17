def count_set_bits(x):
    return bin(x).count('1')

def find_n_for_m_k(m, k):
    n = 1
    while True:
        count = 0
        for i in range(n + 1, 2 * n + 1):
            if count_set_bits(i) == k:
                count += 1
        if count == m:
            print(n)
            return
        n += 1

# Read input values for m and k
m, k = map(int, input().split())

# Find and print the required number n
find_n_for_m_k(m, k)
