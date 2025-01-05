#State of the program right berfore the function call: **Precondition**: n is an even integer such that 2 <= n <= 50. The ticket number is an integer of length n.
def func():
    if (__name__ == '__main__') :
        n = int(raw_input().strip())
        digits = map(int, raw_input().strip())
        if (sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:])) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *n is an even integer such that 2 <= n <= 50, digits is a map object containing integers obtained from the input after stripping any leading or trailing whitespaces. If the sum of the first half of digits is equal to the sum of the second half of digits when n is divided by 2, then the function executes the if part. Otherwise, the function executes the else part where the sum of the first half of digits is not equal to the sum of the second half of digits.
    #State of the program after the if block has been executed: *n is an even integer such that 2 <= n <= 50. The ticket number is an integer of length n. If the sum of the first half of digits is equal to the sum of the second half of digits when n is divided by 2, then the function maintains the initial state. Otherwise, the function maintains the initial state.
#Overall this is what the function does:The function does not accept any parameters explicitly. Within the function, it reads an integer `n` and a list of integers `digits` from the input. It then checks if the sum of the first half of `digits` is equal to the sum of the second half of `digits` when `n` is divided by 2. If the condition is met, it prints 'YES'; otherwise, it prints 'NO'. The function is intended to determine if a given ticket number is a lucky ticket number based on the sums of its digit halves. The preconditions state that `n` should be an even integer between 2 and 50, and the ticket number should be of length `n`.

