#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and a is a list of integers of length n where 1 ≤ a_i ≤ n. Additionally, the array a is guaranteed to be beautiful, and the sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: `t` is 0, `_` is a placeholder, `n` is greater than 0, `a` is a list of integers provided by the user, `tmp` is the first element of the list `a`, `cnt` is the count of consecutive elements in `a` that are equal to `tmp` at the end of the list, and `ans` is the minimum count of consecutive elements equal to `tmp` found in the list `a` during the loop execution, updated to be the minimum of its previous value and `cnt`. If `n` is equal to 1 or `ans` is equal to `n`, the output is `-1`. Otherwise, the output is `ans`.
#Overall this is what the function does:The function `func` reads multiple test cases from the user input. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then calculates the minimum length of consecutive subarrays where all elements are equal to the first element of `a`. If the list `a` has only one element or if all elements are the same, it prints `-1`. Otherwise, it prints the minimum length of such subarrays. After processing all test cases, the function ends with `t` being 0, and the variables `n`, `a`, `tmp`, `cnt`, and `ans` holding their final values from the last test case.

