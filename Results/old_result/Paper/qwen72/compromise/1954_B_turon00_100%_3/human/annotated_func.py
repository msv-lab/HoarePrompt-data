#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and a is a list of n integers where 1 ≤ a_i ≤ n. The array a is guaranteed to be beautiful, and the sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: `t` is an input integer such that 0 ≤ t ≤ 0, `_` is a temporary variable used in the loop, `n` is the input integer, `a` is a list of integers provided by the input, `tmp` is equal to `a[0]`, `i` is `n-1`, `cnt` is the count of consecutive elements in `a` that are equal to `tmp` at the end of the loop, and `ans` is the minimum of the previous `ans` and the current `cnt`. If `n` is equal to 1 or `ans` is equal to `n`, no further changes occur. Otherwise, `n` is not equal to 1 and `ans` is not equal to `n`.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. It calculates the minimum length of consecutive elements in `a` that are equal to the first element of `a`. If `n` is 1 or all elements in `a` are the same, it prints `-1`. Otherwise, it prints the minimum length found. The function does not return any value; it only prints the result for each test case. After the function concludes, the input variables `t`, `n`, and `a` are no longer needed, and the state of the program is reset for the next test case, if any.

