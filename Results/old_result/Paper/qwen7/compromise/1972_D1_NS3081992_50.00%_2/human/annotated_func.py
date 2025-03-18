#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program reads an integer from standard input (sys.stdin.buffer.readline()) and returns it. The integer read is within the range 1 ≤ t ≤ 10^4.
#Overall this is what the function does:The function reads an integer from standard input, which must be within the range 1 ≤ t ≤ 10^4, and returns this integer.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object containing integers read from the standard input, specifically the integers split from a single line of space-separated values.
#Overall this is what the function does:The function reads a single line of space-separated integers from the standard input, splits the line into individual integers, and returns a map object containing these integers.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of two integers, which are the values of n and m read from the standard input.
#Overall this is what the function does:The function reads two integers, `n` and `m`, from the standard input and returns them as a list. The integers `n` and `m` are constrained such that `1 ≤ n, m ≤ 2 ⋅ 10^6`.

#State of the program right berfore the function call: rows_number is a non-negative integer such that 1 ≤ rows_number ≤ 10^4.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #A list containing the result of `func_3()` called `rows_number` times
#Overall this is what the function does:The function `func_4` accepts a parameter `rows_number`, a non-negative integer within the range of 1 to 10^4, and returns a list. This list contains the results of calling another function `func_3()` exactly `rows_number` times.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns a string read from standard input buffer, stripped of any trailing whitespace.
#Overall this is what the function does:The function reads a line of input from the standard input buffer, strips any trailing whitespace, and returns it as a string. This process is performed without requiring any input parameters.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each of the next t lines contains two space-separated integers n and m such that 1 ≤ n, m ≤ 2 ⋅ 10^6, and the sum of n and the sum of m over all test cases do not exceed 2 ⋅ 10^6.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a line from the standard input buffer as a decoded string after stripping any trailing whitespace.
#Overall this is what the function does:The function reads a single line from the standard input buffer, strips any trailing whitespace, and decodes it into a string before returning it.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers obtained by splitting the input string and converting each element to an integer.
#Overall this is what the function does:The function reads a single line of space-separated integers from the standard input, splits the line into individual elements, converts each element to an integer, and returns a list of these integers.

#State of the program right berfore the function call: rows is a non-negative integer such that 0 <= rows.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #A list containing the result of func_7() called `rows` times
#Overall this is what the function does:The function accepts a non-negative integer `rows` and returns a list containing the result of calling `func_7()` exactly `rows` times.

#State of the program right berfore the function call: None of the variables in the function signature are present or used in the provided code snippet. The function does not take any parameters and does not contribute to solving the described problem.
def func_9():
    return input()
    #The program returns the user's input from the input() function call
#Overall this is what the function does:The function accepts no parameters and returns the user's input from the `input()` function call.

#State of the program right berfore the function call: There is no input parameter for the function, and it should read an integer t from the standard input, where 1 ≤ t ≤ 10^4, indicating the number of test cases. For each test case, it should read two integers n and m, where 1 ≤ n, m ≤ 2⋅10^6, and the sum of n or m over all test cases does not exceed 2⋅10^6.
def func_10():
    return int(input())
    #The program reads an integer t from the standard input, where 1 ≤ t ≤ 10^4, indicating the number of test cases, and then returns that integer t.
#Overall this is what the function does:The function reads an integer t from the standard input, where 1 ≤ t ≤ 10^4, indicating the number of test cases, and returns that integer t.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6.
def func_11():
    return input().split()
    #The program returns a list of strings containing the values of `n` and `m` separated by spaces.
#Overall this is what the function does:The function reads input from the standard input, splits it into two parts, and returns them as a list of strings. The list contains the values of `n` and `m`, which are separated by spaces.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers; processing is a list of length max(da) containing only 0s and 1s; da and rank are integers such that 1 <= da <= max(da) and rank is a list of length max(da) initialized with zeros.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: Postcondition: `tmp` is 1000000000, `d` is a dictionary where keys are integers and values are lists of integers; `processing` is a list of length `max(da)` containing only 0s and 1s; `da` and `rank` are integers such that 1 <= `da` <= `max(da)`, and `rank` is a list of length `max(da)` initialized with zeros. `len(d[da])` is greater than 1.
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: `tmp` is updated to the minimum value of `func_12(d, processing, di, rank)` for each `di` in `d[da]` where `processing[di - 1]` is initially 0. The `processing` list remains unchanged except for the temporary changes made inside the loop. `d`, `da`, `rank`, and `max(da)` retain their original values.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns the value of `rank[da - 1]`, which is `tmp + 1`.
#Overall this is what the function does:The function `func_12` accepts a dictionary `d` where keys are integers and values are lists of integers, a list `processing` of length `max(da)` containing only 0s and 1s, an integer `da`, and a list `rank` of length `max(da)` initialized with zeros. It returns either 1 or the value of `rank[da - 1]`, which is `tmp + 1`. If the length of `d[da]` is 1, the function immediately returns 1. Otherwise, it updates the `processing` list temporarily to mark nodes as processed and recursively calculates the minimum value of `rank[da - 1]` for each node in `d[da]` where `processing[di - 1]` is initially 0. Finally, it sets `rank[da - 1]` to this minimum value plus one and returns this value.

#State of the program right berfore the function call: a and b are non-negative integers where b is non-zero.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns x as 1, y as 0, and a as a non-negative integer.
    #State: a and b are non-negative integers where b is non-zero
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #y, x - a // b * y, g
#Overall this is what the function does:The function `func_13` accepts two non-negative integers `a` and `b` (with `b` being non-zero) and returns a tuple containing three elements: `x`, `y`, and `g`. If `b` is zero, it returns `x` as 1, `y` as 0, and `a` unchanged. Otherwise, it recursively calculates `x`, `y`, and `g` using the values of `b` and the remainder of `a` divided by `b`, and returns `y`, `x - a // b * y`, and `g`.

#State of the program right berfore the function call: a is a list of integers, n and m are non-negative integers, and k is an integer.
def func_14(a, n, m, k):
    for i in range(n):
        if a[i] < m:
            k -= m - a[i]
        
    #State: a is a list of integers where each element that was less than m has been adjusted such that it is now equal to m, and k is reduced by the total amount by which those elements were less than m.
    if (k >= 0) :
        return 1
        #The program returns 1
    #State: a is a list of integers where each element that was less than m has been adjusted such that it is now equal to m, and k is less than 0
    return -1
    #The program returns -1
#Overall this is what the function does:The function accepts a list of integers `a`, two non-negative integers `n` and `m`, and an integer `k`. It adjusts each element in `a` that is less than `m` to be equal to `m` and decreases `k` by the total difference between these elements and `m`. If `k` is greater than or equal to 0 after adjustments, the function returns 1; otherwise, it returns -1.

