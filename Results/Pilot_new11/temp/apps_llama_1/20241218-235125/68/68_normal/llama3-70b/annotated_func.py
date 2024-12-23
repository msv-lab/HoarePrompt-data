#State of the program right berfore the function call: The function takes no arguments, but the input to the program will be three non-negative integers x, y, z (0 <= x, y, z <= 100), representing the number of persons who would upvote, downvote, or vote with unknown outcome.
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
                #State of the program after the if-else block has been executed: `x`, `y`, and `z` are non-negative integers, `x` equals `y`, `x` is less than or equal to `y + z`, if `z` is 0, then the state of `x`, `y`, and `z` remains as is. If `z` is greater than 0, then a '?' has been printed, and `x`, `y`, and `z` are still non-negative integers with `x` equal to `y` and `x` less than or equal to `y + z`.
            else :
                print('?')
            #State of the program after the if-else block has been executed: `x`, `y`, and `z` are non-negative integers, `x` is less than or equal to `y + z`, `x` is greater than or equal to `y`. If `x` equals `y`, then if `z` is 0, the state of `x`, `y`, and `z` remains as is; if `z` is greater than 0, a '?' has been printed and `x`, `y`, and `z` are still non-negative integers with `x` equal to `y`. If `x` does not equal `y`, then a '?' has been printed to the console.
        #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers (0 <= x, y, z <= 100), `x` is less than or equal to `y + z`. If `x` is less than `y`, a hyphen (-) has been printed to the console. If `x` is greater than or equal to `y`, then if `x` equals `y` and `z` is 0, the state of `x`, `y`, and `z` remains as is; if `x` equals `y` and `z` is greater than 0, or if `x` is greater than `y`, a '?' has been printed to the console, and in all these cases, `x`, `y`, and `z` are still non-negative integers with `x` being either equal to or greater than `y`.
    #State of the program after the if-else block has been executed: `x`, `y`, and `z` are non-negative integers (0 <= x, y, z <= 100), if `x` is greater than the sum of `y` and `z`, '+' has been printed. If `x` is less than or equal to the sum of `y` and `z`, then if `x` is less than `y`, a hyphen (-) has been printed; if `x` is greater than or equal to `y`, then if `x` equals `y` and `z` is 0, the state of `x`, `y`, and `z` remains as is, otherwise, if `x` equals `y` and `z` is greater than 0, or if `x` is greater than `y`, a '?' has been printed, with `x`, `y`, and `z` remaining non-negative integers and `x` being either equal to or greater than `y`.
#Overall this is what the function does:The function reads three non-negative integers x, y, z, representing upvotes, downvotes, and unknown outcome votes, and prints an outcome based on these inputs. The outcome is '+' if x is greater than y + z, '-' if x is less than y, '0' if x equals y and z is 0, and '?' in all other cases where x is less than or equal to y + z and either x equals y with z greater than 0 or x is greater than y. After execution, the state of the program will have printed one of these four outcomes to the console, with x, y, and z remaining as input non-negative integers. The function does not modify the input values or return any value, only printing the determined outcome to the console.

