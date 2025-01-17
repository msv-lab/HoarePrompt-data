def lowbit(x):
    return x & -x

def fenwick_transform(a, n):
    s = [0] * n
    for k in range(1, n + 1):
        sum_value = 0
        for i in range(k - lowbit(k) + 1, k + 1):
            sum_value += a[i - 1]
        s[k - 1] = sum_value % 998244353
    return s

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MOD = 998244353
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        k = int(data[index + 1])
        index += 2
        b = list(map(int, data[index:index + n]))
        index += n
        
        # We will simulate the reverse process
        a = b[:]
        for _ in range(min(n, k)):
            a = fenwick_transform(a, n)
        
        results.append(' '.join(map(str, a)))
    
    sys.stdout.write('\n'.join(results) + '\n')