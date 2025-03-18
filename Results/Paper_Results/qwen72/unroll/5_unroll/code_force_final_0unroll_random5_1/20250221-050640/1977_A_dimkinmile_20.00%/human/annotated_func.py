#State of the program right berfore the function call: The function should take two parameters, n and m, which are non-negative integers such that 1 <= n, m <= 100. Additionally, the function should be able to handle multiple test cases, where the number of test cases, t, is a positive integer such that 1 <= t <= 100.
def func_1():
    n, m = map(int, input().split())
    if (n >= m) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: *The function takes two parameters, `n` and `m`, which are non-negative integers such that 1 <= n, m <= 100. Additionally, the function handles multiple test cases, where the number of test cases, `t`, is a positive integer such that 1 <= t <= 100. `n` and `m` are specific non-negative integers provided by the input, and the input is split into two integers. If `n` is greater than or equal to `m`, the current value of `n` is greater than or equal to the current value of `m`. If `n` is less than `m`, the current value of `n` is less than the current value of `m`.
#Overall this is what the function does:The function `func_1` reads two non-negative integers `n` and `m` from the user input, where 1 <= n, m <= 100. It then compares `n` and `m`. If `n` is greater than or equal to `m`, it prints 'Yes'. If `n` is less than `m`, it prints 'No'. The function does not handle multiple test cases or accept any parameters; it only processes a single input of two integers and prints the result of the comparison.

