#State of the program right berfore the function call: The function `func_1` does not take any parameters, but it reads a binary string `s` from the input, where `s` is a list of integers (0s and 1s), and `n` and `ans` are initialized to 0.
def func_1():
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: `s` is a list of integers (0s and 1s), `i` is `len(s) - 1`, `n` is the number of 1s in `s`, and `ans` is the sum of `n + 1` for each 0 in `s` that comes after at least one 1.
    print(ans)
    #This is printed: - The `print(ans)` statement will print the value of `ans` calculated as described above.
    #
    #Output:
#Overall this is what the function does:The function `func_1` reads a list of integers (0s and 1s) from the input, processes this list, and prints an integer `ans`. The value of `ans` is the sum of `n + 1` for each 0 in the list that comes after at least one 1, where `n` is the count of 1s encountered before the 0. The function does not return any value.

#State of the program right berfore the function call: No variables are passed to the function `func_2`. The function reads an integer `t` from the standard input, where 1 <= t <= 10^4, representing the number of test cases. For each test case, it calls `func_1` without passing any arguments.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is 0.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `t` from the standard input, where 1 <= t <= 10^4, representing the number of test cases. For each test case, it calls `func_1` without passing any arguments. The function does not return any value. After the function concludes, the variable `t` is 0, but this is not a reliable postcondition as it is not explicitly set in the code.

