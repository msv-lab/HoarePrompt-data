#State of the program right berfore the function call: n is a positive even integer such that 2 <= n <= 50. The second line contains an integer of length n.**
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *n is a positive even integer such that 2 <= n <= 50; digits is a list of integers extracted from the input string. If the sum of the first half of digits is equal to the sum of the second half of digits, then the function executes the if part. Otherwise, the function executes the else part.
    #State of the program after the if block has been executed: *n is a positive even integer such that 2 <= n <= 50, digits is a list of integers extracted from the input string. If the sum of the first half of digits is equal to the sum of the second half of digits, then the function continues with the if part. Otherwise, the function terminates.
#Overall this is what the function does:The function `func` reads an integer `n` and a sequence of integers of length `n` from the user. It then compares whether the sum of the first half of the sequence is equal to the sum of the second half. If the sums are equal, it prints 'YES'; otherwise, it prints 'NO'. The function does not accept any parameters explicitly but relies on user input for `n` and the sequence of integers.

