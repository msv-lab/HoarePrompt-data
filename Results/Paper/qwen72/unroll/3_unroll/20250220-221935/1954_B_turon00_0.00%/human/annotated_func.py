#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and a is a list of integers of length n where 1 ≤ a_i ≤ n. The array a is guaranteed to be beautiful, and the sum of n over all test cases does not exceed 3 · 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().strip().split()))
        
        tmp = a[0]
        
        aa = set(a)
        
        if len(aa) == 1:
            print(-1)
        
        cnt = 0
        
        ans = n
        
        for i in range(n):
            if a[i] == tmp:
                cnt += 1
            else:
                ans = min(ans, cnt)
                cnt = 0
        
        ans = min(ans, cnt)
        
        print(ans)
        
    #State: The loop has finished executing all iterations. For each iteration, the variable `ans` holds the minimum length of consecutive elements in the list `a` that are equal to the first element of `a`. If all elements in `a` are the same, `ans` is -1. The values of `t`, `n`, and `a` are unchanged for each test case, but the loop has printed the value of `ans` for each test case.
#Overall this is what the function does:The function `func` processes `t` test cases, where each test case involves a list of integers `a` of length `n`. For each test case, it calculates and prints the minimum length of consecutive elements in `a` that are equal to the first element of `a`. If all elements in `a` are the same, it prints -1. The function does not return any value; it only prints the result for each test case. After the function concludes, the values of `t`, `n`, and `a` are unchanged for each test case.

