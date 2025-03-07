#State of the program right berfore the function call: None of the variables in the function signature are provided in the given code snippet. The function `func_1` does not take any arguments.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program reads an integer from standard input (sys.stdin) and returns it.
#Overall this is what the function does:The function `func_1` reads an integer from standard input and returns it.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, n and k are integers satisfying 2 <= n <= 10^6 and 1 <= k <= n.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object containing integers read from the standard input buffer, split by spaces.
#Overall this is what the function does:The function reads integers from the standard input buffer, splits them by spaces, and returns a map object containing these integers.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, n and k are integers satisfying 2 <= n <= 10^6 and 1 <= k <= n.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of two integers, read from standard input, split and converted to integers.
#Overall this is what the function does:Functionality: The function reads two integers from standard input, splits them based on whitespace, converts them to integers, and returns them as a list.

#State of the program right berfore the function call: rows_number is a positive integer such that 1 <= rows_number <= 25.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #A list containing the result of func_3() called `rows_number` times
#Overall this is what the function does:The function accepts a positive integer `rows_number` (between 1 and 25) and returns a list containing the results of calling `func_3()` exactly `rows_number` times.

#State of the program right berfore the function call: None of the variables in the provided function signature are used within the function, and the function returns a value read from standard input. However, based on the problem description, the function should take no arguments since the input is read from standard input.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program reads a line from standard input, removes any trailing whitespace, and returns it.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and returns the modified line.

#State of the program right berfore the function call: None of the variables in the function signature are provided in the given code snippet. The function does not take any parameters.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a decoded string that was read from standard input, stripped of trailing whitespace.
#Overall this is what the function does:The function reads a line of text from standard input, strips any trailing whitespace, decodes it from bytes to a string, and returns the resulting string.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers obtained by splitting the input string and converting each element to an integer.
#Overall this is what the function does:The function reads a single input string from the user, splits the string into individual elements, converts each element to an integer, and returns a list of these integers. This process applies to any valid input string provided by the user.

#State of the program right berfore the function call: rows is a positive integer such that 1 <= rows <= 25.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #A list of length rows, where each element is the result of calling func_7()
#Overall this is what the function does:The function `func_8` accepts a positive integer `rows` (between 1 and 25) and returns a list of length `rows`. Each element in the list is the result of calling another function `func_7()` one time for each element in the list.

#State of the program right berfore the function call: None of the variables in the function signature are used within the function. The function does not take any arguments and returns the result of `input()` which is expected to be provided by the user or the calling context.
def func_9():
    return input()
    #The program waits for user input and returns the value provided by the user.
#Overall this is what the function does:The function accepts no parameters and waits for user input, returning the value provided by the user.

#State of the program right berfore the function call: None of the variables in the function signature are used within the function, and the function returns an integer read from input which represents the number of test cases (t).
def func_10():
    return int(input())
    #The program returns an integer entered by the user, representing the number of test cases.
#Overall this is what the function does:The function accepts no parameters and reads an integer value from user input, representing the number of test cases. This integer value is then returned to the caller.

#State of the program right berfore the function call: None of the variables in the function signature are provided in the code snippet. The function `func_11()` does not take any parameters.
def func_11():
    return input().split()
    #The program returns a list of strings obtained by splitting the input received from the user.
