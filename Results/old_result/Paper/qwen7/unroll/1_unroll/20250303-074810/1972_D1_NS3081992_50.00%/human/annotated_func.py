#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each of the next t lines contains two space-separated integers n and m such that 1 ≤ n, m ≤ 2 ⋅ 10^6 and the sum of n and the sum of m over all test cases do not exceed 2 ⋅ 10^6.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns an integer read from standard input, which is within the range of 1 to 10^4.
#Overall this is what the function does:The function reads an integer from standard input, which is within the range of 1 to 10^4, and returns this integer.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6; the sum of n and the sum of m over all test cases do not exceed 2 ⋅ 10^6.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns two integers read from standard input, split and converted to integers.
#Overall this is what the function does:The function reads two integers from standard input, splits them based on whitespace, converts them to integers, and returns them.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of two integers, where the first integer is the value of n and the second integer is the value of m, both read from the standard input.
#Overall this is what the function does:The function reads two integers, `n` and `m`, from the standard input and returns them as a list where `n` is the first element and `m` is the second element.

#State of the program right berfore the function call: rows_number is a non-negative integer such that 1 ≤ rows_number.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #A list containing the result of func_3() called `rows_number` times
#Overall this is what the function does:The function accepts a non-negative integer `rows_number` and returns a list containing the result of calling `func_3()` exactly `rows_number` times.

#State of the program right berfore the function call: `t` is an integer such that `1 \leq t \leq 10^4`, and for each test case, `n` and `m` are integers such that `1 \leq n, m \leq 2 \cdot 10^6`.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns an integer input from standard input, which is within the range of 1 to 10^4.
#Overall this is what the function does:The function reads an integer input from standard input, which must be within the range of 1 to 10^4, and returns this integer.

#State of the program right berfore the function call: None of the variables in the function signature are provided in the given code snippet. The function `func_6` reads input from standard input but does not take any parameters.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a decoded string that is read from standard input, stripped of trailing whitespace.
#Overall this is what the function does:The function reads a string from standard input, removes any trailing whitespace, decodes it from bytes to a string, and returns the resulting string.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each of the next t lines contains two space-separated integers n and m such that 1 ≤ n, m ≤ 2 ⋅ 10^6, and the sum of n and the sum of m over all test cases do not exceed 2 ⋅ 10^6.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers, each pair of integers (n, m) as provided in the input, where 1 ≤ n, m ≤ 2 ⋅ 10^6.
#Overall this is what the function does:The function reads a series of pairs of integers (n, m) from standard input, where each 1 ≤ n, m ≤ 2 ⋅ 10^6, and returns them as a list of integers.

#State of the program right berfore the function call: rows is a non-negative integer representing the number of rows for which to generate results using func_7().
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #A list containing the results of calling func_7() for each row from 0 to rows - 1
#Overall this is what the function does:The function `func_8` accepts a non-negative integer `rows` and returns a list containing the results of calling `func_7()` for each row from 0 to `rows - 1`.

#State of the program right berfore the function call: There is no information provided about the variables in the function signature for `func_9`. However, based on the context, it seems the function should process inputs related to the test cases described in the problem statement. The function likely reads input values for `t`, followed by `t` pairs of integers `n` and `m`, but this is not reflected in the provided function signature.
def func_9():
    return input()
    #The program returns the input provided by the user as a string.
#Overall this is what the function does:The function accepts no parameters and returns the input provided by the user as a string.

#State of the program right berfore the function call: None of the variables in the function signature are present in the provided code snippet. The function does not take any parameters.
def func_10():
    return int(input())
    #The program returns an integer input by the user.
#Overall this is what the function does:The function prompts the user to input an integer and returns this integer.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6.
def func_11():
    return input().split()
    #The program returns a list of strings obtained by splitting the input string at the whitespace boundaries.
#Overall this is what the function does:The function reads an input string from the standard input, splits it into a list of strings based on whitespace boundaries, and returns this list.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers; processing is a list of zeros and ones with the same length as the number of elements in the lists of d; da is an integer key present in the dictionary d; rank is a list of integers with the same length as the number of keys in the dictionary d.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: tmp is 1000000000, d is a dictionary where keys are integers and values are lists of integers, da is an integer key present in the dictionary d, rank is a list of integers with the same length as the number of keys in the dictionary d, and the length of d[da] is not equal to 1
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: Output State: tmp is the minimum value between the initial tmp (1000000000) and the values returned by `func_12(d, processing, di, rank)` for each `di` in `d[da]` where `processing[di - 1]` is initially 0. For each such `di`, `processing[di - 1]` is temporarily set to 1 during the iteration but reverts back to 0 after the iteration. The `rank` list and the dictionary `d` remain unchanged.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns the value of `tmp` incremented by 1, where `tmp` is the minimum value between the initial tmp (1000000000) and the values returned by `func_12(d, processing, di, rank)` for each `di` in `d[da]` where `processing[di - 1]` is initially 0 and then reverted to 0; `rank[da - 1]` is `tmp + 1`.
#Overall this is what the function does:The function accepts a dictionary `d` where keys are integers and values are lists of integers, a list `processing` of zeros and ones with the same length as the number of elements in the lists of `d`, an integer key `da` present in the dictionary `d`, and a list `rank` of integers with the same length as the number of keys in the dictionary `d`. It returns 1 if the length of `d[da]` is 1. Otherwise, it recursively calculates the minimum value between the initial `tmp` (1000000000) and the values returned by `func_12(d, processing, di, rank)` for each `di` in `d[da]` where `processing[di - 1]` is initially 0 and then reverted to 0. Finally, it sets `rank[da - 1]` to `tmp + 1` and returns `tmp + 1`.

#State of the program right berfore the function call: a and b are positive integers, and b is not zero.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns x as 1, y as 0, and a as a positive integer.
    #State: a and b are positive integers, and b is not zero
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns y, x - a // b * y, and g, where y, x, and g are the results of func_13(b, a % b)
#Overall this is what the function does:The function `func_13` accepts two parameters, `a` and `b`, both of which are positive integers with `b` not being zero. It returns three values: `x`, `y`, and `g`. If `b` is zero, it returns `x` as 1, `y` as 0, and `a` as a positive integer. Otherwise, it recursively calls itself with `b` and `a % b`, and returns the results adjusted according to the Euclidean algorithm for finding the greatest common divisor (GCD).

#State of the program right berfore the function call: a is a list of integers, n and m are positive integers such that 0 <= n and 0 <= m, and k is an integer.
def func_14(a, n, m, k):
    for i in range(n):
        if a[i] < m:
            k -= m - a[i]
        
    #State: Output State: a is a list of integers where each element that was less than m has had the difference between m and its original value subtracted from k.
    if (k >= 0) :
        return 1
        #The program returns 1
    #State: a is a list of integers where each element that was less than m has had the difference between m and its original value subtracted from k, and k is less than 0
    return -1
    #The program returns -1
#Overall this is what the function does:The function accepts a list of integers `a`, two non-negative integers `n` and `m`, and an integer `k`. It iterates through the first `n` elements of `a`, adjusting `k` based on the difference between `m` and any element in `a` that is less than `m`. If `k` is non-negative after the iteration, the function returns 1; otherwise, it returns -1.

