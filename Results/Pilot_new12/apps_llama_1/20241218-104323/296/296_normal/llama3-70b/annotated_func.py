#State of the program right berfore the function call: n is a positive integer such that 2 <= n <= 10^9.
def func():
    n = int(input())
    if (n == 2) :
        print('NO')
    else :
        print('YES')
        k = 2
        print(k)
        print('1', n // 2)
        print('1', n)
    #State of the program after the if-else block has been executed: `n` is an input integer, if `n` is 2, then 'NO' has been printed. Otherwise, 'YES' has been printed, `k` is 2, 2 has been printed, '1' has been printed twice, `n // 2` has been printed, and '1' and the value of `n` have been printed, and `n` is not equal to 2.
#Overall this is what the function does:The function reads a positive integer `n` from user input, where `n` is expected to be between 2 and 10^9. If `n` is 2, it prints 'NO'. For any other `n`, it prints 'YES', followed by the number 2, and then two lines containing '1' and a number: the first line contains `n // 2` (integer division of `n` by 2), and the second line contains `n` itself. The function does not return any value (i.e., it implicitly returns None), and its primary action is to print specific output based on the input `n`. The function does not handle cases where the input `n` is not a positive integer within the specified range or is not a valid integer, which could lead to errors if such inputs are provided.

