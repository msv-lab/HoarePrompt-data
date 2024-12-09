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
        #State of the program after the if-else block has been executed: *`x`, `y`, `z` are integers in the range 0 to 100. If `max_downvotes` is less than `min_upvotes`, the output is '+'. Otherwise, `max_downvotes` is greater than or equal to `min_upvotes`.
    #State of the program after the if-else block has been executed: *`x`, `y`, `z` are integers in the range 0 to 100. If `max_upvotes` is less than `min_downvotes`, then it is established that the current value of `max_upvotes` is less than the current value of `min_downvotes`. Otherwise, if `max_downvotes` is less than `min_upvotes`, the output is '+'; otherwise, `max_downvotes` is greater than or equal to `min_upvotes`.
#Overall this is what the function does:The function accepts three integers `x`, `y`, and `z` from user input, where each integer is within the range of 0 to 100. It then checks the relationships between calculated maximum and minimum upvotes and downvotes. If the maximum possible upvotes (`x + z`) is less than the minimum possible downvotes (`y`), it prints `'-'`. If the maximum possible downvotes (`y + z`) is less than the minimum possible upvotes (`x`), it prints `'+'`. If neither condition is met, it prints `'?'`. The function does not return any value.

