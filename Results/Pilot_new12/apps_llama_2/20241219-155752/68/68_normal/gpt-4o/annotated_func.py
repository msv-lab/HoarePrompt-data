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
        #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are input integers such that 0 <= x, y, z; `min_upvotes` equals `x`; `max_upvotes` equals `x + z`; `min_downvotes` equals `y`; `max_downvotes` equals `y + z`; and `max_upvotes` is greater than or equal to `min_downvotes`. If `max_downvotes` is less than `min_upvotes`, then '+' has been printed. Otherwise, if `max_downvotes` is greater than or equal to `min_upvotes`, then '?' has been printed.
    #State of the program after the if-else block has been executed: `x`, `y`, and `z` are input integers such that 0 <= x, y, z; `min_upvotes` equals `x`; `max_upvotes` equals `x + z`; `min_downvotes` equals `y`; `max_downvotes` equals `y + z`. If `x + z < y`, then no action has been taken. Otherwise, if `x + z` is greater than or equal to `y`, then either '+' has been printed if `y + z < x`, or '?' has been printed if `y + z` is greater than or equal to `x`.
#Overall this is what the function does:The function accepts three non-negative integers `x`, `y`, and `z` as input, where `0 <= x, y, z <= 100`. After execution, the function will have printed one of three possible characters to the console: `-` if the maximum possible upvotes (`x + z`) are less than the minimum possible downvotes (`y`), `+` if the maximum possible downvotes (`y + z`) are less than the minimum possible upvotes (`x`), or `?` if neither of the above conditions are met. The function does not modify the input values or return any value, and its purpose is to provide a simple classification based on the input integers.

