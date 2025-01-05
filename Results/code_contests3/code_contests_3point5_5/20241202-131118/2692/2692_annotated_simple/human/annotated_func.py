#State of the program right berfore the function call: n is an even integer such that 2 <= n <= 50. The second line contains an integer of length n.**
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *n is an even integer such that 2 <= n <= 50, digits is a map object containing integers after converting input by stripping any leading and trailing whitespaces. If the sum of the first half of digits is equal to the sum of the second half of digits, then the function performs some specific action. Otherwise, 'NO' is printed.
    #State of the program after the if block has been executed: *n is an even integer such that 2 <= n <= 50, digits is a map object containing integers after converting input by stripping any leading and trailing whitespaces. If the sum of the first half of digits is equal to the sum of the second half of digits, then the function performs some specific action. Otherwise, 'NO' is printed.
#Overall this is what the function does:The function `func` reads an even integer `n` from the input within the range 2 to 50, followed by a list of integers of length `n`. It then checks if the sum of the first half of the list is equal to the sum of the second half. If the sums are equal, it prints 'YES'; otherwise, it prints 'NO'. The exact task performed based on the sum equality is not specified in the given information.

