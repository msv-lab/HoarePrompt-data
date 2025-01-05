#State of the program right berfore the function call: n is an even integer such that 2 <= n <= 50.**
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *n is an even integer such that 2 <= n <= 50; digits is a list of integers representing each digit of n. If the sum of the digits in the first half of the list is equal to the sum of the digits in the second half of the list, the function returns 'YES'. Otherwise, the sums are unequal.
    #State of the program after the if block has been executed: *n is an even integer such that 2 <= n <= 50. Digits is a list of integers representing each digit of n. If the sum of the digits in the first half of the list is equal to the sum of the digits in the second half of the list, the function returns 'YES'. Otherwise, the sums are unequal.
#Overall this is what the function does:The function `func` does not accept any parameters. It reads an even integer `n` between 2 and 50 from the standard input. It then reads the digits of `n` into a list. If the sum of the digits in the first half of the list is equal to the sum of the digits in the second half of the list, it prints 'YES'. Otherwise, it prints 'NO'.

