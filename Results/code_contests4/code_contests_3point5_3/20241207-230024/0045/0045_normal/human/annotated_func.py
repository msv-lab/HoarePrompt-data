#State of the program right berfore the function call: n is an integer such that 0 <= n <= 52. Each card is represented by a character and an integer, where the character represents the suit ('S', 'H', 'C', 'D') and the integer represents the rank (1 to 13).**
def func_1():
    n = int(input())
    d = {'S': [None] * 13, 'H': [None] * 13, 'C': [None] * 13, 'D': [None] * 13}
    for i in range(n):
        x, y = raw_input().split()
        
        d[x][int(y) - 1] = True
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, n is greater than 0, dictionary d has all four suits 'S', 'H', 'C', 'D' with a list of 13 boolean values for each suit indicating whether the corresponding card is True or not, x and y are assigned values from the last input split
    for k in ['S', 'H', 'C', 'D']:
        for i in range(13):
            if d[k][i]:
                continue
            print('%s %d' % (k, i + 1))
        
    #State of the program after the  for loop has been executed: All boolean values in `d` are True for each suit 'S', 'H', 'C', 'D'. `n` is greater than 0, `x` and `y` are assigned values from the last input split.
#Overall this is what the function does:The function `func_1` reads an integer `n` within the range 0 to 52 and constructs a dictionary `d` with keys 'S', 'H', 'C', 'D' mapping to lists of 13 boolean values. It then iterates `n` times, taking input for card suit and rank, and marks the corresponding position in the dictionary as True. Afterward, it iterates through all suits and ranks, printing the ones not marked as True. The function operates based on the constraints specified for the input values.

