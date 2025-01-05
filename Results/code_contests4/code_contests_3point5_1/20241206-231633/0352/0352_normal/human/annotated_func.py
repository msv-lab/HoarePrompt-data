#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 52, and c_i is an integer representing the card number in the deck.**
def func():
    n = int(input())
    i = 1
    sq = False
    while i <= n:
        if i == n:
            sq = True
        
        i = i * 3
        
    #State of the program after the loop has been executed: `n` is an integer such that 1 ≤ n ≤ 52, `i` is the smallest power of 3 greater than `n`, `sq` is True if `i` is equal to `n`, otherwise `sq` is False
    if sq :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an integer such that 1 ≤ n ≤ 52, `i` is the smallest power of 3 greater than `n`, `sq` is True if `i` is equal to `n`, otherwise `sq` is False. If `sq` is True, 'YES' is printed. If `sq` is False, 'NO' is printed.
#Overall this is what the function does:The function takes an integer input n (1 ≤ n ≤ 52) and generates a deck of playing cards. Each card is represented by a unique integer between 1 and 52. The function then checks if the smallest power of 3 greater than n is equal to n, and prints 'YES' if true, 'NO' otherwise.

