#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n and m are integers such that 1 <= n <= 50 and 1 <= m <= 5, and a is a string of n characters where each character is from 'A' to 'G'.
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
        
    #State: t is an input integer, 1 <= n <= 50, 1 <= m <= 5, and a is a string of n characters where each character is from 'A' to 'G'. The loop has finished executing t times, and for each iteration, the value of ans is printed. The value of ans for each iteration is the number of characters from 'A' to 'F' that are either missing from the string s or appear fewer than m times.
#Overall this is what the function does:The function `func` reads an integer `t` (1 <= t <= 1000) from the input, and for each of the `t` test cases, it reads two integers `n` and `m` (1 <= n <= 50, 1 <= m <= 5) and a string `s` of `n` characters where each character is from 'A' to 'G'. For each test case, the function calculates and prints the number of characters from 'A' to 'F' that are either missing from the string `s` or appear fewer than `m` times. The function does not return any value. After the function concludes, `t` test cases have been processed, and the calculated values for `ans` have been printed for each test case.

