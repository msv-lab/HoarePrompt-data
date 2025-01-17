def func_1(n, q, encrypted_values):
    a = []
    last = 0
    results = []
    for i in range(q):
        v = (encrypted_values[i] + last) % n
        a.append(v)
        f_a = func_2(a)
        last = f_a
        results.append(f_a)
    return results

def func_2(b):
    max_val = max(b)
    min_val = min(b)
    return max_val - min_val
t = int(input())
for _ in range(t):
    (n, q) = map(int, input().split())
    encrypted_values = list(map(int, input().split()))
    results = func_1(n, q, encrypted_values)
    print(' '.join(map(str, results)))