#State of the program right berfore the function call: n is an even integer such that 2 ≤ n ≤ 50, and the ticket number is a positive integer represented as a string of length exactly n containing only the digits 4 and 7.
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is an even integer such that 2 ≤ `n` ≤ 50, and `digits` is a map object of integers from the input. If the sum of the first half of `digits` equals the sum of the second half, 'YES' is printed. Otherwise, 'NO' is printed.
    #State of the program after the if block has been executed: *`n` is an even integer such that 2 ≤ `n` ≤ 50, and `digits` is a map object of integers derived from a ticket number represented as a string of length exactly `n` containing only the digits 4 and 7. If the sum of the first half of `digits` equals the sum of the second half, 'YES' is printed. Otherwise, 'NO' is printed.
#Overall this is what the function does:The function accepts an even integer `n` (2 ≤ n ≤ 50) and a ticket number represented as a string of exactly `n` digits, which can only be '4' and '7'. It checks if the sum of the first half of the digits equals the sum of the second half. If they are equal, it prints 'YES'; otherwise, it prints 'NO'. However, if the input does not strictly adhere to the specified format (i.e., the ticket number must contain only '4' and '7'), the function does not handle such cases or provide any errors or warnings. Additionally, the function does not return any value; it only prints the result.

