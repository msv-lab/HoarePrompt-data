#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2 ⋅ 10^5), and 0 ≤ y ≤ n - x; the vertices Bessie has chosen are represented as x distinct integers from 1 to n, and the sum of x over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: `i` is equal to `x`, `ans` is equal to `x`, `t1` is `(a[x-1] + 1) % n`, `t2` is `(a[x-1] + 2) % n`.
    #
    #After all the iterations of the loop, the variable `i` will be equal to `x`, as it increments by 1 in each iteration starting from 0. The loop continues until `i` reaches `x`. The variable `ans` is incremented by 1 each time the conditions `t1 not in present and t2 in present` are met. Since the problem statement indicates that the loop updates `ans` to `x` if these conditions are satisfied for all `i` from 0 to `x-1`, `ans` will be equal to `x`. The values of `t1` and `t2` will be the results of `(a[i] + 1) % n` and `(a[i] + 2) % n` respectively, with `i` being the last value it takes, which is `x-1`.
    gaps = []
    for i in range(x):
        next_elem = a[(i + 1) % x] + (n if i == x - 1 else 0)
        
        gap = next_elem - a[i] - 1
        
        if gap > 0:
            gaps.append(gap)
        
    #State: After the loop executes all its iterations, the variable `i` will be equal to `x`, `ans` will still be equal to the initial value of `x`, `t1` and `t2` will retain their initial values, `gaps` will contain a list of all positive differences between consecutive elements in the array `a` modulo `n`, provided these differences are greater than 0.
    gaps.sort()
    for gap in gaps:
        pairs = gap // 2
        
        if y >= pairs:
            ans += gap
            y -= pairs
        else:
            ans += 2 * y
            break
        
    #State: Output State: All positive differences between consecutive elements in the array `a` modulo `n` have been processed in the `gaps` list. The variable `i` retains its initial value, indicating that the index has not changed throughout the loop's execution. The variable `ans` is the sum of all `gap` values where `y` was greater than or equal to `pairs`, plus twice the value of `y` where `y` was less than `pairs`. The variable `t1` retains its initial value, and `t2` is updated to the last `gap // 2` value processed. The variable `y` is adjusted according to the conditions within the loop for each iteration until all elements in `gaps` have been processed.
    print(ans)
    #This is printed: ans (where ans is the sum of all gap values where y was greater than or equal to pairs, plus twice the value of y where y was less than pairs)
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \( n \), \( x \), and \( y \). It reads a list of integers representing vertices chosen by Bessie and calculates a result based on specific conditions. The function ultimately prints the sum of certain gaps between consecutive vertices, adjusted by the value of \( y \).

