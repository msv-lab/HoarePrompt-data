#State of the program right berfore the function call: **Precondition**: **n is an integer such that 1 ≤ n ≤ 52. c_1, c_2, ..., c_n are integers representing the cards in the deck and each integer from 1 to n appears exactly once in the deck.**
def func():
    n = int(input())
    i = 1
    sq = False
    while i <= n:
        if i == n:
            sq = True
        
        i = i * 3
        
    #State of the program after the loop has been executed: `i` is greater than `n`, `sq` is True, `n` is greater than or equal to 1. If `i` is equal to `n`, `sq` is True. Otherwise, `i` is greater than `n`
    if sq :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`i` is greater than `n`, `sq` is True, `n` is greater than or equal to 1. If `i` is equal to `n`, `sq` is True. Otherwise, `i` is greater than `n`, `sq` is True. If the condition is true, 'YES' is printed. If the condition is false, 'NO' is printed and the initial state of the variables remains unchanged.
#Overall this is what the function does:The function reads an integer n from the user, then iterates through a while loop where i is multiplied by 3 until i is greater than n. If i equals n at any point, the variable sq is set to True. After the loop, if sq is True, it prints 'YES', otherwise it prints 'NO'. The function essentially checks if n is a power of 3 and outputs 'YES' if it is, 'NO' otherwise. The annotations mention generating and shuffling a deck of cards, which is not reflected in the code.

