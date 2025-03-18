#State of the program right berfore the function call: No variables are present in the function signature. Therefore, no precondition can be derived from the given function signature alone.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns an integer value that is read from the standard input buffer.
#Overall this is what the function does:The function `func_1` reads an integer from the standard input buffer and returns it.

#State of the program right berfore the function call: No specific variables are present in the function signature of `func_2`. The function is assumed to read integers from standard input, but based on the given signature alone, there are no variables to describe.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object that contains integers read from standard input, split by whitespace.
#Overall this is what the function does:The function `func_2` reads a line of integers from standard input, splits them by whitespace, and returns a map object containing these integers.

#State of the program right berfore the function call: No variables in the function signature. The function `func_3` does not have any parameters and seems to be reading from standard input. It is expected to return a list of integers obtained from a single line of input.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of integers obtained from a single line of input.
#Overall this is what the function does:The function `func_3` reads a single line of input from the standard input, processes it to extract integers, and returns a list of these integers.

#State of the program right berfore the function call: rows_number is a non-negative integer representing the number of rows or test cases to process.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #The program returns a list containing the results of `func_3()` called `rows_number` times.
#Overall this is what the function does:The function accepts a non-negative integer `rows_number` and returns a list containing the results of calling `func_3()` exactly `rows_number` times.

#State of the program right berfore the function call: No variables in the function signature.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns the input line from standard input, excluding any trailing newline characters.
#Overall this is what the function does:The function `func_5` reads a line from the standard input, removes any trailing newline characters, and returns the resulting string.

#State of the program right berfore the function call: No variables are present in the function signature.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a string that is the input line from standard input, with any trailing newline characters removed and decoded from bytes to a string.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing newline characters, decodes the input from bytes to a string, and returns this string.

#State of the program right berfore the function call: No variables in the function signature. The function `func_7` reads input from the standard input and returns a list of integers.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers that were read from the standard input, where each integer in the list corresponds to an integer value from the input string split by spaces.
#Overall this is what the function does:The function `func_7` reads a string of space-separated integers from the standard input, splits the string into individual integers, and returns a list containing these integers.

#State of the program right berfore the function call: rows is a positive integer representing the number of test cases.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #The program returns a list of length `rows`, where each element is the result of the function `func_7()` called `rows` times.
#Overall this is what the function does:The function accepts a positive integer `rows` representing the number of test cases and returns a list of length `rows`, where each element is the result of calling the function `func_7()`.

#State of the program right berfore the function call: This function does not take any parameters and does not return any specific value. It simply reads input from the standard input.
def func_9():
    return input()
    #The program returns the input read from the standard input.
#Overall this is what the function does:The function `func_9` reads a line of input from the standard input and returns it.

#State of the program right berfore the function call: The function `func_10` does not have any parameters and returns an integer value. This integer is expected to be the input value read from the standard input, which represents the number of test cases (t) in the problem description.
def func_10():
    return int(input())
    #The program returns an integer value that represents the number of test cases (t) read from the standard input.
#Overall this is what the function does:The function `func_10` reads an integer from the standard input and returns it, representing the number of test cases.

#State of the program right berfore the function call: No variables are present in the function signature. The function `func_11` does not take any parameters and does not have any defined variables in its signature.
def func_11():
    return input().split()
    #The program returns a list of substrings obtained by splitting the input string at whitespace.
#Overall this is what the function does:The function `func_11` does not accept any parameters and returns a list of substrings obtained by splitting the input string at whitespace.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers, processing is a list of integers, da is an integer, and rank is a list of integers.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: `d` is a dictionary where keys are integers and values are lists of integers, `processing` is a list of integers, `da` is an integer, `rank` is a list of integers, `tmp` is 10. The length of the list `d[da]` is not equal to 1.
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: `d` is unchanged, `processing` is a list of integers all set to 0, `da` is unchanged, `rank` is unchanged, `tmp` is the minimum value returned by `func_12` for any `di` in `d[da]`.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns `tmp + 1`, where `tmp` is the minimum value returned by `func_12` for any `di` in `d[da]`.
#Overall this is what the function does:The function `func_12` calculates a rank for a given integer `da` based on a dictionary `d` and a list `processing`. It returns `1` if the list associated with `da` in `d` contains only one element. Otherwise, it recursively calculates the minimum rank for all elements in the list `d[da]` and sets the rank of `da` to this minimum rank plus one. The function modifies the `rank` list in place to store the calculated rank for `da`.

