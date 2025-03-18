#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns an integer read from standard input within the range of 1 to 10^4.
#Overall this is what the function does:The function reads an integer from standard input within the range of 1 to 10^4 and returns it.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6; the sum of n and the sum of m over all test cases do not exceed 2 ⋅ 10^6.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns two integers, n and m, read from standard input.
#Overall this is what the function does:The function reads two integers, n and m, from standard input, where 1 ≤ t ≤ 10^4, 1 ≤ n, m ≤ 2 ⋅ 10^6, and the sum of n and m over all test cases does not exceed 2 ⋅ 10^6. It then returns these two integers, n and m.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of integers [n, m] read from standard input.
#Overall this is what the function does:The function reads two integers, `n` and `m`, from standard input and returns them as a list `[n, m]`. Both `n` and `m` must satisfy the conditions 1 ≤ n, m ≤ 2⋅10^6 and are guaranteed to be integers.

#State of the program right berfore the function call: rows_number is a positive integer such that 1 ≤ rows_number.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #A list containing the result of func_3() called `rows_number` times
#Overall this is what the function does:The function accepts a positive integer `rows_number` and returns a list containing the result of calling `func_3()` `rows_number` times.

#State of the program right berfore the function call: `t` is an integer representing the number of test cases, and for each test case, `n` and `m` are integers such that 1 ≤ n, m ≤ 2 * 10^6. The sum of n and the sum of m over all test cases do not exceed 2 * 10^6.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns a string containing the next line of input from the standard input buffer, stripped of any trailing whitespace.
#Overall this is what the function does:The function reads a line of input from the standard input buffer, strips any trailing whitespace, and returns it as a string. This process is performed for each test case specified by the variable `t`.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each of the next t lines contains two space-separated integers n and m such that 1 ≤ n, m ≤ 2 ⋅ 10^6 and the sum of n or m over all test cases does not exceed 2 ⋅ 10^6.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a line from the standard input buffer as a decoded string after stripping the trailing newline character.
#Overall this is what the function does:The function reads a line from the standard input buffer, removes any trailing newline character, decodes it from bytes to a string, and returns it.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers obtained by splitting the input string on spaces and converting each element to an integer.
#Overall this is what the function does:The function reads a single input string, splits it into elements based on spaces, converts each element to an integer, and returns a list of these integers.

#State of the program right berfore the function call: rows is a non-negative integer representing the number of test cases.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #The program returns a list containing the result of calling func_7() for each of the 'rows' test cases.
#Overall this is what the function does:The function accepts a non-negative integer `rows` representing the number of test cases. It generates a list containing the result of calling `func_7()` for each of these `rows` test cases and returns this list.

#State of the program right berfore the function call: This function does not take any parameters and it is expected to be part of a larger solution where the input is provided externally (e.g., through standard input or another function call). It returns a string containing the number of test cases 't'.
def func_9():
    return input()
    #The program returns a string containing the number of test cases 't', which is obtained from user input.
#Overall this is what the function does:The function does not accept any parameters and returns a string containing the number of test cases 't', which is obtained from user input.

#State of the program right berfore the function call: None of the variables in the function `func_10()` are described in the function signature or within the function itself. The function reads input but does not take any parameters.
def func_10():
    return int(input())
    #The program returns an integer input by the user.
#Overall this is what the function does:The function reads an integer input from the user and returns that integer.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6, and the sum of all n and the sum of all m do not exceed 2⋅10^6.
def func_11():
    return input().split()
    #The program returns a list of strings containing the values of `t`, `n`, and `m` for each test case, split from the input string.
#Overall this is what the function does:The function processes an input string containing multiple test cases, where each test case consists of three integers `t`, `n`, and `m` separated by spaces. It returns a list of strings, with each string containing the values of `t`, `n`, and `m` for each test case.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers; processing is a list of length equal to the maximum key in d, initialized with zeros; da is an integer which is a key in d; rank is a list of integers initialized with zeros.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: `d` is a dictionary where keys are integers and values are lists of integers; `processing` is a list of length equal to the maximum key in `d`, initialized with zeros; `da` is an integer which is a key in `d`; `rank` is a list of integers initialized with zeros; `tmp` is 1000000000; the length of `d[da]` is greater than 1
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: Output State: `d` is a dictionary where keys are integers and values are lists of integers; `processing` is a list of length equal to the maximum key in `d`, with each element set to 0 after the loop; `da` is an integer which is a key in `d`; `rank` is a list of integers initialized with zeros; `tmp` is 1000000000; for each `di` in `d[da]`, if `di - 1` was not previously processed (i.e., `processing[di - 1]` was 0), it is marked as processed (set to 1) during the loop, the minimum value of `tmp` is updated based on the function `func_12(d, processing, di, rank)`, and then `processing[di - 1]` is reset to 0 at the end of each iteration.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns 1000000001
#Overall this is what the function does:The function accepts a dictionary `d` where keys are integers and values are lists of integers, a list `processing` of the same length as the maximum key in `d` initialized with zeros, an integer `da` which is a key in `d`, and a list `rank` initialized with zeros. It recursively processes the elements in `d[da]` to find the minimum value of a certain condition, updating the `processing` and `rank` lists accordingly. If the length of `d[da]` is 1, it returns 1. Otherwise, it returns 1000000001.

#State of the program right berfore the function call: a and b are non-negative integers such that \(1 \leq a \leq n\), \(1 \leq b \leq m\), and \(b \neq 0\).
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns x which is 1, y which is 0, and a which is within the range of 1 to n.
    #State: a and b are non-negative integers such that \(1 \leq a \leq n\), \(1 \leq b \leq m\), and \(b \neq 0\)
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns y, x - a // b * y, and g, where y, x, and g are the return values from the function func_13(b, a % b)
#Overall this is what the function does:The function `func_13` accepts two non-negative integer parameters `a` and `b`, with specific constraints. Depending on the value of `b`, it either returns `x` as 1, `y` as 0, and `a` within the range of 1 to `n`, or it returns `y`, `x - a // b * y`, and `g`, where `y`, `x`, and `g` are the results from a recursive call to `func_13(b, a % b)`.

#State of the program right berfore the function call: a is a list of integers, n and m are non-negative integers such that 0 <= n, m <= 2 * 10^6, and k is an integer.
def func_14(a, n, m, k):
    for i in range(n):
        if a[i] < m:
            k -= m - a[i]
        
    #State: a is a list of integers where each element a[i] is at least m, and k is the original value minus the total amount by which elements in a were less than m.
    if (k >= 0) :
        return 1
        #The program returns 1
    #State: a is a list of integers where each element a[i] is at least m, and k is the original value minus the total amount by which elements in a were less than m, and k is less than 0
    return -1
    #The program returns -1
#Overall this is what the function does:The function accepts a list of integers `a`, two non-negative integers `n` and `m`, and an integer `k`. It iterates through the first `n` elements of `a` and adjusts `k` based on whether each element is less than `m`. If `k` is greater than or equal to zero after adjustments, the function returns 1; otherwise, it returns -1.

