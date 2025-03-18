#State of the program right berfore the function call: None, as the function does not take any parameters and directly reads input from the user.
def func_1():
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: `s` is the same input string, `n` is the number of '1's in the string `s`, `ans` is the sum of `n + 1` for each '0' in the string `s` that is not at the beginning of the string and is preceded by at least one '1'.
    print(ans)
    #This is printed: ans (where ans is the sum of n + 1 for each '0' in the string s that is not at the beginning of the string and is preceded by at least one '1', and n is the number of '1's in the string s)
#Overall this is what the function does:The function reads a string from the user and prints a value that represents the sum of `n + 1` for each '0' in the string that is preceded by at least one '1', where `n` is the count of '1's encountered before the '0'. The function does not return any value.

#State of the program right berfore the function call: No variables are passed to the function `func_2`. The function reads an integer `t` from the standard input, which represents the number of test cases, and `t` must satisfy 1 ≤ t ≤ 10^4.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: The value of `t` remains unchanged, and no other variables are affected.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the standard input, which represents the number of test cases to process, where 1 ≤ t ≤ 10^4. It then calls the function `func_1` exactly `t` times. The function does not return any value, and the value of `t` remains unchanged after the function execution. No other variables are affected by the function.

