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
        #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers within the range of 0 to 100. If `max_downvotes` is less than `min_upvotes`, then '+' has been printed. Otherwise, `max_downvotes` is greater than or equal to `min_upvotes`, and '?' has been printed. Additionally, `min_upvotes` is equal to `x`, `max_upvotes` is equal to `x + z`, `min_downvotes` is equal to `y`, and `max_downvotes` is equal to `y + z`, while also satisfying that `max_upvotes` is greater than or equal to `min_downvotes`.
    #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers based on input values within the range of 0 to 100. If `max_upvotes` is less than `min_downvotes`, then the state remains as `min_upvotes` is equal to `x`, `max_upvotes` is equal to `x + z`, `min_downvotes` is equal to `y`, and `max_downvotes` is equal to `y + z`. Otherwise, if `max_downvotes` is less than `min_upvotes`, then '+' has been printed, and the conditions remain the same. If `max_downvotes` is greater than or equal to `min_upvotes`, then '?' has been printed, while the relationships between `min_upvotes`, `max_upvotes`, `min_downvotes`, and `max_downvotes` still hold true.
#Overall this is what the function does:The function accepts three integers x, y, and z (0 <= x, y, z <= 100) via user input. It calculates minimum and maximum values for upvotes and downvotes based on these inputs. The function prints '-' if the maximum upvotes are less than the minimum downvotes, '+' if the maximum downvotes are less than the minimum upvotes, and '?' if neither condition is met. The function does not return any value.

