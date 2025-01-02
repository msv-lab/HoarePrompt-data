#State of the program right berfore the function call: n, m, and p are positive integers such that 1 ≤ n, m, p ≤ 2·10^5; a is a list of n integers where 1 ≤ ai ≤ 10^9; b is a list of m integers where 1 ≤ bi ≤ 10^9.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, m, q = rints()
    a, b, ans = rints(), Counter(rints()), []
    all = len(b)
    for i in range(q):
        dis, mem = set(), Counter()
        
        if int(ceil((n - i) / q)) < m:
            break
        
        for j in range(i, i + (m - 1) * q, q):
            mem[a[j]] += 1
        
        for k, j in mem.items():
            if j == b[k]:
                dis.add(k)
        
        be = i
        
        for j in range(i + (m - 1) * q, n, q):
            mem[a[j]] += 1
            if mem[a[j]] == b[a[j]]:
                dis.add(a[j])
            else:
                dis.discard(a[j])
            if len(dis) == all:
                ans.append(be + 1)
            mem[a[be]] -= 1
            if b[a[be]] and mem[a[be]] == b[a[be]]:
                dis.add(a[be])
            else:
                dis.discard(a[be])
            be += q
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `m` is a positive integer and is at least 2, `q` is a positive integer and is greater than 0, `p` is a positive integer such that \(1 \leq p \leq 2 \times 10^5\), `a` is a list of integers, `b` is a `Counter` object representing the frequencies of integers, `all` is the number of unique elements in `b`, `ans` is a list containing the indices `be + 1` where the window of size `m` with step `q` has all elements matching the required frequencies in `b`, `i` is the last value of `i` for which the loop executed, `dis` is a set containing all unique elements `k` from `mem` where the count of `k` in `mem` equals the count of `k` in `b`, `mem` is a `Counter` object with the counts of `a[j]` for the last window of size `m` with step `q`, `be` is the index just after the last element processed in the last window of size `m` with step `q`. If the loop does not execute, `ans` is an empty list, `dis` is an empty set, `mem` is an empty `Counter` object, and `be` is 0.
    print('%d\n%s' % (len(ans), ' '.join(map(str, sorted(ans)))))
#Overall this is what the function does:The function reads input values for `n`, `m`, and `q`, followed by two lists `a` and `b` of lengths `n` and `m` respectively. It then processes these inputs to find all starting indices in `a` (with a step size of `q`) where a subsequence of length `m` contains exactly the same frequency of elements as specified in `b`. The function prints the number of such valid subsequences and their starting indices in ascending order. The function does not return any value. Edge cases include scenarios where no valid subsequences are found, in which case it prints `0` and an empty list. The function also handles cases where the step size `q` is larger than the remaining elements in the list `a`, terminating early to avoid unnecessary processing.

