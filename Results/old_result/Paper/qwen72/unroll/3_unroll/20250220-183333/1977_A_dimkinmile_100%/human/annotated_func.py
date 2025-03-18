#State of the program right berfore the function call: The function should actually be defined with parameters `n` and `m` as described in the problem, so the correct function definition should be `def func_1(n, m):` where `n` and `m` are integers such that 1 <= n, m <= 100.
def func_1():
    n, m = map(int, input().split())
    if ((n - m) % 2 == 0 and n - m >= 0) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: *`n` and `m` are integers provided by the user, with 1 <= n, m <= 100. If `(n - m) % 2 == 0` and `n - m >= 0`, the difference `n - m` is a non-negative even number. Otherwise, either `(n - m) % 2 != 0` or `n - m < 0`.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads two integers `n` and `m` from user input, where both integers are expected to be between 1 and 100 inclusive. The function then checks if the difference `n - m` is a non-negative even number. If the condition is met, it prints 'Yes'; otherwise, it prints 'No'. After the function concludes, the state of the program is that `n` and `m` are the integers provided by the user, and either 'Yes' or 'No' has been printed to the console.

