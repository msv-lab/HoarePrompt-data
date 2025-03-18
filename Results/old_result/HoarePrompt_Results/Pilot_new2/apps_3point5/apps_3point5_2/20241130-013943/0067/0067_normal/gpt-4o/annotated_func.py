#State of the program right berfore the function call: x, y, and z are non-negative integers such that 0 <= x, y, z <= 100.**
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
        #State of the program after the if-else block has been executed: *min_upvotes is equal to x. max_upvotes is equal to x + z. min_downvotes is equal to y. max_downvotes is equal to y + z. The condition (max_upvotes < min_downvotes) is false, meaning max_upvotes is greater than or equal to min_downvotes. No changes occur in the state of the program variables after the execution of the if else block.
    #State of the program after the if-else block has been executed: *min_upvotes is equal to x. max_upvotes is equal to x + z. min_downvotes is equal to y. max_downvotes is equal to y + z. If max_upvotes is less than min_downvotes, no changes occur in the state of the program variables after the execution of the if else block. If max_upvotes is greater than or equal to min_downvotes, no changes occur in the state of the program variables after the execution of the if else block.
#Overall this is what the function does:The function `func` reads three non-negative integers x, y, and z from input and compares them based on specific conditions. If max_upvotes is less than min_downvotes, it prints '-', if max_downvotes is less than min_upvotes, it prints '+', otherwise it prints '?'. The function does not accept any parameters and always operates on the input integers x, y, and z.

