#State of the program right berfore the function call: The function should accept two parameters, n and m, where n and m are integers such that 1 ≤ n, m ≤ 100.
def func_1():
    n, m = map(int, input().split())
    if (n >= m) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: *`n` and `m` are integers provided by the user, where 1 ≤ n, m ≤ 100. If `n` is greater than or equal to `m`, the program retains the values of `n` and `m`. If `n` is less than `m`, the program also retains the values of `n` and `m`.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads two integers, `n` and `m`, from user input, where 1 ≤ n, m ≤ 100. After reading the input, the function prints 'Yes' if `n` is greater than or equal to `m`, and prints 'No' if `n` is less than `m`. The function does not return any value. After the function concludes, the values of `n` and `m` are retained in the program.

