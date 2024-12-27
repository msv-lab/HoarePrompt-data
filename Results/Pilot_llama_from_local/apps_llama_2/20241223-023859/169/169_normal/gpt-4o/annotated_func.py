#State of the program right berfore the function call: The input to the function will be provided through the standard input, consisting of a positive integer $n$ (1 <= n <= 100) on the first line, followed by a string $s$ of length $n$ containing only '-' and '+' characters, representing the sequence of operations performed by Vasya.
def func():
    n = int(input())
    s = input()
    stones = 0
    for operation in s:
        if operation == '+':
            stones += 1
        elif operation == '-':
            stones = max(0, stones - 1)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 1 and 100 (inclusive), `s` is the input string, `operation` is the last character of `s`, and `stones` is the maximum of 0 and the difference between the counts of '+' and '-' in `s`.
    print(stones)
#Overall this is what the function does:The function accepts a positive integer $n$ and a string $s$ of length $n$ containing '-' and '+' characters, and it calculates the final count of stones after processing the string based on the operations represented by the characters, where '+' increments the stone count and '-' decrements it, ensuring the count does not go below 0. The function then prints this final stone count. The final state of the program after it concludes includes the input integer $n$ and string $s$ being consumed, and the final stone count being printed to the standard output.

