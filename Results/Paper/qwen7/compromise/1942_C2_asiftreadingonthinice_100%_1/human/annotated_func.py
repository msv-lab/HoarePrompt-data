#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and 0 ≤ y ≤ n - x. Additionally, the sum of x over all test cases does not exceed 2⋅10^5. The first line of each test case contains three integers n, x, and y, and the second line contains x distinct integers from 1 to n, representing the vertices Bessie has chosen.
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
            elif (a[i] - a[i - 1]) % 2 == 0:
                tmp.append((a[i] - a[i - 1]) // 2)
        
        if a[0] + n - a[len(a) - 1] == 2:
            ans += 1
        elif (a[0] + n - a[len(a) - 1]) % 2 == 0:
            tmp.append((a[0] + n - a[len(a) - 1]) // 2)
        
        tmp.sort()
        
        for i in tmp:
            if y >= i - 1:
                ans += i
                y -= i - 1
            else:
                break
        
        ans += y
        
        print(min(ans, n - 2))
        
    #State: Output State: `ans` will be the minimum value between the total sum of all elements in `tmp` (where `a[i] - a[i-1]` is even and equals 2 modulo 2, plus any additional increment of 1 if `a[0] + n - a[len(a) - 1]` equals 2, and `y` is the remaining value after subtracting `i - 1` from it as many times as possible within each iteration of the loop, or it remains unchanged if the loop breaks early) plus `x`, and `n - 2`. `y` will be 0 after all iterations, as it is continuously reduced by `i - 1` in each iteration until it cannot be further reduced. `ii` will be `tt`, indicating that all test cases have been processed. `tt` will retain its original value, and `a[0] + n - a[len(a) - 1]` will be either equal to 2 or even and equals 2 modulo 2, depending on the input values for each test case.
    #
    #In simpler terms, after all iterations, `ans` will be the minimum of the total sum of all valid increments found in the loop plus `x`, and `n - 2`. `y` will be completely exhausted, `ii` will match `tt`, and `a[0] + n - a[len(a) - 1]` will follow the conditions specified in the loop.
#Overall this is what the function does:The function processes multiple test cases, each containing integers n, x, and y, and a list of x distinct integers from 1 to n. It calculates and returns the minimum value between the sum of certain increments derived from the differences between consecutive elements in the list (if these differences are even and equal to 2 modulo 2) plus x, and n - 2. The variable y is used to track and reduce a temporary sum during the calculation process, ensuring it is fully exhausted by the end of the function. After processing all test cases, the function outputs the calculated minimum value for each case.

