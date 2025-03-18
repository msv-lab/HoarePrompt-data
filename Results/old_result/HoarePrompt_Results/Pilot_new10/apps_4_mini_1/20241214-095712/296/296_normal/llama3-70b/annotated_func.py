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
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 2 <= `n` <= 10^9. If `n` is equal to 2, 'NO' is printed. Otherwise, when `n` is greater than 2, '1' and `n` are printed as output.
#Overall this is what the function does:The function prompts the user for an integer input `n`. If `n` is equal to 2, it prints 'NO'. For any value of `n` greater than 2 (up to 10^9), it prints 'YES', followed by the number 2, and then prints '1' along with the integer division of `n` by 2, and finally '1' followed by `n`. The function does not return any value.

