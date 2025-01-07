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
        #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers equal to the three input values (0 <= `x`, `y`, `z` <= 100); `min_upvotes` is equal to `x`; `max_upvotes` is equal to `x + z`; `min_downvotes` is equal to `y`; `max_downvotes` is equal to `y + z`; `max_upvotes` is greater than or equal to `min_downvotes` (i.e., `x + z >= y`); if `max_downvotes` is less than `min_upvotes` (i.e., `y + z < x`), then '+' has been printed. Otherwise, the output is '?' with no change to the variable values.
    #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers with values between 0 and 100. If `max_upvotes` (which equals `x + z`) is less than `min_downvotes` (which equals `y`), the output is '-'. Otherwise, if `max_upvotes` is greater than or equal to `min_downvotes`, and if `max_downvotes` (which equals `y + z`) is less than `min_upvotes` (which equals `x`), then the output is '+'. If neither of these conditions is met, the output is '?' with no change to the variable values.
#Overall this is what the function does:The function accepts three integers `x`, `y`, and `z` through standard input, where 0 <= x, y, z <= 100. It calculates the minimum and maximum number of upvotes and downvotes based on these inputs. The function prints '-' if the maximum upvotes (`x + z`) are less than the minimum downvotes (`y`). If the maximum downvotes (`y + z`) are less than the minimum upvotes (`x`), it prints '+'. If neither condition is met, it prints '?'. The function does not return any values but outputs a single character based on the conditions stated.

