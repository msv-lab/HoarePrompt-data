#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n and m are integers such that 1 <= n <= 50 and 1 <= m <= 5, and a is a string of length n containing characters from 'A' to 'G'.
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
        
    #State: t is an input integer, n and m are integers such that 1 <= n <= 50 and 1 <= m <= 5, and a is a string of length n containing characters from 'A' to 'G'. The variable ans is calculated for each iteration of the loop and printed, but its final value after the loop is not retained.
#Overall this is what the function does:The function `func` reads an integer `t` from input, indicating the number of test cases. For each test case, it reads two integers `n` and `m`, and a string `s` of length `n` containing characters from 'A' to 'G'. It calculates the number of additional occurrences required for each character in `p` ('A' to 'G') to appear at least `m` times in `s`, and prints this number for each test case. The function does not return any value; it only prints the results. After the function concludes, the input variables `t`, `n`, `m`, and `s` are no longer needed, and the variable `ans` used for calculation is reset for each test case.

