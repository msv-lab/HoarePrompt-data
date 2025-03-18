#State of the program right berfore the function call: No variables are present in the function signature.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns an integer read from the standard input.
#Overall this is what the function does:The function `func_1` reads an integer from the standard input and returns it.

#State of the program right berfore the function call: No variables in the function signature. The function `func_2` reads input from standard input and returns a map object containing integers split from a single line of input.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object containing integers split from a single line of input.
#Overall this is what the function does:The function `func_2` reads a single line of input from standard input, splits the line into substrings based on whitespace, converts each substring into an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: No variables in the function signature. The function `func_3` reads input from standard input and returns a list of integers, but its signature does not include any parameters.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of integers that were read from the standard input, split by whitespace.
#Overall this is what the function does:The function reads a line of input from the standard input, splits it by whitespace, converts each split component into an integer, and returns a list of these integers.

#State of the program right berfore the function call: rows_number is a positive integer representing the number of rows or test cases.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #The program returns a list containing the results of calling `func_3()` `rows_number` times. Each element in the list corresponds to the output of one call to `func_3()`.
#Overall this is what the function does:The function takes a positive integer `rows_number` as input and returns a list containing the results of calling `func_3()` `rows_number` times. Each element in the list is the output of one call to `func_3()`.

#State of the program right berfore the function call: No variables are present in the function signature.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns a string that is the line read from standard input, excluding any trailing newline character.
#Overall this is what the function does:The function reads a line from the standard input, removes any trailing newline character, and returns the resulting string.

#State of the program right berfore the function call: No variables are present in the function signature of `func_6`. This function does not take any parameters and its purpose is to read a line from standard input, strip any trailing newline characters, and decode it from bytes to a string.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a string that is the line read from standard input, with any trailing newline characters removed and decoded from bytes to a string.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing newline characters, decodes it from bytes to a string, and returns the resulting string.

#State of the program right berfore the function call: No variables are present in the function signature. The function `func_7` does not take any parameters and returns a list of integers obtained from the input.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers obtained from the input, where each integer is derived from splitting the input string by spaces and converting each split substring into an integer.
#Overall this is what the function does:The function `func_7` takes no input parameters and returns a list of integers. This list is created by reading a line of input, splitting it by spaces, and converting each resulting substring into an integer.

#State of the program right berfore the function call: rows is a positive integer representing the number of test cases.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #The program returns a list containing the results of calling `func_7()` `rows` times. Each element in the list corresponds to the return value of one call to `func_7()`.
#Overall this is what the function does:The function `func_8` takes a positive integer `rows` as input and returns a list containing the results of calling `func_7()` `rows` times. Each element in the returned list corresponds to the return value of one call to `func_7()`.

#State of the program right berfore the function call: This function does not have any parameters. It reads input from standard input.
def func_9():
    return input()
    #The program returns the input read from standard input.
#Overall this is what the function does:The function `func_9` reads a line of input from the standard input and returns it.

#State of the program right berfore the function call: No variables in the function signature.
def func_10():
    return int(input())
    #The program returns an integer value that is input by the user.
#Overall this is what the function does:The function does not accept any parameters and returns an integer value that is input by the user.

#State of the program right berfore the function call: No variables in the function signature. The function `func_11` does not take any parameters and thus has no preconditions related to its arguments.
def func_11():
    return input().split()
    #The program returns a list of strings, where each string is a word from the input provided by the user.
#Overall this is what the function does:The function `func_11` prompts the user for input, splits the input into words, and returns a list of these words.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers, processing is a list of integers, da is an integer, and rank is a list of integers.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: `d` is a dictionary where keys are integers and values are lists of integers, `processing` is a list of integers, `da` is an integer, `rank` is a list of integers, `tmp` is 1000000000, and the length of the list `d[da]` is greater than 1
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: `d` is a dictionary where `d[da]` is a list of integers, `processing` is a list of integers with all elements reset to 0, `da` is an integer, `rank` is a list of integers, and `tmp` is the minimum of 1000000000 and the values returned by `func_12(d, processing, di, rank)` for each `di` in `d[da]` where `processing[di - 1]` was 0.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns `tmp + 1`, where `tmp` is the minimum of 1000000000 and the values returned by `func_12(d, processing, di, rank)` for each `di` in `d[da]` where `processing[di - 1]` was 0.
#Overall this is what the function does:The function `func_12` takes a dictionary `d`, a list `processing`, an integer `da`, and a list `rank`. It recursively calculates a value based on the structure of `d` and the state of `processing`. If the list `d[da]` contains only one element, it returns 1. Otherwise, it explores each element in `d[da]` that has not been processed, updates the `processing` list, and computes the minimum value from recursive calls. This minimum value, incremented by 1, is then assigned to `rank[da - 1]` and returned.

