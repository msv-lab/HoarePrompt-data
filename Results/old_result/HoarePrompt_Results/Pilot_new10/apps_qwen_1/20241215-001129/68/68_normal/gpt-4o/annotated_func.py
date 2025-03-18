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
        #State of the program after the if-else block has been executed: *`x` is an integer between 0 and 100, `y` is an integer between 0 and 100, `z` is an integer between 0 and 100, `max_upvotes` is `x + z`, `min_downvotes` is `y`, `max_downvotes` is `y + z`, and `(max_upvotes >= min_downvotes)`. If `max_downvotes < min_upvotes`, then the condition remains unchanged. If `max_downvotes >= min_upvotes`, then the condition also remains unchanged.
    #State of the program after the if-else block has been executed: *`x` is an integer between 0 and 100, `y` is an integer between 0 and 100, `z` is an integer between 0 and 100, `max_upvotes` is `x + z`, `min_downvotes` is `y`, `max_downvotes` is `y + z`. The output contains `-` regardless of whether `max_upvotes < min_downvotes` or `max_upvotes >= min_downvotes`.
#Overall this is what the function does:The function reads three non-negative integers \( x \), \( y \), and \( z \) and prints `-` if the maximum possible upvotes are less than the minimum possible downvotes, `+` if the maximum possible downvotes are less than the minimum possible upvotes, and `?` otherwise.

