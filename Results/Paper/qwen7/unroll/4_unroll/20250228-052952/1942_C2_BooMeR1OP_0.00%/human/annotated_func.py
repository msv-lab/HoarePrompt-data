#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and 0 ≤ y ≤ n - x; the sum of x over all test cases does not exceed 2⋅10^5; the first line of each test case contains three integers n, x, and y; the second line of each test case contains x distinct integers from 1 to n, representing the vertices Bessie has chosen.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is an integer such that 4 ≤ n ≤ 10^9; `x` is an integer such that 2 ≤ x ≤ min(n, 2⋅10^5); `y` is an integer such that 0 ≤ y ≤ n - x; `a` is a sorted list where each element is (num - 1) for each num in the original list `a`; `present` is a set containing all elements from the list `a` minus one; `ans` is x - 2 + number of iterations where `(a[i] + 1) % n` is not in `present` and `(a[i] + 2) % n` is in `present`.
    gaps = []
    for i in range(x):
        next_elem = a[(i + 1) % x] + (n if i == x - 1 else 0)
        
        gap = next_elem - a[i] - 1
        
        if gap > 0:
            gaps.append(gap)
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is an integer such that 4 ≤ n ≤ 10^9; `x` is an integer such that 2 ≤ x ≤ min(n, 2⋅10^5); `y` is an integer such that 0 ≤ y ≤ n - x; `a` is a sorted list where each element is (num - 1) for each num in the original list `a`; `present` is a set containing all elements from the list `a` minus one; `ans` is x - 2 + number of iterations where `(a[i] + 1) % n` is not in `present` and `(a[i] + 2) % n` is in `present`; `gaps` is a list containing the differences between consecutive elements in `a` plus `n` if it's the last element, modulo `n`.
    gaps.sort()
    for gap in gaps:
        pairs = gap // 2
        
        if y >= pairs:
            ans += gap
            y -= pairs
        else:
            ans += 2 * y
            break
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is an integer such that 4 ≤ n ≤ 10^9; `x` is an integer such that 2 ≤ x ≤ min(n, 2⋅10^5); `y` is an integer such that 0 ≤ y ≤ n - x; `a` is a sorted list where each element is (num - 1) for each num in the original list `a`; `present` is a set containing all elements from the list `a` minus one; `ans` is the final value of `ans` after executing the loop; `gaps` is a list containing the differences between consecutive elements in `a` plus `n` if it's the last element, modulo `n`; `gaps` is sorted.
    print(ans)
    #This is printed: ans (the final value of ans after executing the loop)
#Overall this is what the function does:The function processes input data consisting of multiple test cases. Each test case includes integers n, x, and y, followed by x distinct integers from 1 to n. It sorts these integers, calculates the number of gaps that can be filled using the value of y, and returns the final count of such gaps.

