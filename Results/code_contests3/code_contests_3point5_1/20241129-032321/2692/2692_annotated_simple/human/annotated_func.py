#State of the program right berfore the function call: n is an even integer such that 2 <= n <= 50.**
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *n is an even integer such that 2 <= n <= 50; digits is a map object containing the integer values of the characters in the input string. If the sum of the first half of the digits array is equal to the sum of the second half of the digits array, then the function's behavior is unspecified. Otherwise, if the sum of the first half of digits is not equal to the sum of the second half of digits, 'NO' is printed.
    #State of the program after the if block has been executed: *n is an even integer such that 2 <= n <= 50. The digits array contains the integer values of the characters in the input string. If the sum of the first half of the digits array is equal to the sum of the second half of the digits array, the function's behavior is unspecified. If the sum of the first half of digits is not equal to the sum of the second half of digits, 'NO' is printed.
#Overall this is what the function does:The function reads an even integer `n` from the input, along with a list of integers represented by `digits`. It then checks if the sum of the first half of the `digits` array is equal to the sum of the second half. If the sums are equal, the function's behavior is unspecified. If the sums are not equal, it prints 'NO'.

