#State of the program right berfore the function call: The input consists of two lines. The first line contains a single integer n (1 ≤ n ≤ 100 000) representing the number of cockroaches. The second line contains a string of length n, consisting of characters 'b' and 'r', where 'b' denotes a black cockroach and 'r' denotes a red cockroach.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100,000, `line` is a non-empty string, `change_black` is the number of 'b' characters at even indices, and `change_red` is the number of 'r' characters at odd indices.
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
        
    #State of the program after the  for loop has been executed: Output State:
    swaps2 = min(change_red2, change_black2)
    color2 = max(change_red2, change_black2) - swaps2
    total2 = swaps2 + color2
    print(min(total, total2))
#Overall this is what the function does:The function processes an input consisting of two lines: the first line is an integer `n` (1 ≤ n ≤ 100,000) representing the number of cockroaches, and the second line is a string of length `n` containing characters 'b' and 'r'. It calculates the minimum number of swaps required to ensure that all black cockroaches ('b') are at even indices and all red cockroaches ('r') are at odd indices. The function then prints this minimum number of swaps.

