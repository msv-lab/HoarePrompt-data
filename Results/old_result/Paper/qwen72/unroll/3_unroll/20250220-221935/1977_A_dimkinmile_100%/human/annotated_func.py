#State of the program right berfore the function call: The function should take two parameters, n and m, where n and m are integers such that 1 ≤ n, m ≤ 100. The function should also be able to handle multiple test cases, where the number of test cases t is an integer such that 1 ≤ t ≤ 100.
def func_1():
    n, m = map(int, input().split())
    if ((n - m) % 2 == 0 and n - m >= 0) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: *The function takes two parameters, `n` and `m`, where `n` and `m` are integers such that 1 ≤ n, m ≤ 100. The function can handle multiple test cases, where the number of test cases `t` is an integer such that 1 ≤ t ≤ 100. `n` and `m` are assigned the values from the input, which is a space-separated string of two integers. If `(n - m) % 2 == 0` and `n - m >= 0`, then the difference between `n` and `m` is even and non-negative, meaning `n - m` is even and `n` is greater than or equal to `m`. Otherwise, either `(n - m) % 2 != 0` or `n - m < 0`.
#Overall this is what the function does:The function `func_1` reads two integers `n` and `m` from the user input, where `1 ≤ n, m ≤ 100`. It checks if the difference between `n` and `m` is even and non-negative. If both conditions are met, it prints 'Yes'; otherwise, it prints 'No'. The function does not return any value. After the function concludes, the program state is such that the input values `n` and `m` have been processed and the appropriate message has been printed based on the conditions.

