#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n and m are integers such that 1 <= n <= 50 and 1 <= m <= 5, a is a string of length n containing characters from 'A' to 'G'.
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
        
    #State: t is an input integer, 1 <= n <= 50, 1 <= m <= 5, a is a string of length n containing characters from 'A' to 'G'. The loop has printed the number of additional characters needed to make each string s have at least m occurrences of each character from 'A' to 'G'.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two integers `n` and `m`, and a string `s` of length `n` containing characters from 'A' to 'G'. The function calculates and prints the number of additional characters needed to ensure that each character from 'A' to 'G' appears at least `m` times in the string `s`. After processing all test cases, the function concludes without returning any value.