#Overall this is what the function does:The function `func_11()` does not accept any parameters and returns a list of strings obtained by splitting a string input received from the user.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers. da is an integer key present in the dictionary d. processing is a list of the same length as the maximum possible value in the lists within d, initialized with zeros. rank is a list of the same length as the keys in d, initialized with zeros.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: `d` is a dictionary where keys are integers and values are lists of integers; `da` is an integer key present in the dictionary `d`; `processing` is a list of the same length as the maximum possible value in the lists within `d`, initialized with zeros; `rank` is a list of the same length as the keys in `d`, initialized with zeros; `tmp` is 1000000000. The length of `d[da]` is not equal to 1
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: Output State: `d` is a dictionary where keys are integers and values are lists of integers; `da` is an integer key present in the dictionary `d`; `processing` is a list of the same length as the maximum possible value in the lists within `d`, updated such that `processing[di - 1]` is set to 0 for every `di` in `d[da]`; `rank` is a list of the same length as the keys in `d`, initialized with zeros; `tmp` is the minimum value obtained from `func_12(d, processing, di, rank)` for each `di` in `d[da]` during the loop iterations.
    #
    #In simpler terms, after all iterations of the loop, the `processing` list will have all its indices corresponding to elements in `d[da]` set to 0. The `tmp` variable will hold the smallest value returned by `func_12(d, processing, di, rank)` for any `di` in `d[da]` during the loop's execution. The `rank` list and the initial state of `d` and `da` remain unchanged.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns the rank of key `da` in dictionary `d` which is calculated as `tmp + 1`. Here, `tmp` is the minimum value obtained from `func_12(d, processing, di, rank)` for each `di` in `d[da]` during the loop iterations.
#Overall this is what the function does:The function accepts a dictionary `d` where keys are integers and values are lists of integers, a list `processing` of the same length as the maximum possible value in the lists within `d`, initialized with zeros, an integer key `da` present in the dictionary `d`, and a list `rank` of the same length as the keys in `d`, initialized with zeros. If the length of `d[da]` is 1, the function returns 1. Otherwise, it recursively processes each element in `d[da]` using `func_12`, updating the `processing` list and tracking the minimum value (`tmp`). Finally, it sets the rank of `da` in `d` to `tmp + 1` and returns this rank.

#State of the program right berfore the function call: a and b are non-negative integers such that b != 0.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns x as 1, y as 0, and a as a non-negative integer.
    #State: a and b are non-negative integers such that b is not equal to 0
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns y which is b, x - a // b * y, and g which is the result of func_13(b, a % b)
#Overall this is what the function does:The function accepts two non-negative integers, `a` and `b`, where `b` is not zero. It returns three values: `x`, `y`, and `g`. If `b` is zero, it returns `x` as 1, `y` as 0, and `a` as the original value. Otherwise, it recursively calculates `x`, `y`, and `g` using the Extended Euclidean Algorithm, returning `y`, `x - a // b * y`, and `g` respectively.

