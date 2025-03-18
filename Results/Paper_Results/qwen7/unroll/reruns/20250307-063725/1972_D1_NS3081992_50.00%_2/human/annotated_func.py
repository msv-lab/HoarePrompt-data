#State of the program right berfore the function call: None of the variables in the provided function contribute to solving the problem directly. The function `func_1()` reads an integer from standard input and returns it. However, based on the problem description, there should be a function that processes the test cases and calculates the number of valid pairs (a, b) as described. The precondition should describe the expected input and output for such a function, not for `func_1()`.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program reads an integer from standard input and returns it.
#Overall this is what the function does:Functionality: The function accepts no parameters and reads an integer from standard input, then returns it.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object containing integers read from the standard input buffer, split by spaces.
#Overall this is what the function does:The function reads a line of input from the standard input buffer, splits it into individual integer values based on spaces, and returns a map object containing these integers.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6. The values of n and m are provided in the input in such a way that the sum of n or m over all test cases does not exceed 2⋅10^6.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of two integers, n and m, read from the standard input.
#Overall this is what the function does:The function reads two integers, n and m, from the standard input where 1 ≤ n, m ≤ 2⋅10^6, and returns them as a list.

#State of the program right berfore the function call: rows_number is a positive integer representing the number of test cases. Each test case consists of two positive integers n and m such that 1 ≤ n, m ≤ 2 ⋅ 10^6 and the sum of all n and m over all test cases does not exceed 2 ⋅ 10^6.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #A list containing the results of calling `func_3()` for each of the `rows_number` test cases.
#Overall this is what the function does:The function accepts a positive integer `rows_number` representing the number of test cases. For each test case, it calls `func_3()` with two positive integers `n` and `m` (where 1 ≤ n, m ≤ 2⋅10^6). After processing all test cases, it returns a list containing the results of these calls.

#State of the program right berfore the function call: None of the variables in the function `func_5()` are defined in its signature. This function reads a line from standard input, strips the trailing newline character, and returns it. However, since no input parameters are specified, we cannot describe any preconditions related to the input variables.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program reads a line from standard input, removes the trailing newline character, and returns it.
#Overall this is what the function does:The function reads a line from standard input, removes the trailing newline character, and returns the modified line.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a string read from standard input, stripped of trailing whitespace, and decoded from bytes to a string.
#Overall this is what the function does:The function reads a line of input from standard input, removes any trailing whitespace, and decodes it from bytes to a string before returning it. This function does not accept any parameters and always returns a string.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2⋅10^6.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers obtained by splitting the input string on spaces and converting each element to an integer.
#Overall this is what the function does:The function reads a space-separated string of integers from the standard input, converts each integer in the string to its numeric form, and returns a list of these integers.

#State of the program right berfore the function call: rows is a non-negative integer representing the number of test cases.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #A list containing the results of calling func_7() for each of the 'rows' test cases.
#Overall this is what the function does:The function accepts a non-negative integer `rows` representing the number of test cases. It returns a list containing the results of calling `func_7()` for each of the `rows` test cases.

#State of the program right berfore the function call: This function does not take any parameters and it seems to be reading input from the user or another source, which is not defined in the context of the problem. However, based on the function signature, there are no variables to describe in terms of preconditions related to the problem.
def func_9():
    return input()
    #The program returns the input provided by the user
#Overall this is what the function does:The function `func_9` does not accept any parameters and returns the input provided by the user.

#State of the program right berfore the function call: None of the variables in the function `func_10()` are documented in the provided code snippet. The function simply reads an integer input and returns it. However, based on the context, we can infer that the function is part of a larger program that processes multiple test cases, where each test case involves two integers n and m. Therefore, the input to `func_10()` is the number of test cases, t.
def func_10():
    return int(input())
    #The program returns the number of test cases, t, which is an integer input from the user.
#Overall this is what the function does:The function `func_10()` reads an integer input from the user and returns it as the number of test cases, `t`. This value represents the total number of test cases that will be processed in the subsequent part of the program.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6, and the sum of n or m over all test cases does not exceed 2 ⋅ 10^6.
def func_11():
    return input().split()
    #The program returns a list of strings containing the values of `n` and `m` for each test case as split from user input.
