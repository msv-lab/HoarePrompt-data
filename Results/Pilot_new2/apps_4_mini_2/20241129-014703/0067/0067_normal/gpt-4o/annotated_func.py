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
        #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that 0 <= `x` <= 100, 0 <= `y` <= 100, 0 <= `z` <= 100; `min_upvotes` is equal to `x`; `max_upvotes` is equal to `x + z`; `min_downvotes` is equal to `y`; `max_downvotes` is equal to `y + z`; `max_upvotes` is greater than or equal to `min_downvotes` (i.e., `x + z` >= `y`). If `max_downvotes` is less than `min_upvotes` (i.e., `y + z < x`), a '+' has been printed. Otherwise, if `max_downvotes` is greater than or equal to `min_upvotes` (i.e., `y + z >= x`), the code prints '?'.
    #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that 0 <= `x` <= 100, 0 <= `y` <= 100, 0 <= `z` <= 100. If `max_upvotes` (i.e., `x + z`) is less than `min_downvotes` (i.e., `y`), then `'-'` is printed. Otherwise, if `max_downvotes` (i.e., `y + z`) is less than `min_upvotes` (i.e., `x`), then `'+'` is printed. If `max_downvotes` is greater than or equal to `min_upvotes`, then '?' is printed.
#Overall this is what the function does:The function accepts three non-negative integers `x`, `y`, and `z` through user input, representing the number of upvotes, downvotes, and additional votes respectively. It calculates the minimum and maximum possible upvotes and downvotes based on these values. The function then prints a symbol based on the following conditions: if the maximum possible upvotes are less than the minimum downvotes, it prints '-', indicating that the upvotes cannot outnumber the downvotes. If the maximum downvotes are less than the minimum upvotes, it prints '+', implying a clear advantage in upvotes. If neither condition is met, it prints '?', suggesting uncertainty in the outcome. The function does not return any value.

