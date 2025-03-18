#State of the program right berfore the function call: The function `func_1` is expected to take two parameters, `n` and `m`, where both `n` and `m` are integers such that 1 ≤ n, m ≤ 100. The function should be able to handle multiple test cases, where the number of test cases `t` is an integer such that 1 ≤ t ≤ 100.
def func_1():
    n, m = map(int, input().split())
    if (n >= m) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: *`n` and `m` are integers such that 1 ≤ n, m ≤ 100, and `t` is an integer such that 1 ≤ t ≤ 100. `n` and `m` are assigned the values from the input, which are split and converted to integers. If `n` is greater than or equal to `m`, then `n` is greater than or equal to `m`. Otherwise, `n` is less than `m`.
#Overall this is what the function does:The function `func_1` reads two integers, `n` and `m`, from the user input, where both integers are expected to be between 1 and 100. It then compares `n` and `m`. If `n` is greater than or equal to `m`, it prints 'Yes'. Otherwise, it prints 'No'. The function does not return any value and does not handle multiple test cases as described in the annotations. After the function concludes, `n` and `m` retain their values from the input, and the program state is unchanged except for the printed output.

