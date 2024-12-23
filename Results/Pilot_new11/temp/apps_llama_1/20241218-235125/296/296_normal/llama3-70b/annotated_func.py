#State of the program right berfore the function call: n is a positive integer greater than or equal to 2 and less than or equal to 10^9.
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
    #State of the program after the if-else block has been executed: `n` is an input integer, if `n` equals 2, then 'NO' has been printed. If `n` is not equal to 2, then 'YES', 2, '1' twice, `n // 2`, and `n` have been printed to the console, and `k` is 2.
#Overall this is what the function does:The function reads a positive integer `n` from the user, checks if it equals 2, and based on this condition, prints either 'NO' or 'YES' along with additional numbers if `n` is not 2. If `n` is 2, the program only prints 'NO'. If `n` is any other positive integer greater than or equal to 2 and less than or equal to 10^9, it prints 'YES', the number 2, and two pairs of numbers: '1' followed by `n // 2`, and '1' followed by `n`. The function does not return any values but modifies the console output. It handles all positive integer inputs within the specified range but does not include error handling for non-integer or out-of-range inputs.

