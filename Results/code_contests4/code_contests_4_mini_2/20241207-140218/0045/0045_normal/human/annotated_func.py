#State of the program right berfore the function call: n is a non-negative integer such that 0 <= n <= 52, and each of the following n lines contains a suit represented by 'S', 'H', 'C', or 'D' and a rank represented by an integer from 1 to 13.
def func_1():
    n = int(input())
    d = {'S': [None] * 13, 'H': [None] * 13, 'C': [None] * 13, 'D': [None] * 13}
    for i in range(n):
        x, y = raw_input().split()
        
        d[x][int(y) - 1] = True
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer such that 0 <= n <= 52; `d` is a dictionary with keys 'S', 'H', 'C', 'D' each holding a list of 13 values, with some of these values potentially set to True depending on the inputs received during the loop execution.
    for k in ['S', 'H', 'C', 'D']:
        for i in range(13):
            if d[k][i]:
                continue
            print('%s %d' % (k, i + 1))
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer such that 0 <= n <= 52, `k` is 'D', `i` is 12, and the printed output includes 'S', 'H', 'C', and 'D' followed by the numbers 1 to 13 corresponding to the indices where `d[k][i]` is false.
#Overall this is what the function does:The function accepts no parameters and reads a non-negative integer `n` (where 0 <= n <= 52) that represents the number of cards. It then records the suits ('S', 'H', 'C', 'D') and ranks (1 to 13) of the cards, marking them as present in a dictionary. After processing the input, the function prints out all the missing cards for each suit, indicating which ranks are not present among the input cards. If no cards are inputted (i.e., if n is 0), it will print all cards from each suit.

