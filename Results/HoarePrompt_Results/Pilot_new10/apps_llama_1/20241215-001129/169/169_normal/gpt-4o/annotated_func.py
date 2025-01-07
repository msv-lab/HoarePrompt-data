#State of the program right berfore the function call: The input to the function will be a positive integer n and a string s of length n consisting of only '+' and '-' characters, where n is in the range 1 <= n <= 100.
def func():
    n = int(input())
    s = input()
    stones = 0
    for operation in s:
        if operation == '+':
            stones += 1
        elif operation == '-':
            stones = max(0, stones - 1)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer in the range 1 <= `n` <= 100, `s` is a string equal to the user's input, `stones` is the maximum of 0 and the difference between the number of '+' operations and the number of '-' operations in `s`.
    print(stones)
#Overall this is what the function does:The function reads an integer `n` and a string `s` of length `n` from the user, consisting of only '+' and '-' characters, and prints the maximum of 0 and the difference between the number of '+' operations and the number of '-' operations in `s`.

