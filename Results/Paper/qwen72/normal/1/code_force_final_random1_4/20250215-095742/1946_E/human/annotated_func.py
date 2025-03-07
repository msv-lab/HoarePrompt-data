#State of the program right berfore the function call: a and b are non-negative integers such that b <= a.
def func_1(a, b):
    if (b == 0) :
        return 1, 0
        #The program returns the tuple (1, 0)
    #State: a and b are non-negative integers such that b <= a, and b is not equal to 0
    if (a < b) :
        c, d = func_1(b, a)
        return d, c
        #The program returns the values of `d` and `c`, which are the results of `func_1(b, a)`. Since `b` is a non-negative integer and `b <= a`, but the current value of `a` is less than the current value of `b`, this implies that `a` and `b` have swapped values or `a` has been updated to a value less than `b` before calling `func_1`. The exact values of `c` and `d` depend on the implementation of `func_1`, but they are the outputs of `func_1` when called with `b` and `a` as arguments.
    #State: a and b are non-negative integers such that b <= a, and b is not equal to 0, and a is greater than or equal to b
    if (a % b == 0) :
        return 1, -(a // b - 1)
        #The program returns a tuple (1, -((a // b) - 1)), where `a` is a non-negative integer divisible by `b` with no remainder, and `b` is a non-negative integer not equal to 0 and less than or equal to `a`. The first element of the tuple is 1, and the second element is the negative of the quotient of `a` divided by `b` minus 1.
    #State: a and b are non-negative integers such that b <= a, b is not equal to 0, a is greater than or equal to b, and a is not divisible by b
    c, d = func_1(b, a % b)
    return d, c - a // b * d
    #The program returns a tuple `(d, c - a // b * d)` where `d` and `c` are the results of the function call `func_1(b, a % b)`. Here, `d` is the second result from `func_1`, and the second value in the tuple is calculated by subtracting the product of `a` divided by `b` (integer division) and `d` from `c`.
#Overall this is what the function does:The function `func_1` takes two non-negative integers, `a` and `b`, with the constraint that `b` is less than or equal to `a`. It returns a tuple of two integers. Depending on the values of `a` and `b`, the function can return one of the following:

1. If `b` is 0, the function returns the tuple (1, 0).
2. If `a` is less than `b`, the function swaps the values of `a` and `b` and returns the results of `func_1(b, a)`, swapping the order of the returned tuple.
3. If `a` is divisible by `b` with no remainder, the function returns the tuple (1, -((a // b) - 1)).
4. If none of the above conditions are met, the function recursively calls itself with `b` and `a % b`, and returns a tuple where the first element is the second result of the recursive call, and the second element is the first result of the recursive call minus the product of `a` divided by `b` (integer division) and the second result of the recursive call.

#State of the program right berfore the function call: a is an integer, b is a non-negative integer, and it is implied that a and b are related to the computation of permutations or their counts, possibly representing a count of permutations or a part of the permutation's structure.
def func_2(a, b):
    c, d = func_1(b, 1000000007)
    return c * a % 1000000007
    #The program returns the result of (c * a) % 1000000007, where `c` is one of the results from the function `func_1(b, 1000000007)` and `a` is an integer.
#Overall this is what the function does:The function `func_2` takes two parameters, `a` (an integer) and `b` (a non-negative integer). It computes the result of `(c * a) % 1000000007`, where `c` is the first element returned by the function `func_1(b, 1000000007)`. The function returns this computed value.

