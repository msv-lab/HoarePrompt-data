#State of the program right berfore the function call: None of the variables in the function `func_1()` are provided in the function signature. This function reads an integer from standard input (stdin) and returns it. Therefore, the precondition should describe the expected input from stdin rather than the function parameters.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program reads an integer from standard input (stdin) and returns it.
#Overall this is what the function does:The function reads an integer from standard input (stdin) and returns it.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object containing integers read from the standard input buffer, split by spaces.
#Overall this is what the function does:The function reads a line of input from the standard input buffer, splits it into individual integer values based on spaces, and returns a map object containing these integers.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of integers [n, m] read from the standard input, where n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
#Overall this is what the function does:The function reads two integers, n and m, from the standard input, ensuring that both values are within the range 1 ≤ n, m ≤ 2 ⋅ 10^6, and returns them as a list [n, m].

#State of the program right berfore the function call: rows_number is a non-negative integer representing the number of test cases. Each test case consists of two positive integers n and m such that 1 ≤ n, m ≤ 2 ⋅ 10^6 and the sum of all n and the sum of all m over all test cases does not exceed 2 ⋅ 10^6.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #The program returns a list of length `rows_number`, where each element is the result of calling `func_3()` for each test case. Each call to `func_3()` processes a pair of integers `n` and `m` as specified in the test case.
#Overall this is what the function does:The function accepts a non-negative integer `rows_number` representing the number of test cases. For each test case, it calls `func_3()` with a pair of integers `n` and `m`. It then returns a list of length `rows_number`, where each element is the result of the corresponding call to `func_3()`.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program reads a line from standard input, strips any trailing whitespace, and returns it as a string.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns it as a string.

#State of the program right berfore the function call: None of the variables in the function `func_6()` are documented within the provided code snippet. However, it is inferred that the function reads a single line from standard input, decodes it from bytes to a string, strips any trailing whitespace, and returns the result. This function does not take any parameters.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program reads a single line from standard input, decodes it from bytes to a string, strips any trailing whitespace, and returns the result.
#Overall this is what the function does:The function reads a single line from standard input, decodes it from bytes to a string, strips any trailing whitespace, and returns the result.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers obtained by splitting the input string on spaces and converting each element to an integer.
#Overall this is what the function does:The function reads a space-separated list of integers from standard input, converts each element into an integer, and returns this list.

#State of the program right berfore the function call: rows is a non-negative integer such that 0 <= rows.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #A list of length 'rows', where each element is the result of calling 'func_7()'
#Overall this is what the function does:The function accepts a non-negative integer `rows` and returns a list containing `rows` elements. Each element in the list is the result of calling the `func_7()` function.

#State of the program right berfore the function call: There is no input parameter for the function `func_9`, and it is expected to read input from the standard input stream according to the problem description.
def func_9():
    return input()
    #The program reads input from the standard input stream and returns it.
#Overall this is what the function does:The function `func_9` reads input from the standard input stream and returns it.

#State of the program right berfore the function call: None of the variables in the function `func_10` are defined or used within its body, and it does not take any parameters. This function simply reads an integer input from the standard input and returns it.
def func_10():
    return int(input())
    #The program reads an integer input from the standard input and returns it.
#Overall this is what the function does:The function reads an integer input from the standard input and returns it.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_11():
    return input().split()
    #The program returns a list of strings containing the values of `n` and `m` separated by spaces.
