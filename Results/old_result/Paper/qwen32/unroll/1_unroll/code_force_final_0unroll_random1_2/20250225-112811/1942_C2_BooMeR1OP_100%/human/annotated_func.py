#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 4 ≤ n ≤ 10^9, x is an integer such that 2 ≤ x ≤ min(n, 2 · 10^5), and y is an integer such that 0 ≤ y ≤ n - x. The sum of x over all test cases does not exceed 2 · 10^5. The second line of each test case consists of x distinct integers from 1 to n, representing the vertices Bessie has chosen.
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
        
    #State: The output state consists of `t` lines, each representing the final value of `ans` after processing each test case. The variables `n`, `x`, `y`, and the list `a` are modified during each iteration of the outer loop but revert to their initial state for the next test case. The variables `ans`, `st`, `odd`, and `even` are recalculated for each test case and do not persist between iterations.
#Overall this is what the function does:The function processes multiple test cases, each defined by the number of vertices `n`, the number of chosen vertices `x`, a constraint `y`, and a list of `x` distinct chosen vertices. For each test case, it calculates and prints a value `ans` based on the gaps between the chosen vertices and the constraint `y`.

