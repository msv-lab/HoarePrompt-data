#State of the program right berfore the function call: n is an integer such that 13 ≤ n < 10^5 and n is odd. The string s is a sequence of n digits.
def func():
    n = int(input().strip())

s = input().strip()

moves = (n - 11) // 2

count_8 = s[:n - 11].count('8')
    if (count_8 > moves) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an integer, `s` is a string, `moves` is equal to `(n - 11) // 2`, and `count_8` is the count of '8' in the substring `s[:n - 11]`. If `count_8` is greater than `moves`, the function prints 'YES'. Otherwise, the function prints 'NO'.
#Overall this is what the function does:The function takes an integer `n` (where 13 ≤ n < 10^5 and n is odd) and a string `s` consisting of `n` digits as input. It then calculates the number of moves required based on `n`, which is given by `(n - 11) // 2`. The function counts the occurrences of the digit '8' in the substring of `s` starting from the beginning up to the index `n - 11`. Depending on whether the count of '8's is greater than the calculated number of moves, the function prints either 'YES' or 'NO'. An edge case to consider is when `n` is exactly 13, in which case the substring `s[:n - 11]` would be empty, resulting in `count_8` being 0. Another edge case is when `n` approaches 10^5, the calculation of `moves` should ensure it remains within the valid range. The function does not handle invalid inputs or non-digit characters in the string `s`.

