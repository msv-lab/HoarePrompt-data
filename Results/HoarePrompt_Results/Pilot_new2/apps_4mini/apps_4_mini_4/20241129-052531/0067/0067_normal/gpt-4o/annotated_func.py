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
        #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers in the range 0 to 100. If `max_downvotes` is less than `min_upvotes`, then the output is '+'. Otherwise, `max_downvotes` is greater than or equal to `min_upvotes`.
    #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers in the range 0 to 100. If `max_upvotes` is less than `min_downvotes`, the output is '-'. If `max_downvotes` is less than `min_upvotes`, the output is '+'. Otherwise, `max_downvotes` is greater than or equal to `min_upvotes`.
#Overall this is what the function does:The function accepts three integers as input (x, y, and z) which represent upvotes and downvotes, and it outputs a character based on the relative values of the calculated maximum and minimum upvotes and downvotes. It prints '-' if the maximum upvotes are less than the minimum downvotes, '+' if the maximum downvotes are less than the minimum upvotes, and '?' if neither condition is met. The function does not return any value.

