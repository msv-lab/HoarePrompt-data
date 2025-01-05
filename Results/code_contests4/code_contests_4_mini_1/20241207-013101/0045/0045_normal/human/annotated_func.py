#State of the program right berfore the function call: n is a non-negative integer such that 0 <= n <= 52, and the following n lines contain pairs of a character ('S', 'H', 'C', 'D') representing suits and integers (1 to 13) representing ranks, with no duplicate cards.
def func_1():
    n = int(input())
    d = {'S': [None] * 13, 'H': [None] * 13, 'C': [None] * 13, 'D': [None] * 13}
    for i in range(n):
        x, y = raw_input().split()
        
        d[x][int(y) - 1] = True
        
    #State of the program after the  for loop has been executed: `d` contains lists for each key ('S', 'H', 'C', 'D') with some indices set to True based on the input values; `n` is a non-negative integer indicating the number of iterations executed. If `n` is 0, then `d` remains unchanged with all values still set to None.
    for k in ['S', 'H', 'C', 'D']:
        for i in range(13):
            if d[k][i]:
                continue
            print('%s %d' % (k, i + 1))
        
    #State of the program after the  for loop has been executed: `d` contains lists for each key ('S', 'H', 'C', 'D'); `n` is at least 0; `k` has taken values 'S', 'H', 'C', 'D'; `i` has reached 13; printed output includes lines for each falsy value found in all lists across the keys.
#Overall this is what the function does:The function accepts a non-negative integer `n` (0 <= n <= 52) and reads `n` pairs of suits ('S', 'H', 'C', 'D') and ranks (1 to 13) from input, marking the corresponding indices in a dictionary as `True` for the suits. After processing the input, it prints out all the missing cards for each suit, indicating which ranks (1 to 13) are not marked as present based on the input. If `n` is 0, it simply outputs all ranks for all suits since no cards are read.

