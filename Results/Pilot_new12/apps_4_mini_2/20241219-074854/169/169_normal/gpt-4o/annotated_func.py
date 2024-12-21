#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100, and s is a string of length n consisting only of the symbols "+" and "-".
def func():
    n = int(input())
    s = input()
    stones = 0
    for operation in s:
        if operation == '+':
            stones += 1
        elif operation == '-':
            stones = max(0, stones - 1)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 <= `n` <= 100, `s` is a string of length `n` consisting only of "+" and "-". `stones` is the net effect of all operations in `s`, where `stones` will be equal to the count of '+' minus the count of '-' but cannot be less than 0.
    print(stones)
#Overall this is what the function does:The function reads a positive integer `n` and a string `s` of length `n` composed solely of the characters "+" and "-". It calculates the resultant value of `stones` based on the operations encoded in `s`, where each "+" increases the count of `stones` by 1 and each "-" decreases `stones` by 1, ensuring that `stones` does not drop below 0. After processing all characters in `s`, the function outputs the final value of `stones`.

