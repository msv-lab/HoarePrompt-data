#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n.
def func():
    t = int(input())
    for tc in range(t):
        n, k = map(int, input().split())
        
        i = 0
        
        while 1 << i + 1 <= k:
            i = i + 1
        
        ans = [k - (1 << i), k + 1, k + 1 + (1 << i)]
        
        for j in range(20):
            if j != i:
                ans.append(1 << j)
        
        print(len(ans))
        
        print(*ans)
        
    #State: The loop has finished executing for all `t` test cases. For each test case, `n` and `k` were read from input, and the loop calculated and printed a list `ans` of integers. The length of `ans` and the integers in `ans` were printed for each test case. The variables `t`, `n`, and `k` retain their final values from the last test case, and the loop variables `tc`, `i`, and `j` are no longer in scope.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 1000`. For each of the `t` test cases, it reads two integers `n` and `k` from the input, where `2 <= n <= 10^6` and `1 <= k <= n`. The function then calculates a list `ans` of integers based on the value of `k`. Specifically, it finds the largest power of 2 less than or equal to `k`, and constructs a list `ans` that includes `k - (1 << i)`, `k + 1`, and `k + 1 + (1 << i)`, where `i` is the exponent of the largest power of 2. Additionally, it appends all powers of 2 up to `1 << 19` to the list, except for `1 << i`. The function prints the length of the list `ans` followed by the elements of `ans` for each test case. After all test cases are processed, the variables `t`, `n`, and `k` retain their final values from the last test case, and the loop variables `tc`, `i`, and `j` are no longer in scope.

