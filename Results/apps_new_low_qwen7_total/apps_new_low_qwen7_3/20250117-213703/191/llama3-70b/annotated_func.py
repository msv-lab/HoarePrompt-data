#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 1000, and a 2D list stars representing the star map where each element is either '.' or '*' indicating empty space or a star respectively.
def func():
    n, m = map(int, input().split())

stars = []
    for _ in range(n):
        row = input()
        
        for j, c in enumerate(row):
            if c == '*':
                stars.append((j, _))
        
    #State of the program after the  for loop has been executed: Output State: `n` is a positive integer, `m` is a positive integer, `stars` is a list of tuples where each tuple contains the index and the asterisk character from each row where an asterisk was found. Each tuple in `stars` has the form `(j, '*')` where `j` is the index of the asterisk in its respective row, and the rows are processed up to `n` times. The variable `row` is the last non-empty string read during the loop, and `j` is the index of the last asterisk character found in `row`. If no asterisks are found in any row, `stars` will be an empty list. The loop does not execute if `n` is less than or equal to 0.
    min_x = min(x for x, y in stars)

max_x = max(x for x, y in stars)

min_y = min(y for x, y in stars)

max_y = max(y for x, y in stars)

side = max(max_x - min_x + 1, max_y - min_y + 1)

print(side)
#Overall this is what the function does:The function processes a star map represented as a 2D list where each element is either '.' or '*', indicating empty space or a star respectively. It reads the dimensions of the star map from user input, constructs a list of coordinates for all stars found in the map, and then calculates the side length of the smallest square that can contain all the stars. If no stars are found, the function returns a side length of 1. The function does not modify the original input but rather uses the input to derive the required output.

