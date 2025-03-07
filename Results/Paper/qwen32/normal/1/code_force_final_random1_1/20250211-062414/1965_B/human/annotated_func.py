#State of the program right berfore the function call: No variables are present in the function signature.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns an integer read from the standard input buffer.
#Overall this is what the function does:The function reads an integer from the standard input buffer and returns it.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object that applies the int function to each element of the list obtained by splitting the line read from sys.stdin.buffer.
#Overall this is what the function does:The function `func_2` reads a line from the standard input buffer, splits the line into elements, converts each element to an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: No variables are present in the function signature.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of integers that were read from standard input, split by whitespace.
#Overall this is what the function does:The function `func_3` reads a line of input from standard input, splits it into components based on whitespace, converts each component into an integer, and returns a list of these integers.

#State of the program right berfore the function call: rows_number is a positive integer representing the number of rows or test cases.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #The program returns a list containing the results of calling `func_3()` `rows_number` times.
#Overall this is what the function does:The function accepts a positive integer `rows_number` and returns a list containing the results of calling `func_3()` `rows_number` times.

#State of the program right berfore the function call: This function does not have any parameters. It reads a line from standard input and returns it as a byte string stripped of the trailing newline character.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns a byte string that is a line read from standard input, stripped of its trailing newline character.
#Overall this is what the function does:The function reads a line from standard input and returns it as a byte string with the trailing newline character removed.

#State of the program right berfore the function call: No variables are present in the function signature. Therefore, no precondition can be derived from the given function signature alone.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a string that is read from standard input, stripped of any trailing newline characters, and decoded from bytes to a string.
#Overall this is what the function does:The function `func_6` reads a line of input from standard input, removes any trailing newline characters, converts the byte string to a regular string, and returns the result.

#State of the program right berfore the function call: No variables are present in the function signature of `func_7`.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers, where each integer is derived from splitting the input string by spaces and converting each split substring into an integer.
#Overall this is what the function does:The function `func_7` reads a line of input from the user, splits it into substrings based on spaces, converts each substring into an integer, and returns a list of these integers.

#State of the program right berfore the function call: rows is a positive integer representing the number of test cases.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #The program returns a list containing the results of calling `func_7()` `rows` times. Each element in the list corresponds to the output of a single call to `func_7()`.
#Overall this is what the function does:The function `func_8` takes a positive integer `rows` as input and returns a list of length `rows`, where each element is the result of a separate call to the function `func_7`.

#State of the program right berfore the function call: This function does not have any parameters, and it returns the input which is expected to be a string representing the number of test cases followed by lines of test cases each containing two integers n and k.
def func_9():
    return input()
    #The program returns the input which is expected to be a string representing the number of test cases followed by lines of test cases each containing two integers n and k.
#Overall this is what the function does:The function `func_9` does not accept any parameters. It reads and returns a single string from the input, which is expected to represent the number of test cases followed by lines of test cases, where each line contains two integers, `n` and `k`.

#State of the program right berfore the function call: This function does not have any parameters, as it reads an integer input from the user. It returns an integer which represents the number of test cases (t), where 1 <= t <= 1000.
def func_10():
    return int(input())
    #The program returns an integer which represents the number of test cases (t), where 1 <= t <= 1000.
#Overall this is what the function does:The function reads an integer input from the user representing the number of test cases and returns this integer, ensuring that the value is between 1 and 1000 inclusive.

#State of the program right berfore the function call: No variables are present in the function signature.
def func_11():
    return input().split()
    #The program returns a list of substrings obtained by splitting the input string at each whitespace.
#Overall this is what the function does:The function `func_11` takes no input parameters and returns a list of substrings obtained by splitting the user-provided input string at each whitespace.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers, processing is a list of integers, da is an integer key present in d, and rank is a list of integers.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: `d` is a dictionary where keys are integers and values are lists of integers, `processing` is a list of integers, `da` is an integer key present in `d`, `rank` is a list of integers, `tmp` is `10`. The length of the list `d[da]` is greater than 1.
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: `d` is a dictionary where keys are integers and values are lists of integers, `processing` is a list of integers, `da` is an integer key present in `d`, `rank` is a list of integers, and `tmp` is the minimum value of `func_12(d, processing, di, rank)` for all `di` in `d[da]` where `processing[di - 1]` was `0`.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns `tmp + 1`, where `tmp` is the minimum value of `func_12(d, processing, di, rank)` for all `di` in `d[da]` where `processing[di - 1]` was `0`.
#Overall this is what the function does:The function `func_12` calculates a rank for a given key `da` in the dictionary `d` by recursively evaluating its connected nodes in `d` using the `processing` list to track visited nodes. It updates the `rank` list with the calculated rank for `da`. If the list associated with `da` contains only one element, it returns 1. Otherwise, it returns the minimum rank obtained from its connected nodes plus one.

