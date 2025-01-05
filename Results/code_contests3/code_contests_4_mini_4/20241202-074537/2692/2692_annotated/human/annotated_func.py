#State of the program right berfore the function call: n is an even integer such that 2 ≤ n ≤ 50, and the ticket number is a positive integer represented as a string of exactly n digits containing only the digits 4 and 7.
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is an even integer such that 2 ≤ n ≤ 50; `digits` is a map object containing integers from the input string. If the sum of the first half of the digits equals the sum of the second half, 'YES' is printed. Otherwise, 'NO' is printed.
    #State of the program after the if block has been executed: *`n` is an even integer such that 2 ≤ n ≤ 50, and `digits` is a map object containing integers from the input string. If the sum of the first half of the digits equals the sum of the second half, 'YES' is printed; otherwise, 'NO' is printed.
#Overall this is what the function does:The function reads an even integer `n` (where 2 ≤ n ≤ 50) and a string of exactly `n` digits containing only the digits 4 and 7. It then checks if the sum of the first half of the digits equals the sum of the second half, printing 'YES' if they are equal and 'NO' otherwise. It should be noted that the code does not handle invalid input cases (e.g., if the digits contain numbers other than 4 and 7, or if the input string is not exactly `n` digits long).

