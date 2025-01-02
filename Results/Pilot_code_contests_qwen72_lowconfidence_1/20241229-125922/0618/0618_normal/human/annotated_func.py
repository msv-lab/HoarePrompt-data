#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 < a + b + c + d ≤ 10^5.
def func_1():
    a, b, c, d = func_3()
    s1 = b - a
    s2 = c - d
    if (s1 == s2) :
        out = [1, 0] * a + [1, 2] * (b - a) + [3, 2] * d
    else :
        if (s1 + 1 == s2) :
            if (a > 0) :
                a -= 1
                out = [0] + [1, 0] * a + [1, 2] * (b - a) + [3, 2] * d
            else :
                c -= 1
                out = [2] + [1, 0] * a + [1, 2] * (b - a) + [3, 2] * d
            #State of the program after the if-else block has been executed: *`a`, `b`, `c`, and `d` are non-negative integers such that 0 < a + b + c + d ≤ 10^5, and they have been updated to the values returned by `func_3()`. `s1` is not equal to `s2`. If `a > 0`, `s1` is equal to `b - a + 1`, `s2` is equal to `c - d`, the current value of `s1 + 1` is equal to `s2`, and `out` is a list constructed as `[0] + [1, 0] * a + [1, 2] * (b - a) + [3, 2] * d` with a length of 1 + 2b + 2d. If `a == 0`, `a` is 0, `b` remains unchanged, `c` is `c - 1`, `d` remains unchanged, `s1` is `b`, `s2` is `b + 2`, and `out` is `[2] + [1, 2] * b + [3, 2] * d`.
        else :
            if (s1 == s2 + 1) :
                if (d > 0) :
                    d -= 1
                    out = [1, 0] * a + [1, 2] * (b - a) + [3, 2] * d + [3]
                else :
                    b -= 1
                    out = [1, 0] * a + [1, 2] * (b - a) + [3, 2] * d + [1]
                #State of the program after the if-else block has been executed: *`a`, `b`, `c`, and `d` are non-negative integers such that \(0 < a + b + c + d \leq 10^5\). If `d > 0`, `d` is decremented by 1, `s2` is updated to `c - (d - 1)`, and `out` is a list constructed as `[1, 0] * a + [1, 2] * (b - a) + [3, 2] * (d - 1) + [3]`. If `d` is 0, `b` is decremented by 1, `s1` is equal to `s2`, and `out` is `[1, 0] * a + [1, 2] * (b - a) + [1]`. In both cases, `s1` is equal to `b - a`, `s1` is not equal to `s2`, and `s1 + 1` is not equal to `s2`.
            else :
                print('NO')
                return
                #The program does not return any value
            #State of the program after the if-else block has been executed: *`a`, `b`, `c`, and `d` are non-negative integers such that \(0 < a + b + c + d \leq 10^5\). If `d > 0`, `d` is decremented by 1, `s2` is updated to `c - (d - 1)`, and `out` is a list constructed as `[1, 0] * a + [1, 2] * (b - a) + [3, 2] * (d - 1) + [3]`. If `d` is 0, `b` is decremented by 1, `s1` is equal to `s2`, and `out` is `[1, 0] * a + [1, 2] * (b - a) + [1]`. In both cases, `s1` is equal to `b - a`, `s1` is not equal to `s2`, and `s1 + 1` is not equal to `s2`.
        #State of the program after the if-else block has been executed: *`a`, `b`, `c`, and `d` are non-negative integers such that \(0 < a + b + c + d \leq 10^5\), and they have been updated to the values returned by `func_3()`. `s1` is not equal to `s2`. If `s1 + 1 == s2`, then: 
        #- If `a > 0`, `s1` is equal to `b - a + 1`, `s2` is equal to `c - d`, the current value of `s1 + 1` is equal to `s2`, and `out` is a list constructed as `[0] + [1, 0] * a + [1, 2] * (b - a) + [3, 2] * d` with a length of 1 + 2b + 2d.
        #- If `a == 0`, `a` is 0, `b` remains unchanged, `c` is `c - 1`, `d` remains unchanged, `s1` is `b`, `s2` is `b + 2`, and `out` is `[2] + [1, 2] * b + [3, 2] * d`.
        #Otherwise, if `s1 + 1 != s2`:
        #- If `d > 0`, `d` is decremented by 1, `s2` is updated to `c - (d - 1)`, and `out` is a list constructed as `[1, 0] * a + [1, 2] * (b - a) + [3, 2] * (d - 1) + [3]`.
        #- If `d` is 0, `b` is decremented by 1, `s1` is equal to `b - a`, and `out` is `[1, 0] * a + [1, 2] * (b - a) + [1]`.
        #In all cases, `s1` is equal to `b - a`, `s1` is not equal to `s2`, and `s1 + 1` is not equal to `s2`.
    #State of the program after the if-else block has been executed: *`a`, `b`, `c`, and `d` are non-negative integers such that 0 < a + b + c + d ≤ 10^5, and they have been updated to the values returned by `func_3()`. `s1` is equal to `b - a`, and `s2` is equal to `c - d`. If `s1 == s2`, `out` is a list constructed as `[1, 0] * a + [1, 2] * (b - a) + [3, 2] * d`. Otherwise, if `s1 + 1 == s2`:
    #- If `a > 0`, `s1` is equal to `b - a + 1`, `s2` is equal to `c - d`, the current value of `s1 + 1` is equal to `s2`, and `out` is a list constructed as `[0] + [1, 0] * a + [1, 2] * (b - a) + [3, 2] * d` with a length of 1 + 2b + 2d.
    #- If `a == 0`, `a` is 0, `b` remains unchanged, `c` is `c - 1`, `d` remains unchanged, `s1` is `b`, `s2` is `b + 2`, and `out` is `[2] + [1, 2] * b + [3, 2] * d`.
    #If `s1 + 1 != s2`:
    #- If `d > 0`, `d` is decremented by 1, `s2` is updated to `c - (d - 1)`, and `out` is a list constructed as `[1, 0] * a + [1, 2] * (b - a) + [3, 2] * (d - 1) + [3]`.
    #- If `d` is 0, `b` is decremented by 1, `s1` is equal to `b - a`, and `out` is `[1, 0] * a + [1, 2] * (b - a) + [1]`.
    #In all cases, `s1` is equal to `b - a`, `s1` is not equal to `s2`, and `s1 + 1` is not equal to `s2`.
    print('YES')
    print(*out)
