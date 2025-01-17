import sys
from math import gcd

input = lambda: sys.stdin.readline().rstrip()  # Faster input

def set_bit(n: int, offset: int) -> int:
    """Set the bit at the given offset in the integer n."""
    return n | (1 << offset)

def test_bit(n: int, offset: int) -> int:
    """Test if the bit at the given offset in the integer n is set."""
    return n & (1 << offset)

def solve_case():
    n, x_add = map(int, input().split())  # Read n and x
    a = list(map(int, input().split()))  # Read the array a

    a_max = max(a)  # Find the maximum value in a

    n_bits = 19  # Number of bits to consider (since max a[i] <= 4 * 10^5)

    # Arrays to track numbers with bits not set
    cnt_bit_not_set = [0] * n_bits
    idx_bit_not_set = [[-1] * 2 for _ in range(n_bits)]
    
    # Count numbers with each bit not set
    for i, x in enumerate(a):
        for k in range(n_bits):
            if not x & 1:
                if cnt_bit_not_set[k] < 2:
                    idx_bit_not_set[k][cnt_bit_not_set[k]] = i
                cnt_bit_not_set[k] += 1
            x >>= 1

    to_test = set()  # Indices to test for potential red set
    and_score = 0  # Initial bitwise AND score

    # Determine the initial bitwise AND score and potential candidates
    for k in range(n_bits):
        if cnt_bit_not_set[k] == 0:
            and_score = set_bit(and_score, k)
        elif cnt_bit_not_set[k] == 1:
            to_test |= {idx_bit_not_set[k][0]}
        elif cnt_bit_not_set[k] == 2:
            to_test |= {idx_bit_not_set[k][0], idx_bit_not_set[k][1]}

    # Check pairs of numbers for potential red set
    for i in to_test:
        for j in range(n):
            if i != j:
                g = gcd(a[i], a[j])
                and_remain = 0
                for k in range(n_bits - 1, -1, -1):
                    and_remain <<= 1
                    c = n - cnt_bit_not_set[k]
                    if test_bit(a[i], k):
                        c -= 1
                    if test_bit(a[j], k):
                        c -= 1
                    if c == n - 2:
                        and_remain |= 1
                if g > and_remain + x_add:
                    red = [a[i], a[j]]
                    blue = [a[x] for x in range(n) if x != i and x != j]
                    return f"YES\n{2} {' '.join(map(str, red))}\n{n - 2} {' '.join(map(str, blue))}"

    # Index numbers by their values
    idx = [[] for _ in range(a_max + 1)]
    for i, x in enumerate(a):
        idx[x] += [i]

    # Check for possible GCD values
    for x in range(and_score + x_add + 1, a_max + 1):
        red_idx = []
        for y in range(x, a_max + 1, x):
            i = 0
            while len(red_idx) < 2 and i < len(idx[y]):
                if idx[y][i] not in to_test:
                    red_idx += [idx[y][i]]
                i += 1
            if len(red_idx) == 2:
                break
        if len(red_idx) == 2:
            i = red_idx[0]
            j = red_idx[1]
            red = [a[i], a[j]]
            blue = [a[x] for x in range(n) if x != i and x != j]
            return f"YES\n{2} {' '.join(map(str, red))}\n{n - 2} {' '.join(map(str, blue))}"

    return "NO"

# Read number of test cases
ans = []
for _ in range(int(input())):
    ans += [str(solve_case())]
print("\n".join(ans))