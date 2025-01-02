#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 12, and a list of n pairs of integers and a list of m pairs of integers are provided, where each pair consists of two distinct integers between 1 and 9. It is also guaranteed that there is at least one pair in the first list and one pair in the second list that share exactly one number.
def func():
    n, m = map(int, raw_input().split())
    p1 = list(map(int, raw_input().split()))
    p2 = list(map(int, raw_input().split()))
    cand = set()
    cc = [set() for i in range(n)]
    dd = [set() for i in range(m)]
    for i in range(n):
        for j in range(m):
            a, b = p1[2 * i], p1[2 * i + 1]
            c, d = p2[2 * j], p2[2 * j + 1]
            if a not in (c, d) and b not in (c, d):
                continue
            if a in (c, d) and b in (c, d):
                continue
            if a in (c, d):
                kandidat = a
            else:
                kandidat = b
            cand.add(kandidat)
            cc[i].add(kandidat)
            dd[j].add(kandidat)
        
    #State of the program after the  for loop has been executed: `i` is `n-1`, `a` is `p1[2*i]`, `b` is `p1[2*i + 1]`, `n` must be greater than 0, `m` must be greater than or equal to 1, `cand` is a set containing all unique `kandidat` values, `cc[i]` is a set containing all `kandidat` values for `i`, `dd[j]` is a set containing all `kandidat` values for `j`.
    if (len(cand) == 1) :
        print(cand.pop())
    else :
        if (max(len(cc[i]) for i in range(n)) <= 1 and max(len(dd[i]) for i in range(m
    )) <= 1) :
            print(0)
        else :
            print(-1)
        #State of the program after the if-else block has been executed: *`i` is `n-1`, `a` is `p1[2*i]`, `b` is `p1[2*i + 1]`, `n` must be greater than 0, `m` must be greater than or equal to 1, `cand` is a set containing all unique `kandidat` values, `cc[i]` is a set containing all `kandidat` values for `i`, `dd[j]` is a set containing all `kandidat` values for `j`. If `max((len(cc[i]) for i in range(n))) <= 1` and `max((len(dd[i]) for i in range(m))) <= 1`, then 0 is printed. Otherwise, -1 is printed.
    #State of the program after the if-else block has been executed: *`i` is `n-1`, `a` is `p1[2*i]`, `b` is `p1[2*i + 1]`, `n` must be greater than 0, `m` must be greater than or equal to 1, `cand` is either an empty set or a set containing all unique `kandidat` values, `cc[i]` is a set containing all `kandidat` values for `i`, `dd[j]` is a set containing all `kandidat` values for `j`. If `len(cand) == 1`, the program prints 0 if `max((len(cc[i]) for i in range(n))) <= 1` and `max((len(dd[i]) for i in range(m))) <= 1`, otherwise it prints -1. Otherwise, the program prints -1.
#Overall this is what the function does:The function `func()` accepts two integers `n` and `m`, both within the range of 1 to 12, and two lists of pairs of integers. Each pair consists of two distinct integers between 1 and 9. The function iterates through these pairs to find if there is at least one pair from the first list and one pair from the second list that share exactly one common number. If such a pair is found, it adds the shared number to a set `cand`. After processing all pairs, the function checks the following conditions:
1. If `cand` contains exactly one element, it prints that element.
2. If the maximum size of any set in `cc` or `dd` is less than or equal to 1, and `cand` is non-empty, it prints 0.
3. In all other cases, it prints -1.

The function ensures that if no such pairs are found or if the conditions mentioned above do not hold, it correctly returns -1. This covers all possible edge cases including when there are no shared numbers or when the conditions for printing 0 are met.

