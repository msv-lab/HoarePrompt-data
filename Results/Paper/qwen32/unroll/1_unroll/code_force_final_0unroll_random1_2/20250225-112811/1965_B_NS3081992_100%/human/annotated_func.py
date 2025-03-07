#State of the program right berfore the function call: No variables are present in the function signature.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns an integer value read from the standard input.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns an integer value read from the standard input.

#State of the program right berfore the function call: No variables are present in the function signature, thus no specific precondition can be derived from it.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object that applies the `int` function to each element of the list created by splitting the input line read from `sys.stdin.buffer`. This input line is expected to contain space-separated integers.
#Overall this is what the function does:The function `func_2` reads a line from the standard input, splits it into space-separated parts, converts each part to an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: No variables are present in the function signature of `func_3`.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of integers that were read from the standard input, split by whitespace.
#Overall this is what the function does:The function `func_3` reads a line of input from the standard input, splits it by whitespace, converts each split component into an integer, and returns the resulting list of integers.

#State of the program right berfore the function call: rows_number is a positive integer representing the number of test cases.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #The program returns a list of length `rows_number` where each element is the result of calling `func_3()`
#Overall this is what the function does:The function accepts a positive integer `rows_number` and returns a list of length `rows_number`, where each element is the result of calling `func_3()`.

#State of the program right berfore the function call: No variables are present in the function signature.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns a string that is the line read from standard input, with any trailing newline characters removed.
#Overall this is what the function does:The function `func_5` reads a line from the standard input, removes any trailing newline characters, and returns the resulting string.

#State of the program right berfore the function call: This function does not have any parameters. It reads a line from the standard input, removes any trailing whitespace, and decodes it from bytes to a string.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a string that is a line read from the standard input, with any trailing whitespace removed.
#Overall this is what the function does:The function reads a line from the standard input, removes any trailing whitespace from the line, and returns the resulting string.

#State of the program right berfore the function call: No variables are present in the function signature of `func_7`.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers obtained by splitting the input string by spaces and converting each split substring to an integer.
#Overall this is what the function does:The function `func_7` takes no input parameters. It reads a line of input from the user, splits it into substrings based on spaces, converts each substring into an integer, and returns a list of these integers.

#State of the program right berfore the function call: rows is a positive integer representing the number of times the function func_7() will be called and its results collected into a list.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #The program returns a list containing the results of calling `func_7()` `rows` number of times.
#Overall this is what the function does:The function `func_8` takes a positive integer `rows` as input and returns a list containing the results of calling the function `func_7()` `rows` number of times.

#State of the program right berfore the function call: This function does not take any parameters and returns the input as a string.
def func_9():
    return input()
    #The program returns the input as a string.
#Overall this is what the function does:The function does not accept any parameters and returns a string that is provided by the user input.

#State of the program right berfore the function call: This function does not have any parameters. It reads an integer input from the user, which represents the number of test cases (t), and returns it. The value of t is a positive integer such that 1 <= t <= 1000.
def func_10():
    return int(input())
    #The program returns an integer input read from the user, which represents the number of test cases (t), and the value of t is a positive integer such that 1 <= t <= 1000.
#Overall this is what the function does:The function `func_10` reads an integer input from the user, representing the number of test cases, and returns this integer. The returned value is guaranteed to be a positive integer within the range of 1 to 1000.

#State of the program right berfore the function call: No variables in the function signature.
def func_11():
    return input().split()
    #The program returns a list of strings, where each string is a substring from the input, split by whitespace.
#Overall this is what the function does:The function takes no input and returns a list of strings, where each string is a substring from the user's input, split by whitespace.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers, processing is a list of integers, da is an integer key present in d, and rank is a list of integers.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: `d` is a dictionary where keys are integers and values are lists of integers, `processing` is a list of integers, `da` is an integer key present in `d`, `rank` is a list of integers, `tmp` is 1000000000. The length of the list `d[da]` is greater than 1.
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: `d` is a dictionary where keys are integers and values are lists of integers, `processing` is a list of integers, `da` is an integer key present in `d`, `rank` is a list of integers, `tmp` is the minimum value returned by `func_12(d, processing, di, rank)` for all `di` in `d[da]`.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns `tmp + 1`, where `tmp` is the minimum value returned by `func_12(d, processing, di, rank)` for all `di` in `d[da]`.
#Overall this is what the function does:The function `func_12` processes a dictionary `d` with integer keys and list-of-integer values, a list `processing`, an integer `da` which is a key in `d`, and a list `rank`. It recursively evaluates the minimum value obtained from processing each element in the list `d[da]` and updates the `rank` list. If the list `d[da]` contains only one element, it returns 1. Otherwise, it returns the minimum value from the recursive calls plus one, updating the `rank` list with this value for the key `da`.

