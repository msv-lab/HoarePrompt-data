def compute_prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

def minimal_fold_length(s):
    n = len(s)
    pi = compute_prefix_function(s)
    k = n - pi[-1]
    return k

import sys

def main():
    import sys
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        if idx >= len(data):
            n = 0
            s = ''
        else:
            n = int(data[idx])
            idx += 1
            if idx >= len(data):
                s = ''
            else:
                s = data[idx]
                idx += 1
        if n == 0:
            results.append(0)
            continue
        k = minimal_fold_length(s)
        results.append(k)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