#State of the program right berfore the function call: a and b are integers, where a is the dividend and b is the divisor.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns (1, 0, a)
    #State: a and b are integers, where a is the dividend and b is the divisor, and b is not equal to 0
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns the tuple (y, x - a // b * y, g), where y is an integer, x - a // b * y is the result of the expression using the given integers x, a, and b, and g is the greatest common divisor of a and b.
#Overall this is what the function does:The function accepts two integer parameters, `a` and `b`. If `b` is 0, it returns the tuple (1, 0, a). Otherwise, it returns a tuple (y, x - a // b * y, g), where `y` is an integer, `x - a // b * y` is derived from the recursive calculation, and `g` is the greatest common divisor of `a` and `b`.

#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n.
def func_14():
    n, k = func_7()
    b = bin(n)[2:]
    l = len(b)
    if (k == 1) :
        if (n == 2) :
            return '1\n2'
            #The program returns the string '1\n2'
        #State: `n` and `k` are the values returned by `func_7()`, and they satisfy the conditions 2 <= n <= 10^6 and 1 <= k <= n; `b` is the binary string representation of `n`; `l` is the length of the binary string `b`. The current value of `k` is 1, and `n` is not equal to 2.
        ans = [2, 3]
        for i in range(2, l):
            ans.append(2 ** i)
            
        #State: `ans` is `[2, 3]` followed by `2
    else :
        bk = bin(k)[2:]
        ans = []
        lk = len(bk)
        for i in range(lk - 1):
            ans.append(2 ** i)
            
        #State: `ans` is a list containing the powers of 2 from `2^0` to `2^(lk-2)`. All other variables (`n`, `k`, `b`, `l`, `bk`, `lk`) remain unchanged.
        ans.append(k - 1 - sum(ans))
        ans.append(k + 1)
        ans.append(2 * k + 1)
        for i in range(lk, l):
            ans.append(2 ** i)
            
        #State: `ans` is a list containing the powers of 2 from `2^0` to `2^(lk-2)`, followed by `k - 2^(lk-1)`, `k + 1`, and `2 * k + 1`, and then the powers of 2 from `2^(lk)` to `2^(l-1)`. All other variables (`n`, `k`, `b`, `l`, `bk`, `lk`) remain unchanged.
    #State: `n` and `k` are the values returned by `func_7()`, and they satisfy the conditions 2 <= n <= 10^6 and 1 <= k <= n; `b` is the binary string representation of `n`; `l` is the length of the binary string `b`. If `k` is 1, `ans` is `[2, 3]` followed by `2`. Otherwise, `ans` is a list containing the powers of 2 from `2^0` to `2^(lk-2)`, followed by `k - 2^(lk-1)`, `k + 1`, and `2 * k + 1`, and then the powers of 2 from `2^(lk)` to `2^(l-1)`. All other variables (`n`, `k`, `b`, `l`, `bk`, `lk`) remain unchanged.
    return ' '.join(map(str, ans))
    #The program returns a space-separated string of integers. If `k` is 1, the string is "2 3 2". Otherwise, the string starts with powers of 2 from `2^0` to `2^(lk-2)`, followed by `k - 2^(lk-1)`, `k + 1`, `2 * k + 1`, and then the powers of 2 from `2^(lk)` to `2^(l-1)`.
#Overall this is what the function does:The function accepts two integer parameters `n` and `k` such that 2 <= n <= 10^6 and 1 <= k <= n. If `k` is 1, the function returns the string '1\n2'. Otherwise, it returns a space-separated string of integers that starts with powers of 2 from `2^0` to `2^(lk-2)`, followed by `k - 2^(lk-1)`, `k + 1`, `2 * k + 1`, and then the powers of 2 from `2^(lk)` to `2^(l-1)`, where `lk` is the length of the binary representation of `k`.

#State of the program right berfore the function call: This function does not have any parameters in its signature, so no precondition can be derived from the variables in the function signature.
def func_15():
    for _ in range(func_10()):
        sys.stdout.write(str(func_14()) + '\n')
        
    #State: The loop has executed 3 times, printing the numbers 1, 2, and 3 each on a new line. The state of variables not involved in the loop remains unchanged.
#Overall this is what the function does:The function `func_15` does not accept any parameters and prints numbers to the standard output. Specifically, it prints the numbers 1, 2, and 3, each on a new line, a total of three times. The state of any variables not involved in the loop remains unchanged.

