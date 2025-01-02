#State of the program right berfore the function call: The input consists of two lines. The first line is an integer n (1 ≤ n ≤ 100 000) representing the number of cockroaches, and the second line is a string of length n, consisting of characters 'b' and 'r' that denote black cockroaches and red cockroaches, respectively.
def func():
    n = int(raw_input())
    line = raw_input()
    change_red = 0
    change_black = 0
    for (idx, val) in enumerate(line):
        if idx % 2 == 0 and val == 'b':
            change_black += 1
        
        if idx % 2 == 1 and val == 'r':
            change_red += 1
        
    #State of the program after the  for loop has been executed: Output State:
    swaps = min(change_red, change_black)
    color = max(change_red, change_black) - swaps
    total = swaps + color
    change_red2 = 0
    change_black2 = 0
    for (idx, val) in enumerate(line):
        if idx % 2 == 1 and val == 'b':
            change_black2 += 1
        
        if idx % 2 == 0 and val == 'r':
            change_red2 += 1
        
    #State of the program after the  for loop has been executed: 
    swaps2 = min(change_red2, change_black2)
    color2 = max(change_red2, change_black2) - swaps2
    total2 = swaps2 + color2
    print(min(total, total2))
#Overall this is what the function does:Functionality: The function reads an integer `n` and a string of length `n` consisting of 'b' and 'r', where 'b' denotes black cockroaches and 'r' denotes red cockroaches. It then counts the number of black and red cockroaches in positions that should ideally be the opposite color based on their index (even-indexed positions should be 'b' and odd-indexed positions should be 'r'). The function calculates the minimum number of swaps required to have as many cockroaches in their correctly positioned color as possible. Specifically, it performs two passes over the string to count mismatches in even and odd indexed positions, calculates the number of swaps needed for each pass, and prints the minimum of these two values. This ensures that the function provides the optimal solution for the given input, considering all edge cases such as strings composed entirely of one color, alternating colors, or mixed distributions.

