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
        #State of the program after the if-else block has been executed: `x` is an integer (0 <= x <= 100), `y` is an integer (0 <= y <= 100), `z` is an integer (0 <= z <= 100), `min_upvotes` is equal to `x`, `max_upvotes` is equal to `x + z`, `min_downvotes` is `y`, `max_downvotes` is `y + z`, and the condition `max_upvotes >= min_downvotes` holds true. If `max_downvotes` is lower than `min_upvotes`, a plus sign is printed to the console. Otherwise, nothing specific changes regarding the values of the variables.
    #State of the program after the if-else block has been executed: *`x` is an integer (0 <= x <= 100), `y` is an integer (0 <= y <= 100), `z` is an integer (0 <= z <= 100), `min_upvotes` is equal to `x`, `max_upvotes` is equal to `x + z`, `min_downvotes` is `y`, `max_downvotes` is `y + z`. If `max_upvotes` is less than `min_downvotes`, the function prints a plus sign to the console. Otherwise, the function does not change the values of the variables.
#Overall this is what the function does:The function takes no parameters and reads three non-negative integers \(x\), \(y\), and \(z\) from standard input, where \(0 \leq x, y, z \leq 100\). It then calculates the minimum and maximum possible upvotes and downvotes based on these values. Specifically, `min_upvotes` is set to \(x\), `max_upvotes` is set to \(x + z\), `min_downvotes` is set to \(y\), and `max_downvotes` is set to \(y + z\).

The function checks if the maximum possible upvotes are less than the minimum possible downvotes. If this condition is true, it prints `-`. Otherwise, it further checks if the maximum possible downvotes are less than the minimum possible upvotes. If this second condition is true, it prints `+`. If neither condition is met, it prints `?`.

After the function executes, the values of `x`, `y`, and `z` remain unchanged, while `min_upvotes`, `max_upvotes`, `min_downvotes`, and `max_downvotes` are updated to reflect the calculations described above. The function prints either `-`, `+`, or `?` to the console based on the conditions evaluated.

