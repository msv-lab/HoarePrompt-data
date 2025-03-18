#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n and m are integers such that 1 <= n <= 50 and 1 <= m <= 5, a is a string of length n containing characters from 'A' to 'G'.
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
        
    #State: After the loop executes all iterations, `t` is 0, `n` and `m` are the last input integers, `s` is the last input string, `p` is 'ABCDEF', `hmp` is a Counter object containing the frequency of each character in the last input string `s`, and `ans` is the sum of `m` for each character in 'ABCDEF' that is not in `hmp` plus the sum of `m - hmp[i]` for each character `i` in `hmp` where `hmp[i]` is less than `m`.
#Overall this is what the function does:The function reads multiple sets of inputs and calculates the number of additional occurrences required for each character in 'ABCDEF' to appear at least `m` times in the input string `s`. It prints this number for each set of inputs. The function processes `t` test cases, where for each case, it takes two integers `n` and `m`, and a string `s` of length `n` containing characters from 'A' to 'G'. After processing all test cases, the function has no return value, but it prints the calculated number for each test case.

