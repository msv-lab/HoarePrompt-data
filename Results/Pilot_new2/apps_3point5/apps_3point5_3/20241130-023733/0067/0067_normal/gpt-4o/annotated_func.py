#State of the program right berfore the function call: **Precondition**: **x, y, and z are non-negative integers such that 0 <= x, y, z <= 100.**
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
        #State of the program after the if-else block has been executed: `x`, `y`, and `z` are non-negative integers such that 0 <= x, y, z <= 100. `x`, `y`, and `z` are assigned the integers obtained from the input split. `min_upvotes` is equal to the value of `x`, `max_upvotes` is equal to `x + z`, `min_downvotes` is equal to `y`, `max_downvotes` is equal to `y + z`. Additionally, `max_upvotes` is not less than `min_downvotes`. If max_downvotes < min_upvotes, then the program does nothing and the state of the variables remains the same. If max_downvotes is not less than min_upvotes, the program also does nothing, and the state of the variables remains the same. Therefore, the values of `x`, `y`, `z`, `min_upvotes`, `max_upvotes`, `min_downvotes`, and `max_downvotes` remain unchanged after the execution of the if else block.
    #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that 0 <= x, y, z <= 100. `x`, `y`, and `z` are assigned the integers obtained from the input split. `min_upvotes` is equal to the value of `x`, `max_upvotes` is equal to `x + z`, `min_downvotes` is equal to `y`, `max_downvotes` is equal to `y + z`. If max_upvotes < min_downvotes, the program prints '-'. Otherwise, the values of `x`, `y`, `z`, `min_upvotes`, `max_upvotes`, `min_downvotes`, and `max_downvotes` remain unchanged after the execution of the if else block.
#Overall this is what the function does:The function `func` takes no parameters. It reads three non-negative integers x, y, and z from input, calculates `min_upvotes`, `max_upvotes`, `min_downvotes`, and `max_downvotes` based on these values, and then determines whether to print '-', '+', or '?' based on certain conditions. If `max_upvotes` is less than `min_downvotes`, it prints '-'. If `max_downvotes` is less than `min_upvotes`, it prints '+'. Otherwise, it prints '?'. The function does not return any value and only prints the result.

