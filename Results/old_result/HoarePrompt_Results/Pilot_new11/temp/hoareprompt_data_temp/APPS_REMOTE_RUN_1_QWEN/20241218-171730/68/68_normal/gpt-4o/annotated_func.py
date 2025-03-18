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
        #State of the program after the if-else block has been executed: `min_upvotes` is `x`, `y` is a non-negative integer between 0 and 100, `max_upvotes` is `x + z`, `min_downvotes` is `y`, `max_downvotes` is `y + z`, and the maximum upvotes are not less than the minimum downvotes. If `max_downvotes` is less than `min_upvotes`, then a `+` is printed. Otherwise, no additional action is performed.
    #State of the program after the if-else block has been executed: *`min_upvotes` is `x`, `y` is a non-negative integer between 0 and 100, `max_upvotes` is `x + z`, `min_downvotes` is `y`, `max_downvotes` is `y + z`. If `max_upvotes` is less than `min_downvotes`, then the program prints a `+`. Otherwise, no additional action is performed.
#Overall this is what the function does:The function does not accept any parameters and returns a string ('+', '-', or '?') based on the comparison of maximum upvotes and minimum downvotes. It takes three non-negative integers \(x\), \(y\), and \(z\) as input, where \(0 \leq x, y, z \leq 100\). After processing, the function checks if the maximum possible upvotes (\(x + z\)) are greater than or equal to the minimum possible downvotes (\(y\)). If the maximum upvotes are less than the minimum downvotes, it prints a '-'. If the minimum downvotes are less than the maximum upvotes, it prints a '+'. If neither condition is met, it prints a '?'. The final state of the program after the function concludes is that the console will display one of these characters ('+', '-', '?').

