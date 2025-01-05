#State of the program right berfore the function call: n is an even integer such that 2 ≤ n ≤ 50, and the ticket number is a positive integer of length exactly n, containing only the digits 4 and 7.
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is an even integer such that 2 ≤ `n` ≤ 50; `digits` holds the mapped integers from the input. If the sum of the first half of the elements in `digits` is equal to the sum of the remaining elements, 'YES' is printed. Otherwise, 'NO' is printed.
    #State of the program after the if block has been executed: *`n` is an even integer such that 2 ≤ `n` ≤ 50; if the sum of the first half of the elements in `digits` is equal to the sum of the remaining elements, 'YES' is printed. Otherwise, 'NO' is printed.
#Overall this is what the function does:The function accepts an even integer `n` (where 2 ≤ n ≤ 50) and expects a ticket number as input, which is a series of digits of length `n` containing only the digits 4 and 7. It checks if the sum of the first half of the digits equals the sum of the second half. If they are equal, it prints 'YES'; otherwise, it prints 'NO'. However, the function does not handle cases where the input does not strictly contain only the digits 4 and 7, nor does it validate the length of the digits against `n` before performing calculations.