#Overall this is what the function does:The function reads input from the standard input, splits it into a list of two strings, and returns this list. The input consists of two space-separated integers `n` and `m`.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers; processing is a list of integers where each element is either 0 or 1 indicating whether the corresponding index has been processed; da is an integer representing the current node; rank is a list of integers representing the rank of each node.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: `tmp` is 1000000000, `d` is a dictionary where keys are integers and values are lists of integers, `processing` is a list of integers where each element is either 0 or 1 indicating whether the corresponding index has been processed, `da` is an integer representing the current node, `rank` is a list of integers representing the rank of each node, and the length of `d[da]` is not equal to 1
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: Output State: `tmp` is updated to the minimum value of `tmp` and the result of `func_12(d, processing, di, rank)` for each `di` in `d[da]` where `processing[di - 1]` is 0, `d` remains unchanged, `processing` is modified such that `processing[di - 1]` is set to 1 and then back to 0 for each `di` in `d[da]` where `processing[di - 1]` is 0, `da` remains unchanged, `rank` remains unchanged.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns the value of tmp incremented by 1.
#Overall this is what the function does:The function processes a dictionary `d` where keys are integers and values are lists of integers, a list `processing` indicating the processing status, an integer `da` representing the current node, and a list `rank` representing the rank of each node. It returns 1 if the length of `d[da]` is 1, otherwise, it updates `tmp` to the minimum value of `tmp` and the result of recursive calls to `func_12` for each unprocessed node connected to `da`, and finally returns `tmp + 1`.

#State of the program right berfore the function call: a and b are non-negative integers where b is non-zero (i.e., 0 < b \leq 2 \cdot 10^6), and a \leq 2 \cdot 10^6.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns x as 1, y as 0, and a as a non-negative integer.
    #State: a and b are non-negative integers where b is non-zero (i.e., 0 < b ≤ 2⋅10^6), and a ≤ 2⋅10^6, and b is not equal to 0
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns y, x - a // b * y, and g, where y, x, and g are the results of func_13(b, a % b)
#Overall this is what the function does:The function `func_13` accepts two parameters, `a` and `b`, which are non-negative integers with `b` being non-zero. Depending on the value of `b`, it either returns `x` as 1, `y` as 0, and `a` as a non-negative integer, or it recursively computes and returns values `y`, `x - a // b * y`, and `g`, where `y`, `x`, and `g` are the results of calling itself with `b` and `a % b`.

#State of the program right berfore the function call: a is a list of integers, n and m are positive integers such that 0 <= n, m <= 2 * 10^6, and k is an integer.
def func_14(a, n, m, k):
    for i in range(n):
        if a[i] < m:
            k -= m - a[i]
        
    #State: a is a list of integers where each element is at least m, and k is the original value minus the total amount by which elements in a were less than m.
    if (k >= 0) :
        return 1
        #The program returns 1
    #State: a is a list of integers where each element is at least m, and k is the original value minus the total amount by which elements in a were less than m, and k is less than 0
    return -1
    #The program returns -1
#Overall this is what the function does:The function accepts a list of integers `a`, two positive integers `n` and `m`, and an integer `k`. It iterates through the list `a` and adjusts the value of `k` based on whether each element is less than `m`. If `k` is non-negative after adjustments, the function returns 1; otherwise, it returns -1.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6 and the product of n and m does not exceed 2 * 10^6.
def func_15():
    n, m = func_7()
    i = 1
    ans = 0
    while i <= m and i * i <= n + i:
        ans += (n + i) // (i * i)
        
        i += 1
        
    #State: The value of `ans` is the sum of (n + i) // (i * i) for all integers i from 1 to the maximum value of i where i <= m and i * i <= n + i.
    return ans - 1
    #The program returns the sum of (n + i) // (i * i) for all integers i from 1 to the maximum value of i where i <= m and i * i <= n + i, minus 1.
#Overall this is what the function does:The function calculates the sum of \((n + i) // (i * i)\) for all integers \(i\) from 1 to the maximum value of \(i\) where \(i \leq m\) and \(i * i \leq n + i\), and then subtracts 1 from this sum.

#State of the program right berfore the function call: func_10 returns an integer representing the number of test cases (t), and for each test case, two integers n and m are provided such that 1 \leq n, m \leq 2 \cdot 10^6 and the sum of n or m over all test cases does not exceed 2 \cdot 10^6.
def func_16():
    for _ in range(func_10()):
        sys.stdout.write(str(func_15()) + '\n')
        
    #State: func_15() is called func_10() times, and each call's result is printed on a new line.
#Overall this is what the function does:The function prints the result of calling `func_15()` for each test case specified by `func_10()`. After completing all test cases, it does not return any value. Each result of `func_15()` is printed on a new line.

