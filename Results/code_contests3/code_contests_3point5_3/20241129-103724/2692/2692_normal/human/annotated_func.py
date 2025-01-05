#State of the program right berfore the function call: n is an even integer such that 2 <= n <= 50.**
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is an even integer such that 2 <= n <= 50. If the sum of the first half of the digits in the list is equal to the sum of the second half of the digits, then the function returns the sums of both halves. Otherwise, the function returns 'NO'.
    #State of the program after the if block has been executed: *n is an even integer such that 2 <= n <= 50. If the sum of the first half of the digits in the list is equal to the sum of the second half of the digits, then the function returns the sums of both halves. Otherwise, the function returns 'NO'.
#Overall this is what the function does:The function `func` does not accept any parameters. It reads an integer `n` from the user input and a list of digits. It then checks if the sum of the first half of the digits is equal to the sum of the second half of the digits. If the condition is met, it prints 'YES', otherwise it prints 'NO'. The function is expected to handle cases where `n` is an even integer between 2 and 50.

