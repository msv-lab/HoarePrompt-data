#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and 0 ≤ y ≤ n - x; the sum of x over all test cases does not exceed 2⋅10^5; the first line of each test case contains three integers n, x, and y; the second line of each test case contains x distinct integers from 1 to n, representing the vertices Bessie has chosen.
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
        
    #State: After all iterations of the loop, `i` will be equal to `x`, `t1` will be `(a[x-1] + 1) % n`, `t2` will be `(a[x-1] + 2) % n`, and `ans` will be incremented for each iteration where `t1` is not in `present` and `t2` is in `present`.
    gaps = []
    for i in range(x):
        next_elem = a[(i + 1) % x] + (n if i == x - 1 else 0)
        
        gap = next_elem - a[i] - 1
        
        if gap > 0:
            gaps.append(gap)
        
    #State: The variable `i` will be equal to `x`, `x` must be a positive integer, `next_elem` will be `a[x % x] + n` if `x` is greater than 1, otherwise it is `a[1]`, `gap` will be `next_elem - a[i-1] - 1`, and `gaps` will be a list containing all positive values of `gap` calculated during each iteration where `gap > 0`.
    #
    #In more detail, after the loop completes all its iterations, `i` will have reached the value of `x`, indicating that the loop has processed every index from `0` to `x-1`. The variable `next_elem` will be calculated as `a[(i + 1) % x] + n` if `i` is less than `x-1`, or simply `a[x % x]` if `i` is `x-1`. The `gap` is computed as the difference between `next_elem` and `a[i]` minus 1. If `gap` is positive, it gets appended to the `gaps` list. Thus, `gaps` will contain all positive `gap` values calculated throughout the loop's iterations.
    gaps.sort()
    for gap in gaps:
        pairs = gap // 2
        
        if y >= pairs:
            ans += gap
            y -= pairs
        else:
            ans += 2 * y
            break
        
    #State: The final value of `ans` is the sum of all `gap` values added during each iteration of the loop, and `y` retains its last adjusted value after the loop exits.
    print(ans)
    #This is printed: ans (where ans is the sum of all gap values added during each iteration of the loop)
#Overall this is what the function does:The function processes input data consisting of multiple test cases. Each test case includes integers n, x, and y, followed by x distinct integers from 1 to n. It calculates and returns the sum of certain gaps derived from the input data. Specifically, it counts how many gaps of size 1 or 2 are present between consecutive elements in the list of chosen vertices, and then sums up the remaining gaps after adjusting based on the value of y. If y is insufficient to cover all possible pairs, it uses the available y to maximize the sum.

