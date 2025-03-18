#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n. The sum of n over all test cases does not exceed 10^7.
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
        
    #State: The variable `t` retains its initial value, representing the number of test cases. The variables `n` and `k` do not retain any specific values as they are overwritten in each iteration. The variable `i` holds the value from the last test case, and `ans` holds the list from the last test case.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `k`. It then calculates and prints the length of a specific list `ans` and the elements of `ans` based on the value of `k`. The list `ans` is constructed such that it contains three specific values derived from `k` and powers of 2, excluding the power of 2 that is used in one of the first three values.

