#State of the program right berfore the function call: s is a binary string (a string consisting of only '0' and '1' characters).
def func_1():
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: `s` remains the same binary string, `n` is the number of '1's in `s`, `ans` is the sum of `n + 1` for each '0' in `s` that is preceded by at least one '1'.
    print(ans)
    #This is printed: ans (where ans is the sum of n + 1 for each '0' in s that is preceded by at least one '1', and n is the number of '1's in s)
#Overall this is what the function does:The function `func_1` reads a binary string `s` from user input. It calculates and prints a value `ans`, which is the sum of `n + 1` for each '0' in `s` that is preceded by at least one '1', where `n` is the number of '1's encountered before the '0'. The function does not return any value. After the function concludes, the binary string `s` remains unchanged, and the value `ans` is printed to the console.

#State of the program right berfore the function call: No variables are passed to the function `func_2`. The function reads an integer `t` from the standard input, where 1 <= t <= 10^4, and iterates `t` times, calling `func_1` in each iteration.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: The value of `t` remains unchanged, and no other variables are affected by the loop.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `t` from the standard input, where `t` must be between 1 and 10,000 inclusive. The function then iterates `t` times, calling `func_1` in each iteration. After the function concludes, the value of `t` remains unchanged, and no other variables are affected by the loop.

