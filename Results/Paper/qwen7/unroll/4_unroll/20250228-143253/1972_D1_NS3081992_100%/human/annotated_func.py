#State of the program right berfore the function call: None of the variables in the function `func_1` are documented within the provided code snippet. However, based on the context, it is expected that `func_1` reads an integer input from standard input (stdin), which represents the number of test cases (`t`). The input is assumed to be in the form of integers, and the function returns this integer.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns an integer input read from standard input (stdin)
#Overall this is what the function does:The function `func_1` reads an integer input from standard input (stdin) and returns it. This integer represents the number of test cases to be processed.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6; the sum of n and the sum of m over all test cases do not exceed 2 ⋅ 10^6.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns two integers read from standard input, split and converted to integers.
#Overall this is what the function does:The function reads two integers from standard input, splits them, and converts them into integers before returning them.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of two integers, where the first integer is the value of 'n' and the second integer is the value of 'm' for each test case.
#Overall this is what the function does:The function reads a line of input from the standard buffer, splits it into integers, and returns a list containing two integers for each test case. The first integer in the list represents 'n', and the second integer represents 'm'.

#State of the program right berfore the function call: rows_number is a positive integer representing the number of test cases. Each test case consists of two positive integers n and m, where 1 ≤ n, m ≤ 2 \cdot 10^6 and the sum of n or m over all test cases does not exceed 2 \cdot 10^6.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #A list containing the results of calling func_3() for each of the 'rows_number' test cases.
#Overall this is what the function does:The function accepts a positive integer `rows_number` representing the number of test cases. For each test case, it calls `func_3()` with two positive integers `n` and `m` (where 1 ≤ n, m ≤ 2⋅10^6), and returns a list containing the results of these calls.

#State of the program right berfore the function call: None of the variables in the function signature are provided in the given code snippet. The function `func_5` reads input from standard input using `sys.stdin.buffer.readline().rstrip()` but does not take any parameters.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns a string read from standard input and stripped of trailing whitespace.
#Overall this is what the function does:The function reads a string from standard input, removes any trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a string read from standard input, stripped of trailing whitespace, and decoded from bytes to a string.
#Overall this is what the function does:The function reads a line of input from the standard input, removes any trailing whitespace, and decodes it from bytes to a string before returning it. This process ensures that the returned value is a clean string representation of the input received.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6, and the sum of n or m over all test cases does not exceed 2 ⋅ 10^6.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers parsed from the input. Each integer in the list corresponds to a value separated by spaces in the input string.
#Overall this is what the function does:The function reads a space-separated list of integers from the input and returns them as a list. The list contains integers that were originally separated by spaces in the input string.

#State of the program right berfore the function call: rows is a non-negative integer such that 0 <= rows.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #A list of length rows, where each element is the result of calling func_7()
#Overall this is what the function does:The function `func_8` accepts a non-negative integer `rows` and returns a list containing `rows` elements. Each element in the list is the result of calling the function `func_7()` once.

#State of the program right berfore the function call: This function does not take any parameters and it seems to be reading input from the user or another source, which is not defined in the context of the problem. However, based on the function signature, there are no variables to describe in terms of preconditions related to the problem's constraints.
def func_9():
    return input()
    #The program returns the input provided by the user.
#Overall this is what the function does:The function does not accept any parameters and returns the input provided by the user.

#State of the program right berfore the function call: There is no input parameter for the function. The function reads the number of test cases \( t \) from the standard input, where \( 1 \leq t \leq 10^4 \). Each test case consists of two space-separated integers \( n \) and \( m \), where \( 1 \leq n, m \leq 2 \cdot 10^6 \), and it is guaranteed that the sum of \( n \) and \( m \) over all test cases does not exceed \( 2 \cdot 10^6 \).
def func_10():
    return int(input())
    #The program reads an integer \( t \) from the standard input, where \( 1 \leq t \leq 10^4 \), and returns this integer.
#Overall this is what the function does:The function reads an integer \( t \) from the standard input, where \( 1 \leq t \leq 10^4 \), and returns this integer.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_11():
    return input().split()
    #The program returns a list of strings obtained from splitting the input string at whitespace boundaries.
#Overall this is what the function does:The function reads a single input string from the standard input, splits it into a list of substrings based on whitespace boundaries, and returns this list.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers; processing is a list of length equal to the maximum key in d, initialized with zeros; da is an integer which is a key in the dictionary d; rank is a list of integers initialized with zeros.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: Postcondition: `tmp` is 1000000000, `d` is a dictionary where keys are integers and values are lists of integers; `processing` is a list of length equal to the maximum key in `d`, initialized with zeros; `da` is an integer which is a key in the dictionary `d`; `rank` is a list of integers initialized with zeros. Additionally, the length of `d[da]` is not equal to 1.
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: `tmp` is the minimum value obtained from `func_12(d, processing, di, rank)` for each `di` in `d[da]` such that `processing[di - 1]` was initially 0, `d` remains unchanged, `processing` is reset to its original state (all zeros), `da` remains unchanged, and `rank` remains unchanged.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns the minimum value obtained from `func_12(d, processing, di, rank)` for each `di` in `d[da]` such that `processing[di - 1]` was initially 0, plus 1.
#Overall this is what the function does:The function accepts a dictionary `d` where keys are integers and values are lists of integers, a list `processing` of length equal to the maximum key in `d`, initialized with zeros, an integer `da` which is a key in the dictionary `d`, and a list `rank` initialized with zeros. It returns 1 if no valid `di` from `d[da]` where `processing[di - 1]` was initially 0 exists. Otherwise, it returns the minimum value obtained from `func_12(d, processing, di, rank)` for each `di` in `d[da]` such that `processing[di - 1]` was initially 0, plus 1.

#State of the program right berfore the function call: a and b are non-negative integers such that 1 <= a <= n, 1 <= b <= m, and b != 0.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns x which is 1, y which is 0, and a which is a non-negative integer such that 1 <= a <= n
    #State: a and b are non-negative integers such that 1 <= a <= n, 1 <= b <= m, and b is not equal to 0
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns y, x - a // b * y, g
#Overall this is what the function does:The function `func_13` accepts two parameters, `a` and `b`, both non-negative integers such that \(1 \leq a \leq n\) and \(1 \leq b \leq m\), and \(b \neq 0\). It returns either (1, 0, `a`) or (`y`, `x - a // b * y`, `g`), where `g` is the greatest common divisor (GCD) of `a` and `b`. In the first case, it directly returns 1, 0, and `a`. In the second case, it recursively calculates the GCD using the Euclidean algorithm and returns the coefficients `y` and `x - a // b * y`, along with the GCD `g`.

#State of the program right berfore the function call: a is a list of integers, n and m are non-negative integers, and k is an integer.
def func_14(a, n, m, k):
    for i in range(n):
        if a[i] < m:
            k -= m - a[i]
        
    #State: Output State: k is reduced by the sum of (m - a[i]) for all i in the range of n where a[i] is less than m.
    if (k >= 0) :
        return 1
        #The program returns 1
    #State: k is reduced by the sum of (m - a[i]) for all i in the range of n where a[i] is less than m, and k is less than 0
    return -1
    #The program returns -1
#Overall this is what the function does:The function accepts a list of integers `a`, two non-negative integers `n` and `m`, and an integer `k`. It iterates through the first `n` elements of `a`, reducing `k` by the difference between `m` and each element of `a` that is less than `m`. If `k` remains non-negative after this process, the function returns 1; otherwise, it returns -1.

