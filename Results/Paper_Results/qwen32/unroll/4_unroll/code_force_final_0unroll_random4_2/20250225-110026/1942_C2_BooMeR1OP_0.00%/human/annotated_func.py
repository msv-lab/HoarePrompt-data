#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2 · 10^5), and 0 ≤ y ≤ n - x. The sum of x over all test cases does not exceed 2 · 10^5. The second line of each test case consists of x distinct integers from 1 to n, representing the vertices Bessie has chosen.
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
        
    #State: `ans` is the final value after the loop, which is `x - 2` plus the number of times the condition `t1 not in present and t2 in present` is satisfied during the loop iterations.
    gaps = []
    for i in range(x):
        next_elem = a[(i + 1) % x] + (n if i == x - 1 else 0)
        
        gap = next_elem - a[i] - 1
        
        if gap > 0:
            gaps.append(gap)
        
    #State: ans is `x - 2` and gaps is a list of positive differences (gaps) between consecutive elements in the list `a`, considering the list as circular.
    gaps.sort()
    for gap in gaps:
        pairs = gap // 2
        
        if y >= pairs:
            ans += gap
            y -= pairs
        else:
            ans += 2 * y
            break
        
    #State: `ans` is the initial value `x - 2` plus the sum of some or all `gaps` depending on `y`, and `y` is the remaining value after processing.
    print(ans)
    #This is printed: ans (where ans is calculated as x - 2 plus the sum of some or all gaps depending on y)
#Overall this is what the function does:The function calculates and prints a value `ans` for each test case based on the number of vertices `n`, the number of chosen vertices `x`, an integer `y`, and a list of `x` distinct chosen vertices. The value `ans` is determined by considering the gaps between consecutive chosen vertices and adjusting it based on the value of `y`.

