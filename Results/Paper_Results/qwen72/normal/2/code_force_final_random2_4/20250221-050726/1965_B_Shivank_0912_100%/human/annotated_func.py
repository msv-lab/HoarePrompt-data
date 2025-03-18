#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, n and k are integers where 2 <= n <= 10^6 and 1 <= k <= n.
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
        
    #State: After all iterations of the loop, `t` is the initial value provided, `tc` is `t-1`, `n` and `k` are the last set of input integers for the final iteration, `i` is the largest integer such that \( 1 << i \leq k \) for the last iteration, and `j` is 19. The list `ans` for each iteration contains the initial elements `[k - (1 << i), k + 1, k + 1 + (1 << i)]` followed by all powers of 2 from `1 << 0` to `1 << 19`, excluding `1 << i`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads two integers `n` and `k`. It then calculates a list `ans` containing specific values derived from `k` and all powers of 2 up to `1 << 19`, excluding one particular power of 2. The function prints the length of this list and the list itself for each test case. After processing all test cases, the function has no return value, but the state includes the initial value of `t`, the last processed values of `n` and `k`, and the final value of `i` which is the largest integer such that \( 1 << i \leq k \) for the last test case.

