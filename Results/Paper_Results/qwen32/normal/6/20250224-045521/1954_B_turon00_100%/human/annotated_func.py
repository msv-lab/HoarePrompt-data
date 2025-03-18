#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and a is a list of n integers such that 1 ≤ a_i ≤ n. The array a is guaranteed to be beautiful according to the problem's definition. The sum of n across all test cases does not exceed 3 · 10^5.
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
        
    #State: The loop has executed `t` times. For each execution, `n` is an input integer such that 1 ≤ `n` ≤ 3 · 10^5; `a` is a list of `n` integers read from the input. The variable `tmp` is equal to `a[0]`. The variable `cnt` is the length of the longest contiguous subarray starting from `a[0]` that contains only `tmp`. The variable `ans` is the length of the shortest contiguous subarray that contains only `tmp` (or `n` if all elements are `tmp`), updated to be the minimum of its current value and `cnt` throughout the loop. After processing the entire list `a`, if `n` is equal to 1 or `ans` is equal to `n`, the output is `-1`. Otherwise, the output is the value of `ans`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then determines the length of the shortest contiguous subarray within `a` that contains only the first element of `a`. If all elements in `a` are the same or if `n` is 1, it outputs `-1`. Otherwise, it outputs the length of the shortest such subarray.

