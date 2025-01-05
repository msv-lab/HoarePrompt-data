#State of the program right berfore the function call: n is an even integer such that 2 ≤ n ≤ 50, and the ticket number is a positive integer with exactly n digits, which only contains the digits 4 and 7.
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is a positive even integer such that 2 ≤ `n` ≤ 50; `digits` is a mapped list of integers. If the sum of the first half of the elements in `digits` is equal to the sum of the second half, 'YES' is printed. Otherwise, 'NO' is printed.
    #State of the program after the if block has been executed: *`n` is an even integer such that 2 ≤ `n` ≤ 50, and `digits` is a list of integers mapped from a ticket number that contains exactly `n` digits of 4 and 7. If the sum of the first half of the elements in `digits` equals the sum of the second half, 'YES' is printed; otherwise, 'NO' is printed.
#Overall this is what the function does:The function accepts an even integer `n` (where 2 ≤ n ≤ 50) and reads a ticket number with exactly `n` digits, which must consist only of the digits 4 and 7. It then checks if the sum of the first half of the digits equals the sum of the second half. If they are equal, it prints 'YES'; otherwise, it prints 'NO'. The function does not explicitly handle cases where the input does not meet the specified requirements (e.g., if the digits contain numbers other than 4 and 7 or if `n` is not even).

