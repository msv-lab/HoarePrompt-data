#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 52, and the second input line contains n integers representing the cards in the deck, where each integer is unique and in the range from 1 to n.
def func():
    n = int(input())
    i = 1
    sq = False
    while i <= n:
        if i == n:
            sq = True
        
        i = i * 3
        
    #State of the program after the loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 52; `i` is 81, `sq` is True if `n` was a power of 3 encountered (1, 3, 9, or 27), otherwise `sq` is False.
    if sq :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 52; `i` is 81. If `sq` is True, indicating that `n` is a power of 3 (1, 3, 9, or 27), 'YES' is printed. Otherwise, if `sq` is False, 'NO' is printed.
#Overall this is what the function does:The function accepts an integer `n` within the range of 1 to 52 and determines if `n` is a power of 3 (specifically 1, 3, 9, or 27). It prints 'YES' if `n` is a power of 3 and 'NO' otherwise. The function does not utilize the second input line containing unique integers representing cards, which is not processed or needed for the output.

