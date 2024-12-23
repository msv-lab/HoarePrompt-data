#State of the program right berfore the function call: $n$ is a positive integer such that $1 \leq n \leq 100$, and $s$ is a string of length $n$ consisting only of "-" and "+".
def func():
    n = int(input())
    s = input()
    stones = 0
    for operation in s:
        if operation == '+':
            stones += 1
        elif operation == '-':
            stones = max(0, stones - 1)
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string, `n` is the integer value of the input, and for every `operation` in `s`, if `operation` is '+', `stones` is incremented by 1. If `operation` is '-', `stones` is decremented by `n`. Otherwise, the value of `stones` remains unchanged.
    print(stones)
#Overall this is what the function does:The function `func()` accepts no explicit parameters but reads two inputs from the user: an integer `n` (where \(1 \leq n \leq 100\)) and a string `s` of length `n` consisting only of "-" and "+". It then iterates through each character in the string `s`. For each '+', it increments the counter `stones` by 1. For each '-', it decrements `stones` by 1. After processing all characters in `s`, it prints the final value of `stones`. The function does not handle any edge cases explicitly mentioned in the annotations, such as invalid input types or lengths outside the specified range. However, since the function reads inputs directly from the user, it implicitly relies on valid input.

