#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns an integer read from standard input, which is within the range 1 ≤ t ≤ 10^4 for each test case.
#Overall this is what the function does:The function reads an integer from standard input, which is guaranteed to be within the range 1 ≤ t ≤ 10^4, and returns this integer.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object containing integers read from the standard input buffer, split by spaces.
#Overall this is what the function does:The function reads integers from the standard input buffer, splits them by spaces, and returns a map object containing these integers.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each of the next t lines contains two space-separated integers n and m such that 1 ≤ n, m ≤ 2⋅10^6 and the sum of n and the sum of m over all test cases do not exceed 2⋅10^6.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list containing two integers n and m as specified in the input, where each line of input contains these two integers separated by a space.
#Overall this is what the function does:The function reads a single line of input from the standard buffer, splits it into two space-separated integers, and returns them as a list. This list contains the values of n and m as specified in the input.

#State of the program right berfore the function call: rows_number is a positive integer representing the number of test cases. Each test case consists of two positive integers n and m, where 1 ≤ n, m ≤ 2 ⋅ 10^6, and the sum of n or m over all test cases does not exceed 2 ⋅ 10^6.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #A list containing the result of func_3() called `rows_number` times
#Overall this is what the function does:The function accepts a positive integer `rows_number` representing the number of test cases. For each test case, it calls `func_3()` with two positive integers `n` and `m`. It then returns a list containing the results of these calls.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns a string read from standard input, stripped of trailing whitespace.
#Overall this is what the function does:The function reads a single line of input from the standard input buffer, strips any trailing whitespace, and returns it as a string. This action is performed regardless of any potential variations in input length or content within the given constraints.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a string decoded from bytes read from standard input, which is trimmed of trailing whitespace.
#Overall this is what the function does:The function reads a line of input from standard input as bytes, decodes it into a string, and removes any trailing whitespace before returning the resulting string.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each of the next t lines contains two space-separated integers n and m such that 1 ≤ n, m ≤ 2⋅10^6 and the sum of n or m over all test cases does not exceed 2⋅10^6.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers, each pair of which corresponds to the values of n and m from the input, where 1 ≤ n, m ≤ 2⋅10^6.
#Overall this is what the function does:The function reads a series of pairs of integers (n, m) from the standard input, where each 1 ≤ n, m ≤ 2⋅10^6, and returns them as a list of integers.

#State of the program right berfore the function call: rows is a non-negative integer such that 0 <= rows.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #A list containing the result of `func_7()` called `rows` times
#Overall this is what the function does:The function accepts a non-negative integer `rows` and returns a list containing the result of calling `func_7()` exactly `rows` times.

#State of the program right berfore the function call: This function does not take any parameters and it seems to be incomplete or out of context for the problem description. There are no variables related to the problem's conditions in this function signature.
def func_9():
    return input()
    #The program returns the input provided by the user.
#Overall this is what the function does:The function does not accept any parameters and returns the input provided by the user through the `input()` function.

#State of the program right berfore the function call: None of the variables in the function signature are present in the provided code snippet. The function `func_10` reads input but does not take any parameters.
def func_10():
    return int(input())
    #The program returns an integer input by the user.
#Overall this is what the function does:The function reads an integer input from the user and returns it.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_11():
    return input().split()
    #The program returns a list of strings containing the values of `n` and `m` separated by spaces.
#Overall this is what the function does:The function reads input from the standard input, splits it into a list of strings, and returns this list. The list contains two elements: the values of `n` and `m`, which are separated by spaces.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers; processing is a list of length equal to the maximum key in d, initialized with zeros; da is an integer which is a key in the dictionary d; rank is a list of integers with the same length as the maximum key in d, initialized with zeros.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: `d` is a dictionary where keys are integers and values are lists of integers; `processing` is a list of length equal to the maximum key in `d`, initialized with zeros; `da` is an integer which is a key in the dictionary `d`; `rank` is a list of integers with the same length as the maximum key in `d`, initialized with zeros; `tmp` is 1000000000; the length of `d[da]` is greater than 1
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: Output State: The dictionary `d` remains unchanged, `processing` is a list of length equal to the maximum key in `d`, with all elements set to zero, `da` is an integer which is a key in the dictionary `d`, `rank` is a list of integers with the same length as the maximum key in `d`, with all elements set to zero, `tmp` is the minimum value obtained from repeatedly calling `func_12(d, processing, di, rank)` for each `di` in `d[da]` during the entire execution of the loop, and `di` has iterated through all elements in `d[da]`.
    #
    #In simpler terms, after the loop completes all its iterations, the dictionary `d` and the list `da` remain unchanged. The `processing` list still contains zeros everywhere. The `rank` list also remains unchanged. The variable `tmp` holds the smallest value returned by `func_12(d, processing, di, rank)` for any `di` in `d[da]` over all iterations of the loop. The variable `di` has gone through every element in `d[da]`.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #`The program returns the value of tmp + 1, where tmp is the minimum value obtained from repeatedly calling func_12(d, processing, di, rank) for each di in d[da] during the entire execution of the loop`