#State of the program right berfore the function call: a and b are integers, where a >= 0 and b >= 0.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns the tuple (1, 0, a) where 'a' is a non-negative integer.
    #State: a and b are integers, where a >= 0 and b >= 0, and b is not equal to 0
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns `(y, x - a // b * y, g)` where `y` and `x` are the coefficients from the function `func_13(b, a % b)`, and `g` is the GCD of `b` and `a % b`.
#Overall this is what the function does:The function `func_13` calculates and returns a tuple containing the coefficients and the greatest common divisor (GCD) of two non-negative integers `a` and `b`. If `b` is 0, it returns `(1, 0, a)`. Otherwise, it recursively computes the coefficients and GCD using the Euclidean algorithm.

#State of the program right berfore the function call: n and k are integers such that 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n.
def func_14():
    n, k = func_7()
    b = bin(n)[2:]
    l = len(b)
    if (k == 1) :
        if (n == 2) :
            return '1\n2'
            #The program returns the string '1\n2'
        #State: `n` and `k` are integers such that 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n, and their specific values are determined by the return values of `func_7()`. `k` is equal to 1. `b` is the binary representation of `n` as a string. `l` is the length of the binary representation of `n`. Additionally, `n` is not equal to 2.
        ans = [2, 3]
        for i in range(2, l):
            ans.append(2 ** i)
            
        #State: ans is [2, 3] + [4, 8, ..., 2
    else :
        bk = bin(k)[2:]
        ans = []
        lk = len(bk)
        for i in range(lk - 1):
            ans.append(2 ** i)
            
        #State: ans is a list containing [2
        ans.append(k - 1 - sum(ans))
        ans.append(k + 1)
        ans.append(2 * k + 1)
        for i in range(lk, l):
            ans.append(2 ** i)
            
        #State: [2, k - 3, k + 1, 2 * k + 1, 2
    #State: `n` and `k` are integers such that 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n, and their specific values are determined by the return values of `func_7()`. `b` is the binary representation of `n` as a string. `l` is the length of the binary representation of `n`. If `k` equals 1, `ans` is set to [2, 3] + [4, 8, ..., 2]. Otherwise, `ans` is set to [2, k - 3, k + 1, 2 * k + 1, 2].
    return str(len(ans)) + '\n' + ' '.join(map(str, ans))
    #The program returns "2\n2 3" if k is 1, otherwise it returns "5\n2 k-3 k+1 2*k+1 2"
#Overall this is what the function does:The function determines two integers `n` and `k` from the function `func_7()`. It then constructs and returns a string based on the value of `k`. If `k` is 1, it returns '1\n2' if `n` is 2, otherwise it returns a string starting with '2\n' followed by the numbers 2 and 3, and then powers of 2 up to the length of the binary representation of `n`. If `k` is not 1, it returns a string starting with '5\n' followed by the numbers 2, `k-1` minus the sum of powers of 2 up to the length of the binary representation of `k`, `k+1`, `2*k+1`, and powers of 2 from the length of the binary representation of `k` up to the length of the binary representation of `n`.

#State of the program right berfore the function call: No variables are present in the function signature of `func_15`. Therefore, no precondition can be extracted based on the given function signature.
def func_15():
    for _ in range(func_10()):
        sys.stdout.write(str(func_14()) + '\n')
        
    #State: The output will consist of `n` lines, where each line contains the string representation of the value returned by `func_14()` in each iteration of the loop.
#Overall this is what the function does:The function `func_15` does not accept any parameters. It outputs multiple lines to the standard output, with each line containing the string representation of a value returned by `func_14()`, repeated a number of times determined by the value returned by `func_10()`.

