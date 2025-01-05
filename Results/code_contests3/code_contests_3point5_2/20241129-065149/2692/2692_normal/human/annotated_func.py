#State of the program right berfore the function call: n is an even integer such that 2 <= n <= 50.**
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *n is an even integer within the range 2 to 50, digits is a map object containing the integer values of the input string after stripping. If the sum of the first half of digits is equal to the sum of the second half of digits when n is divided by 2, then the function executes the if part. Otherwise, if the sums are not equal, then the function executes the else part.
    #State of the program after the if block has been executed: *n is an even integer within the range 2 to 50. Digits is a map object containing the integer values of the input string after stripping. If the sum of the first half of digits is equal to the sum of the second half of digits when n is divided by 2, the function executes the if part. If the sums are not equal, the function executes the else part.
#Overall this is what the function does:The function reads an even integer n within the range of 2 to 50 from the input and a string of digits. It then checks if the sum of the first half of the digits is equal to the sum of the second half of the digits when split at n/2. If the sums are equal, it prints 'YES'; otherwise, it prints 'NO'.

