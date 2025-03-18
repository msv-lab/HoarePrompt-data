#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n and m are integers for each test case such that 1 <= n <= 50 and 1 <= m <= 5, a is a string of length n containing characters from 'A' to 'G'.
def func():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        s = input()
        
        ans = 0
        
        p = 'ABCDEF'
        
        hmp = Counter(s)
        
        for i in p:
            if i not in hmp:
                ans += m
        
        for i in hmp:
            if hmp[i] < m:
                ans += m - hmp[i]
        
        print(ans)
        
    #State: t is an input integer such that 1 <= t <= 1000, n and m are integers for each test case such that 1 <= n <= 50 and 1 <= m <= 5, a is a string of length n containing characters from 'A' to 'G'. The loop has printed the number of characters from 'A' to 'F' that are either missing or have a count less than m for each test case.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case is defined by integers `n` and `m`, and a string `s` of length `n` containing characters from 'A' to 'G'. For each test case, the function calculates and prints the number of characters from 'A' to 'F' that are either missing from the string or have a count less than `m`. The function does not return any value; it only prints the result for each test case. After the function concludes, the input variables `t`, `n`, `m`, and `s` are no longer relevant, and the program state is reset for the next function call.

