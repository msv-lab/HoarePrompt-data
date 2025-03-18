#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 4 ≤ n ≤ 10^9, x is an integer such that 2 ≤ x ≤ min(n, 2 · 10^5), and y is an integer such that 0 ≤ y ≤ n - x. The sum of x over all test cases does not exceed 2 · 10^5. The second line of each test case consists of x distinct integers from 1 to n, representing the vertices Bessie has chosen.
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
        
    #State: ans is x - 2 plus the number of times (a[i] + 1) % n is not in present and (a[i] + 2) % n is in present for i in range(x).
    gaps = []
    for i in range(x):
        next_elem = a[(i + 1) % x] + (n if i == x - 1 else 0)
        
        gap = next_elem - a[i] - 1
        
        if gap > 0:
            gaps.append(gap)
        
    #State: `ans` is unchanged, `gaps` is a list of positive differences (minus one) between consecutive elements in `a`, adjusted by `n` for the last element.
    gaps.sort()
    for gap in gaps:
        pairs = gap // 2
        
        if y >= pairs:
            ans += gap
            y -= pairs
        else:
            ans += 2 * y
            break
        
    #State: `ans` is updated to the sum of all `gap` values for which `y` was sufficient plus `2 * y` for the last `gap` processed where `y < pairs`, and `y` is reduced accordingly.
    print(ans)
    #This is printed: ans (where ans is the sum of all gap values for which y was sufficient plus 2 * y for the last gap processed where y < pairs)
#Overall this is what the function does:The function reads multiple test cases, each consisting of integers `n`, `x`, and `y`, and a list of `x` distinct integers. For each test case, it calculates and prints a value based on the arrangement of the chosen vertices and the additional constraint `y`. The printed value represents a computed sum related to the gaps between the chosen vertices and the constraint `y`.

