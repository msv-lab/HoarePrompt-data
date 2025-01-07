#State of the program right berfore the function call: The input consists of two lines. The first line contains a positive integer n (1 ≤ n ≤ 100) representing the number of operations. The second line contains a string s of length n, where each character is either "-" (indicating removing a stone) or "+" (indicating adding a stone).
def func():
    n = int(input())
    s = input()
    stones = 0
    for operation in s:
        if operation == '+':
            stones += 1
        elif operation == '-':
            stones = max(0, stones - 1)
        
    #State of the program after the  for loop has been executed: `n` is an integer, `s` is a non-empty string consisting of `n` characters either "-" or "+", and `stones` is the final value calculated based on the operations in `s`. If the first character in `s` is '+', `stones` will be the count of '+' operations minus the count of '-' operations (considering the initial value of `stones` as 0). If the first character in `s` is '-', `stones` will be the count of '+' operations minus the count of '-' operations, ensuring `stones` is never less than 0.
    print(stones)
#Overall this is what the function does:The function `func` reads two lines of input from the user. The first line is a positive integer `n` (1 ≤ n ≤ 100) representing the number of operations, and the second line is a string `s` of length `n` consisting of characters either "-" (indicating removing a stone) or "+" (indicating adding a stone). The function then iterates through each character in `s`, updating the count of stones based on the operations specified. If an operation is "+", one stone is added, and if it is "-", one stone is removed, ensuring the stone count does not go below zero. After processing all operations, the function prints the final net number of stones. This function does not return a value explicitly but modifies the state by printing the result. Potential edge cases include the first character being "-", which still ensures the stone count does not drop below zero.

