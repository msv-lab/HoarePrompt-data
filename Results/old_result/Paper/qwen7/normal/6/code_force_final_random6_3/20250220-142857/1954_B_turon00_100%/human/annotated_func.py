#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 \cdot 10^5, and the array a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 3 \cdot 10^5.
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
        
    #State: Output State: `ans` is the minimum value of `cnt` encountered during the entire loop execution, `i` is equal to `n`, `n` remains the same as the initial input, `a` remains the same list of integers, `tmp` is the first element of the list `a`, and `cnt` is reset to 0 at the beginning of each iteration. If `n == 1` or `ans == n`, then the condition `print(-1)` will be executed. Otherwise, `print(ans)` will be executed, where `ans` is the minimum length of the longest sequence of identical elements found in the list `a`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t` (number of test cases), followed by an integer `n` and an array `a` of `n` integers. It then finds the minimum length of the longest sequence of identical elements in the array `a`. If `n` is 1 or the minimum length is equal to `n`, it prints `-1`; otherwise, it prints the minimum length. The function does not return any value but prints the result for each test case.

