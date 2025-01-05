def is_mode(c, t):
    count = t.count(c)
    return count >= (len(t) + 1) // 2

def is_good(p, q):
    n = len(p)
    for i in range(n):
        for l in range(i + 1):
            for r in range(i, n):
                if is_mode(p[i], q[l:r+1]):
                    break
            else:
                return False
    return True

def count_good_strings(n, p):
    modulo = 998244353
    count = 0
    for i in range(2**n):
        q = bin(i)[2:].zfill(n)
        if is_good(p, q):
            count = (count + 1) % modulo
    return count

# Input reading
n = int(input())
p = input().strip()

# Output the result
print(count_good_strings(n, p))