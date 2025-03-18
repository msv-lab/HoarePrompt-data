#State of the program right berfore the function call: None of the variables in the function signature are used. The function reads input directly, which is expected to be a binary string represented as a list of integers (0s and 1s).
def func_1():
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: `s` remains unchanged, `n` is the number of 1s in the list `s`, `ans` is the sum of `n + 1` for each 0 encountered after a 1.
    print(ans)
    #This is printed: - The `print(ans)` statement will print the value of `ans`, which is the sum of `n + 1` for each 0 encountered after a 1 in the list `s`.
    #
    #Output:
#Overall this is what the function does:The function `func_1` reads a binary string represented as a list of integers (0s and 1s) from the user input. It calculates a value `ans` which is the sum of `n + 1` for each 0 encountered after a 1, where `n` is the count of 1s seen so far. The function then prints the value of `ans`. The list `s` remains unchanged after the function execution.

#State of the program right berfore the function call: No variables are passed to the function `func_2`.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: The loop has executed `func_1` `t` times. No variables are passed to the function `func_2`, and `t` remains unchanged.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `t` from the user input, and then calls the function `func_1` exactly `t` times. The function does not return any value. After the function concludes, the integer `t` remains unchanged, and `func_1` has been executed `t` times.

