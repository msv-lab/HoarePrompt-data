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
        
    #State: t is an input integer, n and m are integers such that 1 <= n <= 50 and 1 <= m <= 5, and a is a string of length n containing characters from 'A' to 'G'. The loop has printed the value of ans for each iteration, where ans is the number of characters from 'A' to 'G' that are either missing or have a frequency less than m in the string s.
#Overall this is what the function does:The function `func` processes a series of inputs. It first reads an integer `t` (1 <= t <= 1000), indicating the number of test cases. For each test case, it reads two integers `n` and `m` (1 <= n <= 50, 1 <= m <= 5) and a string `s` of length `n` containing characters from 'A' to 'G'. The function calculates the number of characters from 'A' to 'G' that are either missing from `s` or have a frequency less than `m`, and prints this value for each test case. After processing all test cases, the function concludes without returning any value.

