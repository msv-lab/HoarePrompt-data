#State of the program right berfore the function call: n is an even integer such that 2 ≤ n ≤ 50, and the ticket number is a positive integer represented as a string of length n consisting of digits, which may include leading zeros. The ticket number must contain only the lucky digits 4 and 7.
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is an even integer such that 2 ≤ n ≤ 50; `digits` is a list of integers obtained from mapping int over the input from raw_input(). If the sum of the first half of `digits` equals the sum of the second half, then 'YES' is printed. Otherwise, 'NO' is printed.
    #State of the program after the if block has been executed: *`n` is an even integer such that 2 ≤ n ≤ 50, and `digits` is a list of integers derived from the input ticket number, which is a positive integer represented as a string of length `n`, containing only the lucky digits 4 and 7. If the sum of the first half of `digits` equals the sum of the second half, 'YES' is printed; otherwise, 'NO' is printed.
#Overall this is what the function does:The function accepts an even integer `n` (where 2 ≤ n ≤ 50) and a ticket number, represented as a string of length `n`, which must consist solely of the digits 4 and 7. It checks if the sum of the first half of the digits is equal to the sum of the second half. If they are equal, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value, it only prints the result based on the condition. Additionally, there is a potential edge case if the input does not meet the specified constraints (e.g., if `n` is not even or if the ticket number contains digits other than 4 and 7), which is not handled in the code.

