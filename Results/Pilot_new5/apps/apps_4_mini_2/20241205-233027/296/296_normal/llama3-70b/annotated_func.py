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
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 2 <= n <= 10^9. If `n` is equal to 2, 'NO' is printed. Otherwise, if `n` is greater than 2, the value 2 is printed, followed by '1' and the value of `n`.
#Overall this is what the function does:The function accepts a positive integer `n` through user input within the range of 2 to 10^9. It prints 'NO' if `n` is equal to 2. For any value of `n` greater than 2, it prints 'YES', followed by the integer 2, and then prints '1' along with the integer value of `n` divided by 2, and finally prints '1' along with the integer `n`. No values are returned from the function.

