#State of the program right berfore the function call: n is an even integer such that 2 <= n <= 50. The ticket number is an integer of length n.**
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is an even integer such that 2 <= n <= 50, `digits` is a list of n integers. If the sum of the first half of `digits` is equal to the sum of the second half of `digits`, then the program will return. Otherwise, the program will execute the else part and the sum of the first half of `digits` will not be equal to the sum of the second half of `digits`.
    #State of the program after the if block has been executed: *`n` is an even integer such that 2 <= n <= 50 and the ticket number is an integer of length n. `digits` is a list of n integers. If the sum of the first half of `digits` is equal to the sum of the second half of `digits`, then the program will return. Otherwise, the program will not return and the sum of the first half of `digits` will not be equal to the sum of the second half of `digits`.
#Overall this is what the function does:Functionality: The function `func` reads an even integer `n` from the user input and then reads a list of `n` integers. It checks if the sum of the first half of the list is equal to the sum of the second half. If they are equal, it prints 'YES', otherwise, it prints 'NO'. The function does not return any value. However, there is a missing edge case where the code does not handle the situation if `n` is odd.

