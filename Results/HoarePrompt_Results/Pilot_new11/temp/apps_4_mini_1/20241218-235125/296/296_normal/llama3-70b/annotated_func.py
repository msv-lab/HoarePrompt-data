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
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 2 <= `n` <= 10^9. If `n` equals 2, then 'NO' has been printed. Otherwise, 'YES' has been printed, the value 2 has been printed, and the output is '1' followed by the current value of `n`.
#Overall this is what the function does:The function reads a positive integer `n` from input within the range 2 to 10^9. If `n` equals 2, it prints 'NO'. For all other values of `n`, it prints 'YES', followed by the number 2, and then outputs the string '1' along with the integer `n // 2`, and then again outputs '1' followed by the integer `n`. Note that there is no return value from the function and it does not accept any parameters. The function handles the edge case of `n` being exactly 2 distinctly from any other value of `n`. However, there are no checks or handling for values outside the specified range, which is stated to be between 2 and 10^9, should it not be guaranteed by the context of use.

