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
        
    #State: `t` is 0, `_` is `t-1`, `n` is an input integer greater than 0, `a` is a list of integers provided by the user, `tmp` is equal to the first element of the last `a`, `aa` is a set containing the unique elements of the last `a`, `i` is `n-1`, `cnt` is the count of consecutive elements equal to `tmp` at the end of the last `a`, `ans` is the minimum value between the initial `n` and the maximum count of consecutive elements equal to `tmp` found in the list `a` across all iterations.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a list of integers `a` of length `n`. If all elements in `a` are the same, it prints `-1`. Otherwise, it calculates the minimum length of consecutive subarrays where all elements are equal to the first element of `a` and prints this minimum length. After processing all test cases, the function concludes with `t` being 0, `_` being `t-1`, `n` and `a` being the values from the last test case, `tmp` being the first element of the last `a`, `aa` being a set of the unique elements of the last `a`, `i` being `n-1`, `cnt` being the count of consecutive elements equal to `tmp` at the end of the last `a`, and `ans` being the minimum value between the initial `n` and the maximum count of consecutive elements equal to `tmp` found in the last `a`.

