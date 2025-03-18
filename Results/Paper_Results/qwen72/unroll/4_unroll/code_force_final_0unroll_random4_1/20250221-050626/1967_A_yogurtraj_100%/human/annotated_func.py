#State of the program right berfore the function call: The function `func` is not provided with any parameters, but based on the problem description, it is expected to read input from stdin, where the first line contains an integer t (1 ≤ t ≤ 100) representing the number of test cases. For each test case, the first line contains two integers n and k (1 ≤ n ≤ 2 · 10^5, 0 ≤ k ≤ 10^12), and the second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^12). The sum of n over all test cases does not exceed 5 · 10^5.
def func():
    for ii in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        r = a[0]
        
        rem = 0
        
        y = 0
        
        for i in range(0, n - 1):
            if (i + 1) * (a[i + 1] - a[i]) > k:
                r = a[i] + k // (i + 1)
                rem = k % (i + 1)
                y = n - 1 - i
                k = 0
                break
            else:
                k -= (i + 1) * (a[i + 1] - a[i])
                r = a[i + 1]
        
        if k != 0:
            r = a[n - 1] + k // n
            print((r - 1) * n + 1 + k % n)
        else:
            print((r - 1) * n + 1 + rem + y)
        
    #State: The loop has processed all test cases, and for each test case, it has printed the result of the computation. The variables `ii`, `n`, `k`, `a`, `r`, `rem`, and `y` are no longer in use after the loop completes. The loop itself has finished executing, and the program is ready to terminate or proceed to any code that follows the loop.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input (stdin). Each test case consists of an integer `n` and an integer `k`, followed by a list of `n` integers. For each test case, the function computes and prints a single integer result. The result is calculated based on the sorted list of integers and the value of `k`, ensuring that the distribution of `k` among the integers is maximized in a specific way. After processing all test cases, the function terminates, and the variables used within the function are no longer in scope.

