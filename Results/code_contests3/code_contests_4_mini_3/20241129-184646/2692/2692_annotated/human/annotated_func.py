#State of the program right berfore the function call: n is an even integer such that 2 ≤ n ≤ 50, and the ticket number is a positive integer of exactly n digits, which contains only the digits 4 and 7.
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is an even integer such that 2 ≤ `n` ≤ 50; `digits` is a sequence of integers. If the sum of the first half of `digits` is equal to the sum of the second half, 'YES' is printed. Otherwise, if the sums are not equal, 'NO' is printed.
    #State of the program after the if block has been executed: *`n` is an even integer such that 2 ≤ `n` ≤ 50, and `digits` is a sequence of integers. If the sum of the first half of `digits` equals the sum of the second half, 'YES' is printed; otherwise, 'NO' is printed.
#Overall this is what the function does:The function accepts an even integer `n` (2 ≤ n ≤ 50) and expects a sequence of digits that must be exactly `n` digits long, containing only the digits 4 and 7. It calculates the sum of the first half of these digits and compares it to the sum of the second half. If the two sums are equal, it prints 'YES'; otherwise, it prints 'NO'. However, it does not validate whether the input digits only contain 4s and 7s. If the input does not strictly adhere to this requirement, the function may produce unexpected results.

