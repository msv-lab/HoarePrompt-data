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
        
    #State: `t` is 0, `n` and `m` are input integers, `s` is an input string, `p` is 'ABCDEFG', `hmp` is a Counter object containing the frequency of each character in the input string `s`. `ans` is the number of characters in `p` that are not in `s` multiplied by `m` plus the sum of `(m - hmp[i])` for each character `i` in `s` that has a frequency less than `m`.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, which represents the number of test cases. For each test case, it reads two integers `n` and `m`, and a string `s` of length `n` containing characters from 'A' to 'G'. It then calculates the number of characters in the string `s` that are missing from 'A' to 'G' and multiplies this count by `m`. Additionally, for each character in `s` that appears fewer than `m` times, it adds the difference `(m - frequency of the character)` to the result. Finally, the function prints the calculated result for each test case. After processing all test cases, the function concludes with `t` being 0, and the state of `n`, `m`, `s`, `p`, `hmp`, and `ans` being reset for each iteration.

