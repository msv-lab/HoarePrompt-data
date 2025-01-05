#State of the program right berfore the function call: n is an even integer such that 2 ≤ n ≤ 50, and the ticket number is a positive integer with exactly n digits, which may include leading zeros and contains only the digits 4 and 7.
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is an even integer that has been assigned a positive integer value from input, and `digits` is a map object that produces integers from the input. If the sum of the first half of the integers produced by `digits` equals the sum of the second half, the output is 'YES'. Otherwise, if the sums are not equal, 'NO' is printed.
    #State of the program after the if block has been executed: *`n` is an even integer within the range of 2 to 50, and the ticket number consists of exactly `n` digits made up of the digits 4 and 7. If the sum of the first half of the digits equals the sum of the second half, the output is 'YES'. Otherwise, the output is 'NO'.
#Overall this is what the function does:The function accepts an even integer `n` (2 ≤ n ≤ 50) that represents the number of digits in a ticket number, which must consist solely of the digits 4 and 7. It reads the digits of the ticket number as input and checks if the sum of the first half of the digits equals the sum of the second half. It outputs 'YES' if the sums are equal and 'NO' otherwise. However, the function does not handle invalid inputs (e.g., non-digit characters) or check if the digits are strictly 4s and 7s, which could lead to unexpected behavior.