#Overall this is what the function does:The function reads user input, splits it into a list of strings, where each string contains the values of `n` and `m` for each test case, and returns this list.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers; processing is a list of zeros and ones with the same length as the number of keys in d; da is an integer representing a key in d; rank is a list of zeros with the same length as the number of keys in d.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: Postcondition: `tmp` is 1000000000, `d` is a dictionary where keys are integers and values are lists of integers, `processing` is a list of zeros and ones with the same length as the number of keys in `d`, `da` is an integer representing a key in `d`, `rank` is a list of zeros with the same length as the number of keys in `d`. The length of `d[da]` is not equal to 1.
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: `tmp` is the minimum value obtained from `func_12(d, processing, di, rank)` for each `di` in `d[da]` where `processing[di - 1]` was initially 0, `d` remains unchanged, `processing` is modified such that for each `di` in `d[da]` where `processing[di - 1]` was initially 0, it is set to 1 and then back to 0, `da` remains unchanged, `rank` remains unchanged.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns the value of `rank[da - 1]` which is `tmp + 1`
#Overall this is what the function does:The function accepts a dictionary `d` where keys are integers and values are lists of integers, a list `processing` of zeros and ones with the same length as the number of keys in `d`, an integer `da` representing a key in `d`, and a list `rank` of zeros with the same length as the number of keys in `d`. It returns 1 if the length of `d[da]` is 1, otherwise it recursively processes each element in `d[da]` where `processing` is temporarily set to 1, updates `rank[da - 1]` to the minimum value found plus one, and returns this updated value.

#State of the program right berfore the function call: a and b are positive integers such that 1 <= a, b <= 2 * 10^6 and b != 0.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns x which is 1, y which is 0, and a which is a positive integer.
    #State: a and b are positive integers such that 1 <= a, b <= 2 * 10^6 and b != 0
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns y, x - a // b * y, and g, where y, x, and g are the results of the function call func_13(b, a % b)
#Overall this is what the function does:The function `func_13` accepts two positive integers `a` and `b` (1 ≤ a, b ≤ 2 * 10^6 and b ≠ 0). It returns either (1, 0, a) if `b` is 0, or (y, x - a // b * y, g) where y, x, and g are the results of recursively calling `func_13(b, a % b)`. The function essentially computes the extended greatest common divisor (GCD) of `a` and `b`, returning the GCD along with the coefficients `x` and `y` such that ax + by = g.

#State of the program right berfore the function call: a is a list of integers, n and m are non-negative integers such that 0 <= n, m <= 2 * 10^6, and k is an integer representing a certain threshold value.
def func_14(a, n, m, k):
    for i in range(n):
        if a[i] < m:
            k -= m - a[i]
        
    #State: Output State: a is a list of integers where each element a[i] is at least m, and k is the initial value minus the sum of differences (m - a[i]) for all i in the range of n where a[i] was less than m initially.
    if (k >= 0) :
        return 1
        #The program returns 1
    #State: a is a list of integers where each element a[i] is at least m, and k is the initial value minus the sum of differences (m - a[i]) for all i in the range of n where a[i] is greater than or equal to m initially.
    return -1
    #The program returns -1
#Overall this is what the function does:The function accepts a list of integers `a`, two non-negative integers `n` and `m`, and an integer `k`. It iterates through the first `n` elements of `a` and adjusts `k` based on whether each element is less than `m`. If `k` remains non-negative after adjustments, the function returns 1; otherwise, it returns -1.

#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 2⋅10^6.
def func_15():
    n, m = func_7()
    i = 1
    ans = 0
    while i * i <= n + i:
        ans += (n + i) // (i * i)
        
        i += 1
        
    #State: The value of ans is 0.
    return ans - 1
    #The program returns -1
#Overall this is what the function does:The function accepts no parameters and calculates a value based on the initial values of `n` and `m` obtained from another function, then returns -1. Specifically, it initializes `ans` to 0, iterates through a loop where it updates `ans` by adding `(n + i) // (i * i)` for each `i` starting from 1 until `i * i` exceeds `n + i`, and finally returns `ans - 1`.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6, and the sum of n or m over all test cases does not exceed 2 ⋅ 10^6.
def func_16():
    for _ in range(func_10()):
        sys.stdout.write(str(func_15()) + '\n')
        
    #State: t test cases are printed, each containing a single integer generated by func_15().
#Overall this is what the function does:The function processes a series of test cases, printing one integer per test case. Each test case involves calling `func_15()` which generates an integer value, and this value is written to the standard output followed by a newline. The function does not accept any parameters and does not return any value.

