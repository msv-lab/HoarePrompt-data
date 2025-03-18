#State of the program right berfore the function call: t is an integer where 1 <= t <= 10^4, n is an integer where 4 <= n <= 10^9, x is an integer where 2 <= x <= min(n, 2 * 10^5), y is an integer where 0 <= y <= n - x, and the list of x integers are distinct and within the range 1 to n.
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
        
    #State: The loop will print the value of `ans` for each iteration, and the variables `t`, `n`, `x`, `y`, and `a` will be re-initialized for each iteration based on the input. After all iterations, the final state of `t` will be unchanged, and the values of `n`, `x`, `y`, and `a` will be the inputs for the last iteration.
#Overall this is what the function does:The function `func` reads multiple sets of inputs and processes each set to calculate and print a result. For each set, it accepts an integer `t` indicating the number of test cases, and for each test case, it reads three integers `n`, `x`, and `y`, followed by a list of `x` distinct integers. The function then calculates the number of valid positions to place a new element in the list, considering the constraints and the gaps between the elements. The final result, `ans`, is printed for each test case. After processing all test cases, the function returns to its initial state, ready to process the next set of inputs.

