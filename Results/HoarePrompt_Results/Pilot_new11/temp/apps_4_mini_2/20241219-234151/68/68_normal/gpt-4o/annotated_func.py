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
        #State of the program after the if-else block has been executed: *`x`, `y`, `z` are integers within the range 0 to 100. If `max_downvotes` is less than `min_upvotes`, the output is '+'. Otherwise, a question mark has been printed.
    #State of the program after the if-else block has been executed: *`x`, `y`, `z` are integers within the range 0 to 100. If `max_upvotes` is less than `min_downvotes`, it implies that `x + z < y`, maintaining the ranges initially defined. Otherwise, if `max_downvotes` is less than `min_upvotes`, it indicates that `y + z < x`, resulting in the output being '+'. If neither condition is satisfied, a question mark is printed.
#Overall this is what the function does:The function accepts three non-negative integer inputs: `x`, `y`, and `z`, which should lie within the range of 0 to 100. It calculates the minimum and maximum possible upvotes and downvotes based on these inputs. The function then evaluates and prints the result based on certain conditions: if the maximum possible upvotes are less than the minimum downvotes, it outputs a negative sign ('-'); if the maximum possible downvotes are less than the minimum upvotes, it outputs a positive sign ('+'); if neither of these conditions hold, it outputs a question mark ('?'). The output thus indicates the relationship between possible upvote and downvote counts considering the influence of `z`, but it does not return any value or modify the input parameters. No edge cases for invalid input handling are present, and the function lacks the ability to handle inputs or output results beyond printing to the console.

