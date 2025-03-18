#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers where 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2 * 10^5), and 0 ≤ y ≤ n - x. The sum of x over all test cases does not exceed 2 * 10^5. The second line of each test case consists of x distinct integers from 1 to n, representing the vertices Bessie has chosen.
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
        
    #State: ans = x - 2 + number_of_times_condition_is_true.
    gaps = []
    for i in range(x):
        next_elem = a[(i + 1) % x] + (n if i == x - 1 else 0)
        
        gap = next_elem - a[i] - 1
        
        if gap > 0:
            gaps.append(gap)
        
    #State: `ans` is `x - 2 + number_of_times_condition_is_true`, `gaps` is a list containing all positive gaps calculated during the loop iterations.
    gaps.sort()
    for gap in gaps:
        pairs = gap // 2
        
        if y >= pairs:
            ans += gap
            y -= pairs
        else:
            ans += 2 * y
            break
        
    #State: `ans` is the initial value plus the sum of all `gap` values for which `y >= pairs`, plus `2 * y` if the loop breaks because `y < pairs`. `y` is `0` if the loop completes all iterations without breaking, or the remaining value of `y` when the loop breaks. `gaps` remains unchanged.
    print(ans)
    #This is printed: ans (where ans is the initial value plus the sum of all gap values for which y >= pairs, plus 2 * y if the loop breaks because y < pairs)
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `x`, and `y`, and a list of `x` distinct integers from 1 to `n`. For each test case, it calculates and prints a value `ans` which represents a specific count based on the given conditions and the list of integers.

