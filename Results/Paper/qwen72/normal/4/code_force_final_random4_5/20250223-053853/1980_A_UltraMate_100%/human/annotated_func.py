#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n and m are integers for each test case such that 1 <= n <= 50 and 1 <= m <= 5, and a is a string of length n containing characters from 'A' to 'G'.
def func():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        s = input()
        
        ans = 0
        
        p = 'ABCDEFG'
        
        hmp = Counter(s)
        
        for i in p:
            if i not in hmp:
                ans += m
        
        for i in hmp:
            if hmp[i] < m:
                ans += m - hmp[i]
        
        print(ans)
        
    #State: The loop has finished executing all iterations. For each test case, the integer `n` and `m` have been read from input, the string `s` has been processed, and the integer `ans` has been calculated and printed. The variables `n`, `m`, `s`, and `ans` are reset for each iteration of the loop. The string `p` remains 'ABCDEFG', and the input integer `t` is unchanged.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads two integers `n` and `m`, and a string `s` of length `n` containing characters from 'A' to 'G'. It calculates the number of additional characters needed to ensure that each character from 'A' to 'G' appears at least `m` times in the string `s`, and prints this number for each test case. After processing all test cases, the function completes, and the input integer `t` remains unchanged.

