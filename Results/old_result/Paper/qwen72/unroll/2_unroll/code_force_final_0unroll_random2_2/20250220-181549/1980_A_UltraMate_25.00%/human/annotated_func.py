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
        
    #State: t is an input integer, 1 <= n <= 50, 1 <= m <= 5, and a is a string of n characters where each character is from 'A' to 'G'. The loop has printed the value of `ans` for each iteration, where `ans` is the number of characters in the string `p` ('ABCDEF') that are either not present in `s` or have a frequency less than `m` in `s`. The variables `n`, `m`, and `s` are reinitialized in each iteration, and `a` remains unchanged.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It reads an integer `t` from the input, where `1 <= t <= 1000`, and for each of the `t` test cases, it reads two integers `n` and `m` (where `1 <= n <= 50` and `1 <= m <= 5`) and a string `s` of `n` characters (each character is from 'A' to 'G'). For each test case, it calculates the number of characters in the string 'ABCDEF' that are either not present in `s` or have a frequency less than `m` in `s`, and prints this value. The function performs this calculation and print operation for each of the `t` test cases. After the function concludes, the variables `t`, `n`, `m`, and `s` are no longer in scope, and any external variables remain unchanged.

