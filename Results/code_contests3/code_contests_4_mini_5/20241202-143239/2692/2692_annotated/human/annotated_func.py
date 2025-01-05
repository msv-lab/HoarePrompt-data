#State of the program right berfore the function call: n is an even integer such that 2 ≤ n ≤ 50, and the ticket number is a positive integer represented as a string of length exactly n, containing only the digits 4 and 7.
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is a positive integer obtained from input, the ticket number is a string of length exactly `n`, containing only the digits 4 and 7; `digits` is a map object containing the integer values of the digits from the input string. If the sum of the first half of `digits` equals the sum of the second half, 'YES' is printed. Otherwise, 'NO' is printed.
    #State of the program after the if block has been executed: *`n` is an even integer such that 2 ≤ `n` ≤ 50, and the ticket number is a string of length exactly `n`, containing only the digits 4 and 7. If the sum of the first half of the digits equals the sum of the second half, 'YES' is printed; otherwise, 'NO' is printed.
#Overall this is what the function does:The function accepts an even integer `n` (where 2 ≤ n ≤ 50) and reads a ticket number represented as a string of length `n`, which contains only the digits 4 and 7. It then checks if the sum of the first half of the digits is equal to the sum of the second half of the digits. If they are equal, it prints 'YES'; otherwise, it prints 'NO'. The function does not handle cases where the input is not as specified (for example, if `n` is odd or outside the specified range, or if the ticket number contains digits other than 4 and 7).

