#State of the program right berfore the function call: k is an integer such that 1 ≤ k ≤ 5. The table of panels is represented as a 4x4 grid where each cell contains either a digit from 1 to 9 or a period.**
def func():
    n = input()
    c = [0] * 10
    for i in range(4):
        for j in list(raw_input()):
            if j != '.':
                c[int(j)] += 1
        
    #State of the program after the  for loop has been executed: k is an integer such that 1 ≤ k ≤ 5, the table of panels is represented as a 4x4 grid, c is a list containing 10 zeroes with values possibly incremented based on the non-period elements in the grid.
    print['NO', 'YES'][max(c) <= n * 2]
#Overall this is what the function does:The function `func` reads input and processes a 4x4 grid representing a table of panels where each cell contains either a digit from 1 to 9 or a period. It then checks if the maximum occurrence of any digit in the grid is less than or equal to twice the input value `n` and prints 'YES' or 'NO' accordingly.

