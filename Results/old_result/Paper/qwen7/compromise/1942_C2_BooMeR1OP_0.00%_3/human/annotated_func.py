#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and 0 ≤ y ≤ n - x. The input also includes a list of x distinct integers from 1 to n representing the vertices Bessie has chosen. The sum of x over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 4 ≤ n ≤ 10^9, `x` is an integer such that 2 ≤ x ≤ min(n, 2⋅10^5), `y` is an integer such that 0 ≤ y ≤ n - x, `a` is a list of integers sorted in ascending order where each element is (original element - 1), `present` is a set containing all elements of the list `a` minus one, `ans` is x - 2 + number of iterations where `(a[i] + 1) % n` is not in `present` and `(a[i] + 2) % n` is in `present`.
    gaps = []
    for i in range(x):
        next_elem = a[(i + 1) % x] + (n if i == x - 1 else 0)
        
        gap = next_elem - a[i] - 1
        
        if gap > 0:
            gaps.append(gap)
        
    #State: Output State: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 4 ≤ n ≤ 10^9, `x` is an integer such that 2 ≤ x ≤ min(n, 2⋅10^5), `y` is an integer such that 0 ≤ y ≤ n - x, `a` is a list of integers sorted in ascending order where each element is (original element - 1), `present` is a set containing all elements of the list `a` minus one, `ans` is x - 2 + number of iterations where `(a[i] + 1) % n` is not in `present` and `(a[i] + 2) % n` is in `present`, `gaps` is a list containing the differences between consecutive elements of `a` plus `n` for the last element, adjusted by subtracting the original elements.
    gaps.sort()
    for gap in gaps:
        pairs = gap // 2
        
        if y >= pairs:
            ans += gap
            y -= pairs
        else:
            ans += 2 * y
            break
        
    #State: Output State: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 4 ≤ n ≤ 10^9, `x` is an integer such that 2 ≤ x ≤ min(n, 2⋅10^5), `y` is an integer such that 0 ≤ y ≤ n - x, `a` is a list of integers sorted in ascending order where each element is (original element - 1), `present` is a set containing all elements of the list `a` minus one, `ans` is x - 2 + sum of `gap` for all iterations where `(a[i] + 1) % n` is not in `present` and `(a[i] + 2) % n` is in `present`, `gaps` is a list containing the differences between consecutive elements of `a` plus `n` for the last element, adjusted by subtracting the original elements, and `gaps` is sorted.
    print(ans)
    #This is printed: ans (where ans is defined as \(x - 2 + \text{sum of } \text{gap} \text{ for all iterations where } (\text{a}[i] + 1) \% n \text{ is not in present and } (\text{a}[i] + 2) \% n \text{ is in present})\)
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer \( n \), an integer \( x \), an integer \( y \), and a list of \( x \) distinct integers from 1 to \( n \). It calculates and returns an integer value \( ans \) based on specific conditions related to the gaps between the numbers in the list. Specifically, it counts the number of valid gaps (where the next two consecutive numbers modulo \( n \) meet certain criteria) and adjusts \( ans \) accordingly, while also decrementing \( y \) appropriately. The final value of \( ans \) represents the sum of these adjustments.

