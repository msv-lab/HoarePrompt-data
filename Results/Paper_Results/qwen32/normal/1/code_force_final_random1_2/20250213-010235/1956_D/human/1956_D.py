def apply_operations(a, l, r, ops):
    if l == r:
        if a[l] != 0:
            ops.append((l, l))
            a[l] = 0
        return
 
    apply_operations(a, l + 1, r, ops)
    if a[l] != r - l + 1:
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
 
        apply_operations(a, l + 1, r, ops)
 
def maximize_sum(a):
    n = len(a)
    ops = []
 
    def recursive_maximize_sum(l, r):
        s = sum(a[l:r+1])
        if s <= (r - l + 1) * (r - l + 1):
            apply_operations(a, l, r, ops)
            ops.append((l, r))
            for i in range(l, r + 1):
                a[i] = r - l + 1
        else:
            mx = max(a[l:r+1])
            pos = a[l:r+1].index(mx) + l
            if pos != l:
                recursive_maximize_sum(l, pos - 1)
            if pos != r:
                recursive_maximize_sum(pos + 1, r)
 
    recursive_maximize_sum(0, n - 1)
    return sum(a), len(ops), ops
 
def main():
    n = int(input())
    a = list(map(int, input().split()))
    s, m, ops = maximize_sum(a)
    print(s, m)
    for l, r in ops:
        print(l + 1, r + 1)
 
if __name__ == "__main__":
    main()