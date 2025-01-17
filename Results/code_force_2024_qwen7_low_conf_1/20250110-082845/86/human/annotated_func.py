#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and 0 ≤ y ≤ n - x. Additionally, there are x distinct integers from 1 to n on the second line of each test case, representing the vertices Bessie has chosen, and the sum of x over all test cases does not exceed 2⋅10^5.
def func():
    t = int(input())
    for _ in range(t):
        n, x, y = list(map(int, input().split()))
        
        a = list(map(int, input().split()))
        
        a = [(num - 1) for num in a]
        
        ans = x - 2
        
        st = set(a)
        
        a.sort()
        
        for i in range(x):
            t1 = (a[i] + 1) % n
            t2 = (a[i] + 2) % n
            if t1 not in st and t2 in st:
                ans += 1
        
        odd = []
        
        even = []
        
        for i in range(x):
            next_elem = a[0] + n if i == x - 1 else a[i + 1]
            gap = next_elem - a[i] - 1
            if gap > 1 and gap % 2 == 1:
                odd.append(gap)
            elif gap > 0 and gap % 2 == 0:
                even.append(gap)
        
        odd.sort()
        
        even.sort()
        
        for gap in odd:
            if y < gap // 2:
                ans += 2 * y
                y = 0
                break
            ans += gap
            y -= gap // 2
        
        for gap in even:
            if y < gap // 2:
                ans += 2 * y
                y = 0
                break
            ans += gap
            y -= gap // 2
        
        print(ans)
        
    #State of the program after the  for loop has been executed: `ans` is the sum of all gaps in the `odd` list minus the sum of `gap // 2` for each gap, plus any additional increments due to the `2 * y` condition, up to the point where `y < gap // 2` for the last `gap` processed, and `y` is 0. `odd` and `even` are sorted lists of gaps, `n`, `x`, and `t` are the input values, `st` is the set created from the last list `a`, `t1` and `t2` are the last computed values for the last element in `a` during the last iteration.
#Overall this is what the function does:The function processes input data for multiple test cases, where each test case includes values for \( t \), \( n \), \( x \), and \( y \). For each test case, it reads \( x \) distinct integers from 1 to \( n \) and calculates a value \( ans \) based on certain conditions. Specifically, it checks for gaps between consecutive elements in the list of integers, categorizes these gaps into odd and even, and updates \( ans \) accordingly. If \( y \) is less than half of a gap, it adds \( 2 \times y \) to \( ans \) and sets \( y \) to 0. Finally, it prints the value of \( ans \) for each test case. The function handles edge cases such as when \( y \) becomes 0 before processing all gaps.

