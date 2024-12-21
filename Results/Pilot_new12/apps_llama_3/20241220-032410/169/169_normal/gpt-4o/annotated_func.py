#State of the program right berfore the function call: n is a positive integer (1 <= n <= 100), and s is a string of length n consisting of '+' and '-' characters.
def func():
    n = int(input())
    s = input()
    stones = 0
    for operation in s:
        if operation == '+':
            stones += 1
        elif operation == '-':
            stones = max(0, stones - 1)
        
    #State of the program after the  for loop has been executed: `n` is the original input integer, `s` is the original input string, `operation` is the last character in `s`, and `stones` is the maximum of 0 and the sum of the number of '+' operations minus the number of '-' operations in `s`.
    print(stones)
#Overall this is what the function does:The function accepts a positive integer `n` and a string `s` of length `n` consisting of '+' and '-' characters, where `n` is input by the user and verified to be between 1 and 100, and it returns the net count of '+' operations after considering each '+' as an increment and each '-' as a decrement, but never going below 0. The function effectively calculates the maximum of 0 and the difference between the number of '+' characters and the number of '-' characters in the string `s`, ignoring the integer `n` for any calculations beyond ensuring it is a valid input length. After execution, the program prints this net count, and the state of the program concludes with `n` and `s` remaining unchanged from their initial input values, `operation` being the last character processed in `s`, and `stones` holding the final net count before being printed. The function handles edge cases such as when `s` contains only '-' characters or when the net count would be negative, ensuring the result is never less than 0.

