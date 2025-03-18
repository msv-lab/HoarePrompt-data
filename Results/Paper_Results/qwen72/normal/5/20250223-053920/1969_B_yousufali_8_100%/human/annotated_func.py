#State of the program right berfore the function call: s is a binary string (a string consisting of only '0' and '1' characters), and n is initialized to 0.
def func_1():
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: `s` is the input string, `n` is the number of '1's in `s`, `ans` is the sum of `n + 1` for each '0' in `s` that is preceded by at least one '1'.
    print(ans)
    #This is printed: ans (where ans is the sum of n + 1 for each '0' in s that is preceded by at least one '1', and n is the number of '1's in s)
#Overall this is what the function does:The function `func_1` reads a binary string `s` from user input, processes it to calculate a value `ans` based on the number of '1's and '0's in the string, and prints the final value of `ans`. Specifically, `ans` is the sum of `n + 1` for each '0' in `s` that is preceded by at least one '1', where `n` is the count of '1's encountered before the '0'. The function does not return any value.

#State of the program right berfore the function call: No variables are passed to the function `func_2`. The function reads an integer `t` from the input, which represents the number of test cases, and `t` satisfies 1 <= t <= 10^4.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: The value of `t` remains unchanged, and the function `func_1` has been called `t` times.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `t` from the input, which represents the number of test cases, where `t` is between 1 and 10,000 inclusive. The function calls `func_1` `t` times. After the function concludes, the value of `t` remains unchanged, and the state of the program is such that `func_1` has been executed `t` times. The function does not return any value.

