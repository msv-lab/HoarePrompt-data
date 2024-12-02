#State of the program right berfore the function call: a and b are non-negative integers with no more than 10^6 digits.**
def func():
    a = input().lstrip('0')
    b = input().lstrip('0')
    if (a == b) :
        print('=')
    else :
        if (a < b) :
            print('<')
        else :
            print('>')
        #State of the program after the if-else block has been executed: *`a`, `b` are non-negative integers with no leading zeroes and not equal to each other. If `a` < `b`, then '<' is printed indicating that `a` is less than `b`. If `a` >= `b`, then the program continues with `a` being greater than or equal to `b`.
    #State of the program after the if-else block has been executed: *a, b are non-negative integers with no leading zeroes. If a is equal to b, then both a and b have the same value. If a is not equal to b, then the program outputs '<' if a < b, indicating that a is less than b. If a >= b, the program continues with a being greater than or equal to b.
#Overall this is what the function does:The function `func` reads two non-negative integers `a` and `b` with no leading zeroes. It then compares the values of `a` and `b` and prints '=' if they are equal, '<' if `a` is less than `b`, and '>' if `a` is greater than `b`. The functionality does not cover cases where `a` and `b` have leading zeroes or if the inputs are not valid non-negative integers.

