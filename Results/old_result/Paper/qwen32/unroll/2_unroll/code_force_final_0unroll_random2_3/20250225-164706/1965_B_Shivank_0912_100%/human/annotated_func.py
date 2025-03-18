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
        
    #State: t is 0, n and k are the values from the last test case processed.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two integers `n` and `k`. For each test case, it calculates a list of integers based on the value of `k` and prints the length of this list followed by the list itself. The list is constructed such that it includes specific values derived from `k` and powers of 2, excluding the power of 2 that is closest to `k`.

