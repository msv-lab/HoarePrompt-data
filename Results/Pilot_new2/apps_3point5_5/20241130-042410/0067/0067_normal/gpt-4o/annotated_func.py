#State of the program right berfore the function call: x, y, and z are non-negative integers such that 0 <= x,y,z <= 100.**
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
        #State of the program after the if-else block has been executed: *`x`, `y`, `z` are non-negative integers such that 0 <= `x`, `y`, `z` <= 100. `min_upvotes` is assigned the value of `x`, `max_upvotes` is equal to `x + z`, `min_downvotes` is assigned the value of `y`, `max_downvotes` is equal to `y + z`. The condition (max_upvotes < min_downvotes) is false. Regardless of entering the if or else part, the state of the variables remains the same - `max_downvotes` is not less than `min_upvotes`.
    #State of the program after the if-else block has been executed: *`x`, `y`, `z` are non-negative integers such that 0 <= `x`, `y`, `z` <= 100. `min_upvotes` is assigned the value of `x`, `max_upvotes` is equal to `x + z`, `min_downvotes` is assigned the value of `y`, `max_downvotes` is equal to `y + z`. The condition (max_upvotes < min_downvotes) is false. Regardless of entering the if or else part, the state of the variables remains the same - `max_downvotes` is not less than `min_upvotes`.
#Overall this is what the function does:The function `func` reads three non-negative integers x, y, and z as input. It then computes the minimum and maximum values for upvotes and downvotes based on these inputs. If the maximum upvotes are less than the minimum downvotes, it prints '-', if the maximum downvotes are less than the minimum upvotes, it prints '+', otherwise it prints '?'. The function does not have a return value.

