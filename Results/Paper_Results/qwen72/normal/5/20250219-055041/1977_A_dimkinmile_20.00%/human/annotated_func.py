#State of the program right berfore the function call: The function should take two parameters, n and m, where n and m are integers such that 1 <= n, m <= 100.
def func_1():
    n, m = map(int, input().split())
    if (n >= m) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: *`n` and `m` are input integers such that 1 <= n, m <= 100. If `n` is greater than or equal to `m`, the program retains the values of `n` and `m`. If `n` is less than `m`, the program also retains the values of `n` and `m`.
#Overall this is what the function does:The function `func_1` reads two integers, `n` and `m`, from user input, where both integers are expected to be between 1 and 100, inclusive. It then compares `n` and `m`. If `n` is greater than or equal to `m`, it prints 'Yes'; otherwise, it prints 'No'. After the function concludes, the values of `n` and `m` remain unchanged and are retained in the program.