#Overall this is what the function does:The function `func_1` does not accept any parameters and does not return any value. It modifies the variables `a`, `b`, `c`, and `d` based on the values returned by `func_3`. The function constructs a list `out` based on the relationships between `a`, `b`, `c`, and `d` and prints "YES" followed by the elements of `out`. If certain conditions are not met, the function prints "NO" and exits early. The final state of the program is that `a`, `b`, `c`, and `d` are non-negative integers such that \(0 < a + b + c + d \leq 10^5\), and `out` is a list of integers constructed according to the rules described below:

1. If \(s1 = b - a\) is equal to \(s2 = c - d\):
   - `out` is constructed as `[1, 0] * a + [1, 2] * (b - a) + [3, 2] * d`.

2. If \(s1 + 1 = s2\):
   - If `a > 0`:
     - `a` is decremented by 1.
     - `out` is constructed as `[0] + [1, 0] * a + [1, 2] * (b - a) + [3, 2] * d`.
   - If `a == 0`:
     - `c` is decremented by 1.
     - `out` is constructed as `[2] + [1, 2] * b + [3, 2] * d`.

3. If \(s1 = s2 + 1\):
   - If `d > 0`:
     - `d` is decremented by 1.
     - `out` is constructed as `[1, 0] * a + [1, 2] * (b - a) + [3, 2] * d + [3]`.
   - If `d == 0`:
     - `b` is decremented by 1.
     - `out` is constructed as `[1, 0] * a + [1, 2] * (b - a) + [1]`.

4. If none of the above conditions are met, the function prints "NO" and exits early without constructing `out`.

In all cases where `out` is constructed, the function prints "YES" followed by the elements of `out`. The final state of the program is that `a`, `b`, `c`, and `d` are updated to the values returned by `func_3` and modified according to the conditions described above.

#State of the program right berfore the function call: x and y are non-negative integers.
def func_2(x, y):
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: `y` is 0, `x` is the GCD of the original values of `x` and `y`.
    return x
    #The program returns the GCD of the original values of `x` and `y`, where `y` is 0. Since the GCD of any number and 0 is the number itself, the program returns the original value of `x`.
#Overall this is what the function does:The function `func_2` accepts two non-negative integer parameters `x` and `y`. It computes and returns the greatest common divisor (GCD) of the original values of `x` and `y`. After the function executes, `x` holds the GCD of the original `x` and `y`, and `y` is 0. The function correctly handles the case where either or both of the inputs are 0, returning the non-zero value or 0 if both are 0.

