#State of the program right berfore the function call: x, y, and z are integers in the range [0, 100], where x is the number of persons who would upvote, y is the number of persons who would downvote, and z is the number of persons whose voting intentions are unknown.
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
        #State of the program after the if-else block has been executed: *`x`, `y`, `z` are integers in the range [0, 100]. If `max_downvotes` is less than `min_upvotes`, then '+' is printed. Otherwise, `max_downvotes` is greater than or equal to `min_upvotes` and both `min_upvotes` and `max_upvotes` remain unchanged from their initial values.
    #State of the program after the if-else block has been executed: *`x`, `y`, `z` are integers in the range [0, 100]. If `max_upvotes` is less than `min_downvotes`, then the condition is satisfied. If `max_downvotes` is less than `min_upvotes`, then '+' is printed. Otherwise, `max_downvotes` is greater than or equal to `min_upvotes` and both `min_upvotes` and `max_upvotes` remain unchanged from their initial values.
#Overall this is what the function does:The function accepts three integers `x`, `y`, and `z`, which represent the number of upvotes, downvotes, and unknown voting intentions, respectively. It checks if the maximum possible upvotes (x + z) is less than the minimum downvotes (y), in which case it prints '-' indicating a clear loss. If the maximum possible downvotes (y + z) is less than the minimum upvotes (x), it prints '+' indicating a clear win. If neither condition is met, it prints '?' indicating uncertainty. The function does not return any value; it only prints the results based on the comparisons.

