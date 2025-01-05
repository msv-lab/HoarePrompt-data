#State of the program right berfore the function call: n is a non-negative integer such that 0 <= n <= 52, and for each of the n cards, a suit represented by 'S', 'H', 'C', or 'D' and a rank represented by an integer from 1 to 13 are provided.
def func_1():
    n = int(input())
    d = {'S': [None] * 13, 'H': [None] * 13, 'C': [None] * 13, 'D': [None] * 13}
    for i in range(n):
        x, y = raw_input().split()
        
        d[x][int(y) - 1] = True
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer such that 0 <= n <= 52; `d` contains some keys with values set to True based on user input during the loop execution, while others remain as None; `i` is equal to `n` after the loop execution.
    for k in ['S', 'H', 'C', 'D']:
        for i in range(13):
            if d[k][i]:
                continue
            print('%s %d' % (k, i + 1))
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer such that 0 <= `n` <= 52; `d` contains keys with values set to True or None; `i` is 13; the printed output reflects all combinations of keys `k` and their corresponding indices from 1 to 13 for which the values were None in `d`.
#Overall this is what the function does:The function accepts a non-negative integer `n` (where 0 <= n <= 52) and reads `n` cards from user input, where each card consists of a suit ('S', 'H', 'C', or 'D') and a rank (1 to 13). It then prints all combinations of suits and ranks that were not provided in the input, indicating which cards are missing. If no cards are provided (`n` is 0), it will print all 52 possible cards.