#State of the program right berfore the function call: n and k are integers such that 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n.
def func_14():
    n, k = func_7()
    b = bin(n)[2:]
    l = len(b)
    if (k == 1) :
        if (n == 2) :
            return '1\n2'
            #The program returns the string '1\n2'
        #State: `b` is the binary representation of `n` without the '0b' prefix, `k` is the integer returned from `func_7()` and equals 1, `l` is the length of `b`, and `n` is not equal to 2
        ans = [2, 3]
        for i in range(2, l):
            ans.append(2 ** i)
            
        #State: Output State: `i` is equal to `l`; `l` is the length of `b` and must be greater than or equal to 3; `ans` is [4, 8, 16, ..., 2 ** l]
        #
        #Explanation: The loop runs from `i = 2` to `i = l-1`. Given that the loop executed 3 times, `i` reached 4, meaning `l` must be at least 5 (since the loop starts at 2 and increments by 1 each time). Therefore, `i` will eventually equal `l`, and `ans` will contain all values from `2^2` to `2^l` in steps of 2.
    else :
        bk = bin(k)[2:]
        ans = []
        lk = len(bk)
        for i in range(lk - 1):
            ans.append(2 ** i)
            
        #State: Output State: `i` is equal to `lk - 2`; `lk` must be greater than 3; `ans` is a list containing the values `[1, 2, 4, ..., 2^(lk-2)]`.
        #
        #In natural language: After the loop has executed all its iterations, the variable `i` will be equal to `lk - 2`, meaning the loop has completed `lk - 2` iterations. The variable `lk` must be greater than 3 for the loop to run at least three times. The list `ans` will contain a sequence of powers of 2 starting from \(2^0\) up to \(2^{lk-2}\).
        ans.append(k - 1 - sum(ans))
        ans.append(k + 1)
        ans.append(2 * k + 1)
        for i in range(lk, l):
            ans.append(2 ** i)
            
        #State: Output State: `i` is `lk - 1`, `ans` contains `[2, 2, 4, 8, ..., 2^(lk-2), k + 1, 2 * k + 1, 2^lk]`.
        #
        #To understand this, let's break it down:
        #
        #1. **Initial State**: 
        #   - `i` starts as `lk - 2`.
        #   - `lk` is greater than 3.
        #   - `ans` is initially `[1, 2, 4, ..., 2^(lk-2), k + 1, 2 * k + 1, (k - 1 - sum(ans))]`.
        #
        #2. **Loop Execution**:
        #   - The loop runs from `i = lk - 2` to `i = lk - 1` (inclusive).
        #   - In each iteration, `ans.append(2 ** i)` is executed.
        #
        #3. **After First Iteration**:
        #   - `i` becomes `lk - 1`.
        #   - `ans` becomes `[2]`.
        #
        #4. **After Second Iteration**:
        #   - `i` becomes `lk`.
        #   - `ans` becomes `[2, 2]`.
        #
        #5. **After Third Iteration**:
        #   - `i` becomes `lk + 1` (but since the loop condition stops at `i < l`, it effectively stops at `i = lk`).
        #   - `ans` becomes `[2, 2, 4]`.
        #
        #6. **Final State After All Iterations**:
        #   - `i` will be `lk - 1` because the loop condition `i < l` will stop the loop just before `i` reaches `l`.
        #   - `ans` will contain all the powers of 2 from `2^(lk-2)` to `2^lk` plus the initial elements `[k + 1, 2 * k + 1, (k - 1 - sum(ans))]`.
        #
        #So, the final state of `ans` will include all the powers of 2 from `2^(lk-2)` to `2^lk` followed by the initial elements `[k + 1, 2 * k + 1, (k - 1 - sum(ans))]` and then `2^lk`.
    #State: `i` is `l` if `k` is 1, otherwise `i` is `lk - 1`. `ans` contains all the powers of 2 from `2^(l-2)` to `2^l` followed by the initial elements `[k + 1, 2 * k + 1, (k - 1 - sum(ans))]` and then `2^l` if `k` is not 1.
    return ' '.join(map(str, ans))
    #The program returns a string containing space-separated integers. These integers include all the powers of 2 from \(2^{l-2}\) to \(2^l\), followed by the initial elements \([k + 1, 2 * k + 1, (k - 1 - \text{sum}(ans))]\), and then \(2^l\) if \(k\) is not 1.
#Overall this is what the function does:The function takes no explicit parameters but relies on values obtained from `func_7()`. It returns either the string '1\n2' or a string containing space-separated integers. If `k` is 1, it returns '1\n2'. Otherwise, it constructs a list `ans` containing all powers of 2 from \(2^{l-2}\) to \(2^l\), along with additional elements based on `k` and the sum of `ans`. Finally, it returns a string of these integers separated by spaces.

#State of the program right berfore the function call: None of the variables (t, _, n, k) are defined within the function, implying they are passed as arguments when the function is called elsewhere. Additionally, it is assumed that t is an integer representing the number of test cases, and each test case consists of two integers n and k as described in the problem statement.
def func_15():
    for _ in range(func_10()):
        sys.stdout.write(str(func_14()) + '\n')
        
    #State: The output state after the loop executes all its iterations will include `sys.stdout.write` calling `func_14()` and printing a newline character for each iteration of the loop. Since `func_10()` returns a value of at least 0, the loop will execute for as many times as the value returned by `func_10()`. Each call to `func_14()` during these iterations will produce some output which is then printed to the standard output followed by a newline.
#Overall this is what the function does:The function processes a specified number of test cases (determined by the value of `t`). For each test case, it calls `func_14()` multiple times (the exact number determined by `func_10()`) and prints the result of each call to `func_14()` followed by a newline character. The final state of the program is that the standard output contains the results of these function calls, each on a new line.

