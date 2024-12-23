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
        #State of the program after the if-else block has been executed: *`x` is an input integer, `y` is an input integer, `z` is an input integer, `min_upvotes` is equal to `x`, `max_upvotes` is equal to `x + z`, `min_downvotes` is equal to `y`, `max_downvotes` is equal to `y + z`, and `max_upvotes` is greater than or equal to `min_downvotes`. If `max_downvotes` is less than `min_upvotes`, then '+' has been printed. If `max_downvotes` is greater than or equal to `min_upvotes`, then '?' has been printed.
    #State of the program after the if-else block has been executed: *`x` is an input integer, `y` is an input integer, `z` is an input integer, `min_upvotes` is equal to `x`, `max_upvotes` is equal to `x + z`, `min_downvotes` is equal to `y`, `max_downvotes` is equal to `y + z`. If `x + z` is less than `y`, then the state remains as is. If `x + z` is greater than or equal to `y`, then if `y + z` is less than `x`, '+' has been printed; otherwise, if `y + z` is greater than or equal to `x`, '?' has been printed.
#Overall this is what the function does:The function accepts three non-negative integers `x`, `y`, and `z` between 0 and 100 as input, calculates the minimum and maximum possible upvotes and downvotes based on these inputs, and then prints one of three possible characters: '-', '+' or '?'. The character '-' is printed if the maximum possible upvotes are less than the minimum possible downvotes. The character '+' is printed if the minimum possible upvotes are greater than the maximum possible downvotes. Otherwise, the character '?' is printed. After the function concludes, the state of the program reflects the printed character based on the comparison of the calculated upvotes and downvotes ranges, but it does not modify the input values `x`, `y`, or `z`. The final state is determined by the comparisons made within the function, considering all potential edge cases where the input integers may be at their minimum or maximum values within the specified range.

