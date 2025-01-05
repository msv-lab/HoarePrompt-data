#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 52, and the deck consists of n integers c_1, c_2, ..., c_n where each integer is unique and lies within the range from 1 to n.
def func():
    n = int(input())
    i = 1
    sq = False
    while i <= n:
        if i == n:
            sq = True
        
        i = i * 3
        
    #State of the program after the loop has been executed: `i` is 81, `sq` is True if `n` is 9 or 27 or more; otherwise, `sq` is False.
    if sq :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`i` is 81. If `sq` is True, indicating that `n` is either 9 or 27 or more, 'YES' is printed. Otherwise, if `sq` is False, 'NO' is printed.
#Overall this is what the function does:The function reads an integer `n` (1 ≤ n ≤ 52) from input and checks if `n` is equal to 9 or 27 or a power of 3 that is less than or equal to `n`. If so, it prints 'YES'; otherwise, it prints 'NO'. The logic for determining if `n` is a power of 3 is achieved by repeatedly multiplying `i` by 3 until `i` exceeds `n`. If `n` is a number that is not equal to 9, 27, or a power of 3, the function will print 'NO'.

