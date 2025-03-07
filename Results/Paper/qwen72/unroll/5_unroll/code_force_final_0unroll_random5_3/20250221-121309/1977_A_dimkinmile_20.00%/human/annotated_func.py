#State of the program right berfore the function call: The function `func_1` is expected to take two parameters, `n` and `m`, which are non-negative integers such that 1 <= n, m <= 100. Additionally, the function should be able to handle multiple test cases, indicated by an integer `t` where 1 <= t <= 100.
def func_1():
    n, m = map(int, input().split())
    if (n >= m) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: *`n` and `m` are assigned the values of two non-negative integers provided by the user, where 1 <= n, m <= 100. The function `func_1` is expected to handle multiple test cases, indicated by an integer `t` where 1 <= t <= 100. If `n` is greater than or equal to `m`, the current value of `n` is greater than or equal to the current value of `m`. If `n` is less than `m`, the current value of `n` is less than the current value of `m`.
#Overall this is what the function does:The function `func_1` reads two non-negative integers `n` and `m` from the user input, where 1 <= n, m <= 100. It then compares these two values and prints 'Yes' if `n` is greater than or equal to `m`, and 'No' if `n` is less than `m`. The function does not handle multiple test cases or accept any parameters. After the function concludes, `n` and `m` retain their input values, and the program state reflects the printed result based on the comparison of `n` and `m`.

