#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and 0 ≤ y ≤ n - x; the vertices Bessie has chosen are represented by x distinct integers from 1 to n, and the sum of x over all test cases does not exceed 2⋅10^5.
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
        
    #State of the program after the  for loop has been executed: `t` is an integer such that 1 ≤ `t` ≤ 10^4, `n` is the last `n` value input by the user, `x` is the total number of iterations the loop has executed, `y` is the final value of `y` after all iterations, `a` is the sorted list of integers input by the user, `ans` is the final value of `ans` after all iterations, `st` is a set containing the unique elements of `a`, `odd` is an empty list, `even` is an empty list, and the output of `print(ans)` is the final value of `ans`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \( t \), \( n \), \( x \), and \( y \). For each test case, it first reads a list of integers \( a \) representing vertices chosen by Bessie. It then calculates the minimum number of additional edges needed to connect all chosen vertices in a cycle, considering certain conditions. Specifically, it checks for gaps between consecutive vertices and uses the values of \( y \) to determine how many additional edges can be added before needing to adjust \( y \). The function outputs the total number of additional edges required for each test case.