#State of the program right berfore the function call: a and b are integers, where a >= 0 and b >= 0.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns the tuple (1, 0, a), where a is a non-negative integer.
    #State: a and b are integers, where a >= 0 and b >= 0, and b is not equal to 0
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns `y`, `x - a // b * y`, and `g`, where `g` is the GCD of `b` and `a % b`, and `x` and `y` are Bézout coefficients satisfying the equation `bx + (a % b)y = g`.
#Overall this is what the function does:The function `func_13` computes the greatest common divisor (GCD) of two non-negative integers `a` and `b`, and also finds Bézout coefficients `x` and `y` such that `ax + by = GCD(a, b)`. It returns a tuple containing these coefficients and the GCD. If `b` is 0, it returns `(1, 0, a)`.

#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n.
def func_14():
    n, k = func_7()
    b = bin(n)[2:]
    l = len(b)
    if (k == 1) :
        if (n == 2) :
            return '1\n2'
            #The program returns '1\n2'
        #State: `k` equals 1, `n` and `k` are integers such that 2 <= n <= 10^6 and 1 <= k <= n; `b` is the binary string representation of `n`; `l` is the length of `b`. Additionally, `n` is not equal to 2
        ans = [2, 3]
        for i in range(2, l):
            ans.append(2 ** i)
            
        #State: [2, 3, 4, 8, 16]
    else :
        bk = bin(k)[2:]
        ans = []
        lk = len(bk)
        for i in range(lk - 1):
            ans.append(2 ** i)
            
        #State: `n` and `k` are integers such that \(2 \leq n \leq 10^6\) and \(1 < k \leq n\); `b` is the binary string representation of `n`; `l` is the length of `b`; `bk` is the binary string representation of `k`; `ans` is a list containing `[2, 8, 16, 32]`; `lk` is 5.
        ans.append(k - 1 - sum(ans))
        ans.append(k + 1)
        ans.append(2 * k + 1)
        for i in range(lk, l):
            ans.append(2 ** i)
            
        #State: [2, 8, 16, 32, -49, 11, 21, 2, 32, 64]
    #State: `n` and `k` are integers such that 2 <= n <= 10^6 and 1 <= k <= n; `b` is the binary string representation of `n`; `l` is the length of `b`. If `k` equals 1, the list is set to [2, 3, 4, 8, 16]. Otherwise, the list is set to [2, 8, 16, 32, -49, 11, 21, 2, 32, 64].
    return ' '.join(map(str, ans))
    #The program returns either '2 3 4 8 16' if k equals 1, or '2 8 16 32 -49 11 21 2 32 64' if k does not equal 1.
#Overall this is what the function does:The function accepts two integer parameters `n` and `k` where `2 <= n <= 10^6` and `1 <= k <= n`. It returns '1\n2' if `n` equals 2 and `k` equals 1. Otherwise, it returns a space-separated string of integers. If `k` equals 1, the returned string is '2 3 4 8 16'. If `k` does not equal 1, the returned string is a sequence of integers that depends on the values of `n` and `k`.

#State of the program right berfore the function call: This function does not have any parameters in its signature. It relies on other functions (`func_10` and `func_14`) which are not defined in the provided code snippet. However, based on the usage, `func_10()` likely returns the number of test cases (t), and `func_14()` likely processes each test case to determine the required sequence and its size.
def func_15():
    for _ in range(func_10()):
        sys.stdout.write(str(func_14()) + '\n')
        
    #State: The output consists of `num_iterations` lines, where each line contains the string representation of the value returned by `func_14()` during that iteration.
    #
    #If we assume `num_iterations` is 3 based on the given examples, the output would look like this:
    #```
    #result1
    #result2
    #result3
    #```
    #
    #However, without knowing the exact number of iterations and the specific results from `func_14()`, we can only describe the output state in a generalized form.
    #
    #Therefore, the final output state in the required format is:
    #
    #Output State:
#Overall this is what the function does:The function `func_15` does not accept any parameters. It determines the number of test cases using `func_10()` and processes each test case using `func_14()`. For each test case, it outputs the result returned by `func_14()` on a new line.

