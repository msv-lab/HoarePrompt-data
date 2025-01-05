#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 1000.**
def func():
    n, m = map(int, sys.stdin.readline().split())
    print(n * m) / 2
#Overall this is what the function does:The function `func` reads two integers `n` and `m` from the input and prints their product divided by 2. However, the code has an issue where it tries to perform division on the result of `n * m` and prints the result, which might lead to a syntax error due to the missing parentheses. The function does not have any explicit return value or output other than the printed result of the division. Additionally, the function lacks error handling for cases where the input values are not valid positive integers.

