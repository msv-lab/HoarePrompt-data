#State of the program right berfore the function call: The function `func` is expected to take input through a predefined method or variable not shown in the function definition, typically involving a list of test cases. Each test case consists of an integer n (1 ≤ n ≤ 3 · 10^5) and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n), where the array a is guaranteed to be beautiful. The number of test cases t is a positive integer (1 ≤ t ≤ 10^4), and the sum of n over all test cases does not exceed 3 · 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().strip().split()))
        
        tmp = a[0]
        
        cnt = 0
        
        ans = n
        
        for i in range(n):
            if a[i] == tmp:
                cnt += 1
            else:
                ans = min(ans, cnt)
                cnt = 0
        
        ans = min(ans, cnt)
        
        if n == 1 or ans == n:
            print(-1)
        else:
            print(ans)
        
    #State: After all iterations, `t` is 0, and for each test case, the variable `ans` holds the minimum number of consecutive elements that are equal to the first element of the list `a` for that test case, or -1 if the list `a` has only one element or all elements are the same.
#Overall this is what the function does:The function `func` processes multiple test cases, each containing an integer `n` and a list of `n` integers. For each test case, it calculates the minimum number of consecutive elements that are equal to the first element of the list. If the list has only one element or all elements are the same, it prints `-1`. Otherwise, it prints the calculated minimum number of consecutive elements. After processing all test cases, the function completes and the state of the program is such that all test cases have been evaluated and the appropriate results have been printed.

