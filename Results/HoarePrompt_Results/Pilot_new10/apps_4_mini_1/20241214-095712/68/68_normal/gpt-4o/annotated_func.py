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
        #State of the program after the if-else block has been executed: *`x` is equal to `min_upvotes`, `y` is an integer from the range 0 to 100, `z` is an integer from the range 0 to 100, `max_upvotes` is equal to `min_upvotes + z`, `min_downvotes` is equal to `y`, and `max_downvotes` is equal to `y + z`. If `max_downvotes` is less than `min_upvotes`, then `max_downvotes` is less than `min_upvotes`, and '+' has been printed. Otherwise, `max_downvotes` is greater than or equal to `min_upvotes`.
    #State of the program after the if-else block has been executed: *`x` is equal to `min_upvotes`, `y` is an integer from the range 0 to 100, `z` is an integer from the range 0 to 100, if `max_upvotes` (which equals `min_upvotes + z`) is less than `min_downvotes` (which equals `y`), then '-' has been printed. Otherwise, `max_downvotes` (equal to `y + z`) is evaluated; if `max_downvotes` is less than `min_upvotes`, then '-' has been printed again, but if not, either '+' is printed or `max_downvotes` is greater than or equal to `min_upvotes`.
#Overall this is what the function does:The function accepts three integers x, y, and z (with values ranging from 0 to 100) as input arguments. It calculates the minimum and maximum possible upvotes and downvotes based on these values. It then evaluates these calculated values and prints '-' if the maximum possible upvotes are less than the minimum possible downvotes, '+' if the maximum possible downvotes are less than the minimum possible upvotes, or '?' if neither condition is met, indicating that overlaps exist between the possible upvotes and downvotes.

