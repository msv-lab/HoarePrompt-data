#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 52, and c is a list of n unique integers where each integer is in the range from 1 to n.
def func():
    n = int(input())
    i = 1
    sq = False
    while i <= n:
        if i == n:
            sq = True
        
        i = i * 3
        
    #State of the program after the loop has been executed: `i` is greater than `n`, `sq` is True if `n` is 3 or more, otherwise `sq` is False, `n` remains unchanged, `c` remains unchanged
    if sq :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`i` is greater than `n`, `n` and `c` remain unchanged. If `sq` is True (indicating `n` is 3 or more), 'YES' is printed. Otherwise, if `sq` is False, 'NO' is printed.
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 52) and checks if `n` is a power of 3. If `n` is equal to a power of 3, it prints 'YES'; otherwise, it prints 'NO'. The function does not utilize or validate the list `c` that is mentioned in the annotations.

