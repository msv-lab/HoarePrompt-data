#State of the program right berfore the function call: The function takes no arguments, but it is implied that there are three non-negative integers x, y, z where 0 <= x, y, z <= 100, corresponding to the number of persons who would upvote, downvote or unknown.
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
        #State of the program after the if-else block has been executed: `x` is the number of upvotes, `y` is the number of downvotes, `z` is the number of unknown votes, `min_upvotes` equals `x`, `max_upvotes` equals `x + z`, `min_downvotes` equals `y`, `max_downvotes` equals `y + z`, 0 <= `x`, `y`, `z` <= 100, `x + z` is greater than or equal to `y`. If `y + z` is less than `x`, then the state remains unchanged. Otherwise, a '?' has been printed and `y + z` is greater than or equal to `x`.
    #State of the program after the if-else block has been executed: *`x` is the number of upvotes, `y` is the number of downvotes, `z` is the number of unknown votes, `min_upvotes` equals `x`, `max_upvotes` equals `x + z`, `min_downvotes` equals `y`, `max_downvotes` equals `y + z`, 0 <= `x`, `y`, `z` <= 100. If `x + z` is less than `y`, a string '-' has been returned. Otherwise, if `y + z` is less than `x`, the state remains unchanged; otherwise, a '?' has been printed and `y + z` is greater than or equal to `x`.
#Overall this is what the function does:The function takes three non-negative integers x, y, z as input from the user, representing upvotes, downvotes, and unknown votes respectively, calculates the minimum and maximum possible upvotes and downvotes, and prints '+' if upvotes will definitely win, '-' if downvotes will definitely win, and '?' if the outcome is uncertain, without validating the input range or type.

