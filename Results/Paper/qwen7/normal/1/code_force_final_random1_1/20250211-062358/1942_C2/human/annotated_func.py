#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2 ⋅ 10^5), and 0 ≤ y ≤ n - x; the vertices chosen by Bessie are represented as x distinct integers from 1 to n, and the sum of x over all test cases does not exceed 2 ⋅ 10^5.
def func():
    tt = int(input())
    for ii in range(tt):
        n, x, y = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        ans = x + y - 2
        
        tmp = []
        
        for i in range(1, len(a)):
            if a[i] - a[i - 1] == 2:
                ans += 1
            elif (a[i] - a[i - 1]) % 2 == 0 and y > (a[i] - a[i - 1]) // 2 - 1:
                tmp.append((a[i] - a[i - 1]) // 2)
                ans += (a[i] - a[i - 1]) // 2
                y -= (a[i] - a[i - 1]) // 2 - 1
        
        if a[0] + n - a[len(a) - 1] == 2:
            ans += 1
        elif (a[0] + n - a[len(a) - 1]) % 2 == 0 and y > (a[i] - a[i - 1]) // 2 - 1:
            tmp.append((a[0] + n - a[len(a) - 1]) // 2)
            ans += (a[i] - a[i - 1]) // 2
            y -= (a[i] - a[i - 1]) // 2 - 1
        
        ans += y
        
        print(min(ans, n - 2))
        
    #State: Output State: The loop has executed all its iterations, and the following conditions hold:
    #
    #- `ii` is equal to the total number of iterations, which is the same as the length of the list `a`.
    #- `n` is the first integer input for each iteration.
    #- `x` is the second integer input for each iteration.
    #- `y` is the third integer input for each iteration, adjusted according to the conditions within the loop.
    #- `a` is a list of integers sorted in ascending order for each iteration.
    #- `ans` is the final result calculated after considering all the conditions within the loop. It starts as `x + y - 2` and is incremented by the differences between consecutive elements in `a` that satisfy certain conditions, as well as by the difference between `a[0] + n - a[len(a) - 1]` if it satisfies the condition.
    #- `tmp` is a list containing the valid differences between consecutive elements in `a` that satisfy the condition `(a[i] - a[i - 1]) // 2`.
    #- `i` is the length of the list `a`.
    #- `ans` is further incremented by `y` after all iterations.
    #
    #The final `ans` value is the minimum of itself and `n - 2`, ensuring it does not exceed `n - 2`.
#Overall this is what the function does:The function processes multiple test cases, each involving integers t, n, x, and y. For each test case, it calculates a value `ans` based on the given inputs and additional conditions. Specifically, it sorts a list of integers and then iterates through the list to adjust `ans` based on the differences between consecutive elements. It also considers the difference between the first and last elements of the list plus n. Finally, it prints the minimum of `ans` and `n - 2`, ensuring `ans` does not exceed `n - 2`.

