#State of the program right berfore the function call: The input consists of three non-negative integers x, y, z, each less than or equal to 100, representing the number of people who would upvote, downvote, and vote with unknown outcome, respectively.
def func():
    x, y, z = map(int, input().split())
    if (x > y + z) :
        print('+')
    else :
        if (x < y) :
            print('-')
        else :
            if (x == y) :
                if (z == 0) :
                    print('0')
                else :
                    print('?')
                #State of the program after the if-else block has been executed: `x`, `y`, `z` are non-negative integers, each less than or equal to 100, `x` equals `y`, and `x` is less than or equal to `y + z`. If `z` is 0, a value `0` has been printed. If `z` is greater than 0, a '?' has been printed to the console.
            else :
                print('?')
            #State of the program after the if-else block has been executed: *`x`, `y`, `z` are non-negative integers, each less than or equal to 100, `x` is less than or equal to `y + z`, and `x` is greater than or equal to `y`. If `x` equals `y`, then if `z` is 0, a value `0` has been printed, otherwise a '?' has been printed. If `x` does not equal `y`, then a '?' has been printed.
        #State of the program after the if-else block has been executed: `x`, `y`, `z` are non-negative integers, each less than or equal to 100, `x` is less than or equal to `y + z`. If `x` is less than `y`, a hyphen has been printed to the console. If `x` is greater than or equal to `y`, then if `x` equals `y` and `z` is 0, a value `0` has been printed; otherwise, a '?' has been printed.
    #State of the program after the if-else block has been executed: *`x`, `y`, `z` are non-negative integers, each less than or equal to 100, representing the number of people who would upvote, downvote, and vote with unknown outcome, respectively. If `x` is greater than the sum of `y` and `z`, then '+' has been printed. If `x` is less than or equal to the sum of `y` and `z`, then if `x` is less than `y`, a hyphen has been printed; otherwise, if `x` equals `y` and `z` is 0, a value `0` has been printed; otherwise, a '?' has been printed.
#Overall this is what the function does:The function accepts three implicit non-negative integers x, y, z, each less than or equal to 100, representing upvotes, downvotes, and unknown votes, respectively, and prints '+' if upvotes exceed the sum of downvotes and unknown votes, '-' if upvotes are less than downvotes, '0' if upvotes equal downvotes and there are no unknown votes, and '?' in all other cases.

