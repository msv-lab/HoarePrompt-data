#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 4 ≤ n ≤ 10^9, x is an integer such that 2 ≤ x ≤ min(n, 2 · 10^5), and y is an integer such that 0 ≤ y ≤ n - x. Additionally, the sum of x over all test cases does not exceed 2 · 10^5. The second line of each test case consists of x distinct integers from 1 to n, representing the vertices Bessie has chosen.
def func_1():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    a = [(num - 1) for num in a]
    a.sort()
    present = set(a)
    ans = x - 2
    for i in range(x):
        t1 = (a[i] + 1) % n
        
        t2 = (a[i] + 2) % n
        
        if t1 not in present and t2 in present:
            ans += 1
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is an integer such that 4 ≤ n ≤ 10^9; `x` is an integer such that 2 ≤ x ≤ min(n, 2 · 10^5); `y` is an integer such that 0 ≤ y ≤ n - x; the second line of each test case consists of `x` distinct integers from 1 to `n`, representing the vertices Bessie has chosen; `a` is a list of `x` distinct integers from 0 to n-1, representing the vertices Bessie has chosen, each decreased by 1, sorted in ascending order; `present` is a set of the `x` distinct integers from `a`; `i` is `x - 1`; `t1` is `(a[x-1] + 1) % n`; `t2` is `(a[x-1] + 2) % n`. If `t1` is not in `present` and `t2` is in `present`, then `ans` is `x + (number of times the condition was met during the loop)`. Otherwise, `ans` is `x - 2 + (number of times the condition was met during the loop)`
    gaps = []
    for i in range(x):
        next_elem = a[(i + 1) % x] + (n if i == x - 1 else 0)
        
        gap = next_elem - a[i] - 1
        
        if gap > 0:
            gaps.append(gap)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is an integer such that 4 ≤ n ≤ 10^9; `x` is an integer such that 2 ≤ x ≤ min(n, 2 · 10^5); `y` is an integer such that 0 ≤ y ≤ n - x; `a` is a list of `x` distinct integers from 0 to n-1, representing the vertices Bessie has chosen, each decreased by 1, sorted in ascending order; `present` is a set of the `x` distinct integers from `a`; `i` is `x - 1`; `t1` is `(a[x-1] + 1) % n`; `t2` is `(a[x-1] + 2) % n`; `gaps` is a list containing all positive gaps between consecutive vertices in `a`, considering the circular nature of the list.
    gaps.sort()
    for gap in gaps:
        pairs = gap // 2
        
        if y >= pairs:
            ans += gap
            y -= pairs
        else:
            ans += 2 * y
            break
        
    #State: ans is the sum of gaps processed, y is reduced to 0 or the remaining pairs that could not be fully used for the last processed gap.
    print(ans)
    #This is printed: ans (where ans is the sum of gaps processed)
#Overall this is what the function does:The function processes a series of test cases where each test case consists of an integer `n`, an integer `x`, an integer `y`, and a list of `x` distinct integers. It calculates and prints an integer `ans` based on the gaps between the chosen vertices and the value of `y`. The final value of `ans` represents the sum of processed gaps adjusted by the number of pairs that can be fully used from `y`.

