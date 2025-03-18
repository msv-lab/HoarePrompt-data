#State of the program right berfore the function call: This function does not take any parameters, but it assumes that the input is a binary string provided through the standard input, which is converted to a list of integers.
def func_1():
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: `s` remains the same, `n` is the count of consecutive 1s at the end of the list, `ans` is the sum of `n + 1` for each sequence of 1s followed by a 0.
    print(ans)
    #This is printed: - Since the exact values of `s` are not provided, we can't compute the exact numerical value of `ans`.
    #   - However, based on the structure of the problem, the print statement will output the calculated value of `ans`.
    #
    #Output:
#Overall this is what the function does:The function does not accept any parameters. It reads a binary string from the standard input, converts it to a list of integers, and calculates a value `ans` based on the pattern of 1s and 0s in the list. Specifically, `ans` is the sum of `n + 1` for each sequence of 1s followed by a 0, where `n` is the count of consecutive 1s in that sequence. The function then prints the value of `ans`. The list `s` remains unchanged after the function execution.

#State of the program right berfore the function call: No variables are passed to the function func_2. The function reads an integer t from the input, where 1 <= t <= 10^4, and iterates t times, calling func_1 in each iteration.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: The loop has executed `t` times, and `func_1` has been called `t` times. The value of `t` remains unchanged.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the input, where `1 <= t <= 10^4`, and calls the function `func_1` `t` times. The value of `t` remains unchanged after the function completes. The function does not return any value.

