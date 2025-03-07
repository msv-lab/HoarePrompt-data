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
        
    #State: The loop will print the length of the list `ans` and the elements of the list `ans` for each test case. The list `ans` will contain the values `k - (1 << i)`, `k + 1`, `k + 1 + (1 << i)`, and all powers of 2 from `1 << 0` to `1 << 19` except for `1 << i`. The value of `i` is the largest integer such that `1 << i + 1` is less than or equal to `k`. The variables `t`, `n`, and `k` will remain unchanged after the loop completes.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases (1 <= t <= 1000). For each test case, it reads two integers `n` and `k` (2 <= n <= 10^6 and 1 <= k <= n). It then calculates a list `ans` containing specific integers derived from `k` and all powers of 2 from 0 to 19, excluding one particular power of 2. The function prints the length of `ans` and the elements of `ans` for each test case. The variables `t`, `n`, and `k` remain unchanged after the function execution.

