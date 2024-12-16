#State of the program right berfore the function call: n is a positive integer greater than 1.
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
    #State of the program after the if-else block has been executed: `n` is an input integer, if `n` is equal to 2, then 'NO' has been printed. If `n` is not equal to 2, then 'YES', 2, '1', `n // 2`, '1', and `n` have been printed, and `k` is 2.
#Overall this is what the function does:The function takes an integer `n` as input from the user, checks if `n` is equal to 2 and prints 'NO' if true, otherwise prints 'YES', 2, '1' and `n // 2`, and '1' and `n`, but does not return any value.

