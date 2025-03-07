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
        
    #State: `t` is an input integer such that 1 ≤ t ≤ 10^4, `_` is `t-1`, `n` is an input integer, `a` is a list of integers input by the user, `tmp` is equal to the first element of the list `a`, `aa` is a set containing the unique elements from the list `a`, `i` is `n-1`, `cnt` is the number of consecutive elements equal to `tmp` at the end of the list `a`, `ans` is the minimum count of consecutive elements equal to `tmp` found in the list `a` across all iterations.
#Overall this is what the function does:The function `func` processes multiple test cases, where each test case consists of an integer `n` and a list of integers `a` of length `n`. For each test case, it finds the minimum length of consecutive elements in the list `a` that are equal to the first element of the list. If all elements in the list are the same, it prints `-1`. Otherwise, it prints the minimum length of such consecutive elements. After processing all test cases, the function terminates.