#Overall this is what the function does:The function accepts a dictionary `d` where keys are integers and values are lists of integers, a list `processing` of the same length as the maximum key in `d`, initialized with zeros, an integer `da` which is a key in the dictionary `d`, and a list `rank` of the same length as the maximum key in `d`, initialized with zeros. It returns 1 if the length of `d[da]` is 1. Otherwise, it recursively calls itself for each element `di` in `d[da]`, updating the `processing` list and calculating the minimum value `tmp`. Finally, it sets `rank[da - 1]` to `tmp + 1` and returns this value.

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
    #The program returns y, x - a // b * y, and g, where y, x, and g are the results of the func_13(b, a % b) function call, and x is the quotient, y is the remainder when a is divided by b, and g is the greatest common divisor of a and b.
#Overall this is what the function does:The function `func_13` accepts two parameters, `a` and `b`, which are positive integers and `b` is not zero. It returns a tuple containing three elements: `x`, `y`, and `g`. In the first case, if `b` is zero, it returns `x` as 1, `y` as 0, and `a` as a positive integer. In the second case, it recursively calls itself with `b` and `a % b`, and returns `y`, `x - a // b * y`, and `g`, where `y` and `x` are the results of the recursive call, and `g` is the greatest common divisor of `a` and `b`.

#State of the program right berfore the function call: a is a list of integers, n and m are non-negative integers such that 0 <= n, m <= 2 * 10^6, and k is an integer.
def func_14(a, n, m, k):
    for i in range(n):
        if a[i] < m:
            k -= m - a[i]
        
    #State: Output State: After the loop executes all iterations, `i` will be equal to `n`, `n` will remain unchanged, and `k` will be updated based on the condition `a[i] < m` for each `i` from `0` to `n-1`. Specifically, for each index `i` where `a[i]` is less than `m`, `k` will be decreased by the amount `m - a[i]`.
    #
    #In simpler terms, after the loop completes, `i` will have reached the end of the list (equal to `n`), `n` will stay the same as it was initially, and `k` will have been adjusted according to how many elements in the list `a` were less than `m`, with each such element reducing `k` by the difference `m - a[i]`.
    if (k >= 0) :
        return 1
        #The program returns 1
    #State: `i` will be equal to `n`, `n` will remain unchanged, and `k` will be updated based on the condition `a[i] < m` for each `i` from `0` to `n-1`. Specifically, for each index `i` where `a[i]` is less than `m`, `k` will be decreased by the amount `m - a[i]`. Additionally, `k` will be less than 0.
    return -1
    #The program returns -1
#Overall this is what the function does:The function accepts a list of integers `a`, two non-negative integers `n` and `m`, and an integer `k`. It iterates through the first `n` elements of the list `a`, adjusting `k` based on whether each element is less than `m`. If `k` remains non-negative after processing all elements, the function returns 1; otherwise, it returns -1.

#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6 and \(1 \leq i \leq m\) and \(i^2 \leq n + i\).
def func_15():
    n, m = func_7()
    i = 1
    ans = 0
    while i <= m and i * i <= n + i:
        ans += (n + i) // (i * i)
        
        i += 1
        
    #State: Output State: `i` is the smallest integer greater than or equal to the square root of `n + m`, `n` is the return value of `func_7()`, `m` is the return value of `func_7()`, `ans` is the sum of `(n + i) // (i * i)` for all `i` from 1 to the smallest integer greater than or equal to the square root of `n + m`.
    #
    #To explain further, the loop continues as long as `i` is less than or equal to `m` and `i * i` is less than or equal to `n + i`. The loop increments `i` by 1 each time it runs, and in each iteration, it adds `(n + i) // (i * i)` to `ans`. The loop will terminate when `i` exceeds `m` or when `i * i` exceeds `n + i`. Therefore, `i` will be the smallest integer such that `i * i > n + i`, which is approximately the square root of `n + m`. The final value of `ans` will be the sum of the contributions from each iteration of the loop.
    return ans - 1
    #The program returns the value of `ans` minus 1, where `ans` is the sum of `(n + i) // (i * i)` for all `i` from 1 to the smallest integer greater than or equal to the square root of `n + m`, with `n` and `m` being the return values of `func_7()` and `ans` being calculated as described.
#Overall this is what the function does:The function accepts no parameters and returns the value of `ans` minus 1, where `ans` is the sum of `(n + i) // (i * i)` for all `i` from 1 to the smallest integer greater than or equal to the square root of `n + m`, with `n` and `m` being the return values of `func_7()`.

#State of the program right berfore the function call: func_10 returns an integer representing the number of test cases (t), where 1 ≤ t ≤ 10^4. func_15 processes each test case and returns an integer representing the number of valid pairs for that test case. Each test case consists of two integers n and m, where 1 ≤ n, m ≤ 2 ⋅ 10^6, and the sum of n and m over all test cases does not exceed 2 ⋅ 10^6.
def func_16():
    for _ in range(func_10()):
        sys.stdout.write(str(func_15()) + '\n')
        
    #State: The output state will include `sys.stdout.write` being called `func_10()` times, each time writing the value returned by `func_15()` followed by a newline character.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \( n \) and \( m \). It calls `func_15()` for each test case to determine the number of valid pairs and writes these values to standard output, followed by a newline. The total number of test cases processed is determined by `func_10()`, which returns an integer between 1 and \( 10^4 \). The sum of \( n \) and \( m \) across all test cases does not exceed \( 2 \cdot 10^6 \).

