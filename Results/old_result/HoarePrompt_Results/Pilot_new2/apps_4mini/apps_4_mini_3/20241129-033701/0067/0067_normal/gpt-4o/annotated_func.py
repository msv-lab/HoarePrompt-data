#State of the program right berfore the function call: x, y, and z are integers such that 0 <= x, y, z <= 100.
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
        #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers. If `max_downvotes` is less than `min_upvotes`, then `max_downvotes` is less than `x`. Otherwise, `max_downvotes` is greater than or equal to `min_upvotes`, and the output is '?'.
    #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers. If `max_upvotes` is less than `min_downvotes`, then `max_upvotes` is less than `min_downvotes`, which means `max_upvotes` is less than `y + z`. If `max_downvotes` is less than `min_upvotes`, then `max_downvotes` is less than `x`. Otherwise, `max_downvotes` is greater than or equal to `min_upvotes`, and the output is '?'.
#Overall this is what the function does:The function reads three integers `x`, `y`, and `z` from user input (where each integer is between 0 and 100 inclusive) and evaluates them to determine the relationship between maximum upvotes and downvotes. It outputs '-' if the maximum upvotes are less than the minimum downvotes, '+' if the maximum downvotes are less than the minimum upvotes, or '?' if neither condition is met. The function does not return any value, it only prints the results.