#State of the program right berfore the function call: No variables are passed to the function. The function reads four non-negative integers a, b, c, and d from the standard input, where 0 < a + b + c + d ≤ 10^5.
def func_3():
    return list(map(int, input().split()))
    #The program returns a list of four non-negative integers [a, b, c, d] read from the standard input, where 0 < a + b + c + d ≤ 10^5.
#Overall this is what the function does:The function `func_3` reads four non-negative integers from the standard input, where the sum of these integers is greater than 0 and less than or equal to 10^5. It returns a list containing these four integers. If the input does not conform to the expected format (e.g., fewer or more than four integers, or integers that do not satisfy the sum condition), the behavior is undefined.

#State of the program right berfore the function call: f is a callable object, dim is a tuple of non-negative integers.
def func_4(f):
    return [func_4(f, *dim[1:]) for _ in range(dim[0])] if dim else f()
    #The program returns a list containing `dim[0]` elements, each element being the result of calling `func_4(f, *dim[1:])`, if `dim` is not empty; otherwise, it returns the result of calling `f()`
#Overall this is what the function does:The function `func_4` takes a callable object `f` and a tuple `dim` of non-negative integers. It recursively constructs a nested list structure where the depth of the nesting corresponds to the length of `dim`. Each level of the list contains `dim[i]` elements, and the final elements are the result of calling `f()`. If `dim` is empty, the function directly returns the result of calling `f()`. The function ensures that the returned structure is a list of lists (or a single value if `dim` is empty), with the dimensions specified by `dim`.

#State of the program right berfore the function call: start is an integer representing the starting value of the range, step is an integer representing the difference between each consecutive value in the range, and count is a non-negative integer representing the number of values to generate in the range.
def func_5(start, step, count):
    return range(start, start + step * count, step)
    #The program returns a range object that starts from `start`, ends before `start + step * count`, and increments by `step`.
#Overall this is what the function does:The function `func_5` accepts three parameters: `start` (an integer representing the starting value of the range), `step` (an integer representing the difference between each consecutive value in the range), and `count` (a non-negative integer representing the number of values to generate in the range). It returns a range object that starts from `start`, ends before `start + step * count`, and increments by `step`. If `step` is zero and `count` is greater than zero, the function will return an empty range object because the end value will be equal to the start value, resulting in no progression. If `count` is zero, the function will also return an empty range object since no values are generated.

#State of the program right berfore the function call: l is a list, start is a non-negative integer, and end is an integer such that 0 <= start <= len(l) and end >= 0.
def func_6(l, start, end):
    return range(start, len(l) + end)
    #The program returns a range object from `start` to `len(l) + end`. Here, `start` is a non-negative integer, `len(l)` is the length of the list `l`, and `end` is an integer such that the end point of the range is `len(l) + end`.
#Overall this is what the function does:The function `func_6` accepts a list `l`, a non-negative integer `start`, and an integer `end`. It returns a range object starting from `start` up to, but not including, `len(l) + end`. The list `l` remains unchanged. If `end` is negative, the upper bound of the range can be less than `start`, resulting in an empty range. If `end` is zero, the range will extend from `start` to the end of the list `l`. If `end` is positive, the range will extend beyond the length of the list `l`.

#State of the program right berfore the function call: n is a positive integer.
def func_7(n):
    return 2 ** (n - 1).bit_length()
    #The program returns the smallest power of 2 that is greater than or equal to `n`.
#Overall this is what the function does:The function `func_7` accepts a positive integer `n` and returns the smallest power of 2 that is greater than or equal to `n`. This means that for any given `n`, the function computes the smallest integer `m` such that \(2^m \geq n\). The function correctly handles all positive integers, including edge cases like `n = 1` where the result is `1` (since \(2^0 = 1\)). The function does not handle non-positive integers or non-integer inputs, as it assumes `n` is a positive integer. After the function executes, the program state is unchanged except for the returned value, which is the smallest power of 2 greater than or equal to `n`.

#State of the program right berfore the function call: x and r are integers such that r > 0.
def func_8(x, r):
    return (x + r - 1) // r
    #The program returns the integer division result of (x + r - 1) divided by r, where x is an integer and r is a positive integer.
#Overall this is what the function does:The function `func_8` accepts two parameters `x` and `r`, where `x` is an integer and `r` is a positive integer. It returns the integer division result of `(x + r - 1)` divided by `r`. This effectively rounds up the division of `x` by `r` to the nearest whole number. For example, if `x = 5` and `r = 3`, the function returns `2` because `(5 + 3 - 1) // 3 = 7 // 3 = 2`. The function handles all valid integer inputs for `x` and positive integer inputs for `r`. If `r` is not a positive integer, the behavior is undefined and may lead to errors or incorrect results.

