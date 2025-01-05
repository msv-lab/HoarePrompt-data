#State of the program right berfore the function call: **Precondition**: **n is an integer such that 1 ≤ n ≤ 52. c_1, c_2, ..., c_n are integers representing the cards in the deck, and for all i=1,...,n there is exactly one j∈{1,...,n} such that c_j = i.**
def func():
    n = int(input())
    i = 1
    sq = False
    while i <= n:
        if i == n:
            sq = True
        
        i = i * 3
        
    #State of the program after the loop has been executed: `i` is 108, `sq` is True, `n` is greater than or equal to 1, loop control variable `i` is not equal to `n`
    if sq :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`i` is 108, `sq` is True, `n` is greater than or equal to 1, loop control variable `i` is not equal to `n`. If `sq` is True, the program prints 'YES'. If `sq` is False, the program prints 'NO'.
#Overall this is what the function does:The function reads an integer n from the user, initializes a loop control variable i to 1, and iterates through the loop until i is greater than n. Within the loop, i is multiplied by 3 at each iteration. After the loop, if i equals n, the variable sq is set to True. Then, if sq is True, the function prints 'YES'; otherwise, it prints 'NO'. The function does not accept any parameters and operates based on the described constraints. It verifies if a specific property related to a deck of cards holds true.

