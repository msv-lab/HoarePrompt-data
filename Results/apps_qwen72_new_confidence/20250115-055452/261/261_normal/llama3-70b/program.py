m, k = map(int, input().split())

def count_ones(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def find_n(m, k):
    n = 1
    while True:
        count = sum(1 for i in range(n + 1, 2 * n + 1) if count_ones(i) == k)
        if count == m:
            return n
        n += 1

print(find_n(m, k))
