#State of the program right berfore the function call: The function should take two parameters, n and m, where n and m are integers such that 1 <= n, m <= 100.
def func_1():
    n, m = map(int, input().split())
    if (n >= m) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: *`n` and `m` are integers provided by the user, where 1 <= n, m <= 100. If `n` is greater than or equal to `m`, the current value of `n` is greater than or equal to the current value of `m`. If `n` is less than `m`, the current value of `n` is less than the current value of `m`.
#Overall this is what the function does:The function `func_1` reads two integers `n` and `m` from user input, where 1 <= n, m <= 100. It then compares these integers and prints 'Yes' if `n` is greater than or equal to `m`, and prints 'No' if `n` is less than `m`. The function does not return any value. After the function concludes, the state of the program includes the printed result ('Yes' or 'No') based on the comparison of `n` and `m`.

