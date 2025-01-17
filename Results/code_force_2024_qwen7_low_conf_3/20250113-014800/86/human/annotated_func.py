#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n, x, and y are positive integers satisfying 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2 ⋅ 10^5), and 0 ≤ y ≤ n - x; the input consists of t test cases, where for each test case, the first line contains n, x, and y, followed by the second line containing x distinct integers from 1 to n representing the chosen vertices; the sum of x over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State of the program after the  for loop has been executed: `t` is the number of test cases, `odd` is a sorted list of all gaps that were greater than 1 and odd across all test cases, `even` is an empty list if no even gaps exist, otherwise it is a sorted list of all even gaps, `y` is 0 if the loop breaks early during any test case, otherwise it is the initial value of `y` minus the sum of `gap // 2` for each element in `odd` across all test cases, `ans` is the final value computed for each test case adjusted according to the loop operations.
#Overall this is what the function does:The function processes `t` test cases, each containing integers `n`, `x`, and `y`, and a list of `x` distinct integers representing chosen vertices. For each test case, it computes a value `ans` based on the given inputs and specific conditions. Specifically, it calculates `ans` by considering the positions of the chosen vertices, their adjacent vertices, and the gaps between consecutive chosen vertices. If there are gaps greater than 1, it adjusts `ans` by subtracting half of these gaps up to the value of `y`. The function then prints the computed `ans` for each test case.