#State of the program right berfore the function call: a and b are integers, where a >= 0 and b >= 0.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns (1, 0, a) where a is a non-negative integer
    #State: a and b are integers, where a >= 0 and b >= 0, and b is not equal to 0
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns `y`, `x - a // b * y`, and `g`, where `x`, `y`, and `g` are the values returned by `func_13(b, a % b)`
#Overall this is what the function does:The function `func_13` computes the coefficients of Bézout's identity for two non-negative integers `a` and `b`, returning a tuple `(x, y, g)` where `g` is the greatest common divisor of `a` and `b`, and `x` and `y` are integers satisfying the equation `ax + by = g`.

#State of the program right berfore the function call: n and k are integers such that 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n.
def func_14():
    n, k = func_7()
    b = bin(n)[2:]
    l = len(b)
    if (k == 1) :
        if (n == 2) :
            return '1\n2'
            #The program returns '1\n2'
        #State: `k` equals 1, `n` and `k` are integers such that `2 ≤ n ≤ 10^6` and `1 ≤ k ≤ n`; `b` is the binary representation of `n` without the '0b' prefix; `l` is the length of `b`. Additionally, `n` is not equal to 2
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
            
        #State: `n` and `k` are integers such that `2 ≤ n ≤ 10^6` and `3 ≤ k ≤ n`; `b` is the binary representation of `n` without the '0b' prefix; `l` is the length of `b`; `bk` is the binary representation of `k` without the '0b' prefix; `lk` is the length of `bk` and `lk` must be at least 2; `ans` is `[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]`; `i` is `lk - 2`.
        ans.append(k - 1 - sum(ans))
        ans.append(k + 1)
        ans.append(2 * k + 1)
        for i in range(lk, l):
            ans.append(2 ** i)
            
        #State: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, k - 524288, k + 1, 2 * k + 1, 2^lk, 2^(lk+1), ..., 2^(l-1)]
    #State: `n` and `k` are integers such that `2 ≤ n ≤ 10^6` and `1 ≤ k ≤ n`. `b` is the binary representation of `n` without the '0b' prefix; `l` is the length of `b`. If `k == 1`, then the program processes a specific list `[2, 3, 4, 8, 16]`. Otherwise, the program processes a different list `[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, k - 524288, k + 1, 2 * k + 1, 2^(lk), 2^(lk+1), ..., 2^(l-1)]`.
    return ' '.join(map(str, ans))
    #The program returns a space-separated string of the list `[2, 3, 4, 8, 16]` if `k == 1`. Otherwise, it returns a space-separated string of the list `[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, k - 524288, k + 1, 2 * k + 1, 2^(lk), 2^(lk+1), ..., 2^(l-1)]` where `l` is the length of the binary representation of `n`.
#Overall this is what the function does:The function generates and returns a space-separated string of integers based on the values of `n` and `k`. If `k` equals 1 and `n` equals 2, it returns '1\n2'. If `k` equals 1 and `n` is greater than 2, it returns a sequence starting with `[2, 3, 4, 8, 16]` followed by powers of 2 up to the length of the binary representation of `n`. For other values of `k`, it returns a sequence starting with `[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, k - 1 - sum_of_previous_elements, k + 1, 2 * k + 1]` followed by powers of 2 up to the length of the binary representation of `n`.

#State of the program right berfore the function call: This function does not have any parameters in its signature, so there are no variables to describe. However, it implies that it relies on other functions (`func_10` and `func_14`) which are not provided here. Based on the context, `func_10` likely returns the number of test cases, and `func_14` computes and returns the result for each test case.
def func_15():
    for _ in range(func_10()):
        sys.stdout.write(str(func_14()) + '\n')
        
    #State: The value returned by `func_14()` is written to the standard output as a string followed by a newline.
#Overall this is what the function does:The function `func_15` does not accept any parameters. It processes a number of test cases determined by `func_10`, computes the result for each test case using `func_14`, and writes each result to the standard output as a string followed by a newline.

