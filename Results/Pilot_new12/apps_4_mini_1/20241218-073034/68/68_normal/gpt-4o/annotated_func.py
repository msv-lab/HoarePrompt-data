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
        #State of the program after the if-else block has been executed: *`x`, `y`, `z` are integers such that 0 <= `x` <= 100, 0 <= `y` <= 100, and 0 <= `z` <= 100. If the current value of `max_downvotes` (i.e., `y + z`) is less than `min_upvotes` (i.e., `x`), then a '+' character is printed. Otherwise, if `max_downvotes` is greater than or equal to `min_upvotes`, a '?' character is printed.
    #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers such that 0 <= `x` <= 100, 0 <= `y` <= 100, and 0 <= `z` <= 100. If `max_upvotes` (i.e., `x + z`) is less than `min_downvotes` (i.e., `y`), a hyphen ('-') is printed. Otherwise, if `max_downvotes` (i.e., `y + z`) is less than `min_upvotes` (i.e., `x`), then a '+' character is printed. If `max_downvotes` is greater than or equal to `min_upvotes`, a '?' character is printed.
#Overall this is what the function does:The function reads three integers x, y, and z from input, which represent upvotes, downvotes, and a margin, respectively, constrained between 0 and 100. It calculates the minimum and maximum possible values for upvotes and downvotes: min_upvotes is x, max_upvotes is x + z, min_downvotes is y, and max_downvotes is y + z. Based on these values, it determines the relationship between upvotes and downvotes. If the maximum possible upvotes is less than the minimum possible downvotes, it prints a hyphen ('-'), indicating that downvotes exceed the highest possible upvotes. If the maximum possible downvotes is less than the minimum possible upvotes, it prints a plus sign ('+'), indicating that upvotes exceed the highest possible downvotes. If neither of these conditions is met, it prints a question mark ('?'), indicating an overlap where the upvotes and downvotes cannot be conclusively compared. The function does not return anything, and after its execution, the integers x, y, and z remain within the range of 0 to 100. The function handles edge cases where x, y, or z are at their minimum or maximum values.

