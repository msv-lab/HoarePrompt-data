#State of the program right berfore the function call: x, y, and z are non-negative integers such that 0 <= x, y, z <= 100.**
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
        #State of the program after the if-else block has been executed: *min_upvotes = x, max_upvotes = x + z, min_downvotes = y, max_downvotes = y + z. The condition (max_upvotes < min_downvotes) is false. The relationship (max_downvotes >= min_upvotes) holds true after the if-else block executes.
    #State of the program after the if-else block has been executed: *min_upvotes = x, max_upvotes = x + z, min_downvotes = y, max_downvotes = y + z. If max_upvotes is less than min_downvotes, then the program will retain the same state as the initial state. If max_upvotes is not less than min_downvotes, the relationship (max_downvotes >= min_upvotes) holds true after the if-else block executes.
#Overall this is what the function does:The function `func` reads three non-negative integers `x`, `y`, and `z` from input and calculates certain relationships between these integers. It then prints a specific symbol ('+', '-', or '?') based on the comparisons of `x`, `y`, and `z`. The program checks if `max_upvotes < min_downvotes` and prints '-' if true. It then checks if `max_downvotes < min_upvotes` and prints '+' if true. If both conditions are false, it prints '?'. The function does not explicitly return any value.

