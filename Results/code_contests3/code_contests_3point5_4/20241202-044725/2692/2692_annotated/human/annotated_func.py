#State of the program right berfore the function call: n is an even integer such that 2 <= n <= 50. The ticket number is an integer of length n.**
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *n is an even integer such that 2 <= n <= 50, the ticket number is an integer of length n, __name__ is equal to '__main__', digits is a map object containing integers from the input after stripping. If the sum of the first half of digits is equal to the sum of the second half of digits, then 'YES' is printed. Otherwise, 'NO' is printed and there are no changes to the initial state variables.
    #State of the program after the if block has been executed: *n is an even integer such that 2 <= n <= 50, the ticket number is an integer of length n, __name__ is equal to '__main__', digits is a map object containing integers from the input after stripping. If the sum of the first half of digits is equal to the sum of the second half of digits, then 'YES' is printed. Otherwise, 'NO' is printed. No changes are made to the initial state variables.
#Overall this is what the function does:The function reads an even integer n and a ticket number as input. It then checks if the sum of the first half of the ticket number digits is equal to the sum of the second half. If they are equal, it prints 'YES'; otherwise, it prints 'NO'.

