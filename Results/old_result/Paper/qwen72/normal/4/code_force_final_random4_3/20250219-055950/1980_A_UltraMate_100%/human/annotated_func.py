#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n and m are integers such that 1 <= n <= 50 and 1 <= m <= 5, and a is a string of n characters where each character is one of 'A' to 'G'.
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
        
    #State: `t` is 0, `n` and `m` are input integers, `s` is an input string, `p` is 'ABCDEFG', `hmp` is a Counter object with the frequency of each character in the last input string `s`, `ans` is the total number of characters in `p` that are not in `hmp`, each contributing `m` to the sum, plus the sum of `(m - hmp[i])` for each character `i` in `hmp` where `hmp[i]` is less than `m`.
#Overall this is what the function does:The function `func` reads an integer `t` from user input, indicating the number of test cases. For each test case, it reads two integers `n` and `m`, and a string `s` of length `n` consisting of characters 'A' to 'G'. It calculates the number of characters in the string 'ABCDEFG' that are either missing from `s` or appear fewer than `m` times, and prints this number for each test case. After processing all test cases, the function concludes with `t` being 0, and the state of `n`, `m`, `s`, `p`, `hmp`, and `ans` being undefined or reset for the next test case.

