#State of the program right berfore the function call: x, y, and z are non-negative integers such that 0 <= x, y, z <= 100.
def func():
    x, y, z = map(int, input().split())
    min_upvotes = x
    max_upvotes = x + z
    min_downvotes = y
    max_downvotes = y + z
    if (max_upvotes < min_downvotes) :
        print('-')
    else :
        if (max_downvotes < min_upvotes) :
            print('+')
        else :
            print('?')
        #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that 0 <= `x`, `y`, `z` <= 100; `min_upvotes` is equal to `x`; `max_upvotes` is equal to `x + z`; `min_downvotes` is equal to `y`; `max_downvotes` is equal to `y + z`; `max_upvotes` is greater than or equal to `min_downvotes`; if `max_downvotes` is less than `min_upvotes`, then '+' has been printed. Otherwise, `max_downvotes` is greater than or equal to `min_upvotes`.
    #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that 0 <= `x`, `y`, `z` <= 100. If `max_upvotes` is less than `min_downvotes`, then a string `'-'` has been printed. Otherwise, if `max_upvotes` is greater than or equal to `min_downvotes`, it is checked if `max_downvotes` is less than `min_upvotes`; if so, a string `'+'` has been printed, otherwise, `max_downvotes` is greater than or equal to `min_upvotes`.
#Overall this is what the function does:The function accepts three non-negative integers `x`, `y`, and `z` as input. It calculates the minimum and maximum possible counts of upvotes and downvotes based on these values. It then prints one of three outcomes: '-' if the maximum possible upvotes are less than the minimum downvotes, '+' if the maximum possible downvotes are less than the minimum upvotes, or '?' if neither condition is met. There is no explicit return value from the function.

