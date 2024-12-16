#State of the program right berfore the function call: The input is a string s of length n, where 1 ≤ n ≤ 100, consisting of '-' and '+' characters. Each '-' represents an operation where Vasya takes one stone from the pile, and each '+' represents an operation where Vasya adds one stone to the pile. The pile is non-empty before each operation of taking one stone from the pile.
def func():
    n = int(input())
    s = input()
    stones = 0
    for operation in s:
        if operation == '+':
            stones += 1
        elif operation == '-':
            stones = max(0, stones - 1)
        
    #State of the program after the  for loop has been executed: `n` is an integer representing the original length of the string `s`, `s` is a string of length `n` consisting of '-' and '+' characters (after removing all operations), and `stones` is the net count of '+' operations minus the net count of '-' operations performed on the string `s`.
    print(stones)
#Overall this is what the function does:The function accepts a string `s` consisting of '-' and '+' characters and prints the final count of stones in the pile after performing all operations. If `stones` is 0 after processing all operations, the pile is empty, and if `stones` is not 0, the pile contains `stones` number of stones.

