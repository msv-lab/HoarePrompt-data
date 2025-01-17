MOD = 10**9 + 7

def mod_inverse(a, mod):
    return pow(a, mod-2, mod)

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    k = int(data[1])
    a = list(map(int, data[2:]))
    
    count_0 = a.count(0)
    count_1 = a.count(1)
    
    if count_0 == 0 or count_1 == 0:
        print(1)
        return
    
    if k == 1:
        print(0)
        return
    
    total_pairs = n * (n - 1) // 2
    sorted_pairs = count_0 * count_1
    
    P = sorted_pairs
    Q = total_pairs
    
    prob = (P * mod_inverse(Q, MOD)) % MOD
    print(prob)

if __name__ == "__main__":
    solve()
