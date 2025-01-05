#State of the program right berfore the function call: n is an even integer such that 2 <= n <= 50. The ticket number is an integer of length n.**
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *n is an even integer such that 2 <= n <= 50, the ticket number is an integer of length n, digits is assigned the map object resulting from converting the input using raw_input().strip() to integers. If the sum of the first half of the digits is equal to the sum of the second half of the digits (or the sum of the second half plus the last digit if n is odd), 'YES' is printed. Otherwise, the sum of the first half of the digits is not equal to the sum of the second half of the digits.
    #State of the program after the if block has been executed: *n is an even integer such that 2 <= n <= 50, the ticket number is an integer of length n. Digits is assigned the map object resulting from converting the input using raw_input().strip() to integers. If the sum of the first half of the digits is equal to the sum of the second half of the digits (or the sum of the second half plus the last digit if n is odd), 'YES' is printed. Otherwise, the sum of the first half of the digits is not equal to the sum of the second half of the digits.
#Overall this is what the function does:The function `func` reads an even integer `n` such that 2 <= n <= 50 from the user input. It then reads a ticket number as a list of integers of length `n`. The function calculates the sum of the first half of the digits and compares it with the sum of the second half (or the sum of the second half plus the last digit if `n` is odd). If the sums are equal, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value, and it appears incomplete as it lacks a return statement.

