#State of the program right berfore the function call: No variables are present in the function signature.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns an integer that is read from the standard input.
#Overall this is what the function does:The function `func_1` accepts no parameters and returns an integer that is read from the standard input.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`. However, based on the context, it can be inferred that this function reads a line from standard input, splits it into components, converts them to integers, and returns them as a map object. The input is expected to contain space-separated integers.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object that contains integers converted from space-separated values read from standard input.
#Overall this is what the function does:The function reads a line from standard input, splits it into space-separated components, converts each component to an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: The function `func_3` does not take any input parameters. It reads a line from the standard input, splits it into a list of strings, converts each string to an integer, and returns the resulting list of integers.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of integers that were read from the standard input, split by whitespace, and converted from strings to integers.
#Overall this is what the function does:The function reads a line from the standard input, splits it into a list of substrings based on whitespace, converts each substring to an integer, and returns the resulting list of integers.

#State of the program right berfore the function call: rows_number is a positive integer representing the number of rows or test cases.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #The program returns a list containing the result of `func_3()` called `rows_number` times.
#Overall this is what the function does:The function accepts a parameter `rows_number`, which is a positive integer representing the number of rows or test cases. It returns a list containing the result of `func_3()` called `rows_number` times.

#State of the program right berfore the function call: This function does not have any parameters. It reads a line from the standard input and returns it as a byte string after removing the trailing newline character.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns a byte string that is a line read from the standard input, with the trailing newline character removed.
#Overall this is what the function does:The function reads a line from the standard input, removes the trailing newline character, and returns the result as a byte string.

#State of the program right berfore the function call: No variables are present in the function signature of `func_6`.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a string that is read from standard input, stripped of any trailing newline characters, and decoded from bytes to a string.
#Overall this is what the function does:The function `func_6` reads a line of text from standard input, removes any trailing newline characters, decodes it from bytes to a string, and returns the resulting string.

#State of the program right berfore the function call: No variables are present in the function signature of `func_7`.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers, where each integer is obtained by converting each element of the input string (split by spaces) to an integer.
#Overall this is what the function does:The function `func_7` reads a line of input from the user, splits it into components based on spaces, converts each component into an integer, and returns a list of these integers.

#State of the program right berfore the function call: rows is a positive integer representing the number of test cases.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #The program returns a list of length `rows`, where each element is the result of calling `func_7()`
#Overall this is what the function does:The function `func_8` takes a positive integer `rows` as input and returns a list of length `rows`, where each element is the result of calling `func_7()`.

#State of the program right berfore the function call: The function does not have any parameters, implying that it does not directly contribute to the solution based on the provided signature. However, if we consider the context, it seems to be a placeholder function that might be intended to take input. If we were to hypothesize based on the problem description and typical input handling, a more fitting signature might include parameters for n and k. Assuming such a signature, it would be: def func_9(n, k): where n and k are integers such that 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n.
def func_9():
    return input()
    #The program returns the input provided by the user, which is a string.
#Overall this is what the function does:The function accepts no parameters and returns a string input provided by the user.

#State of the program right berfore the function call: No variables in the function signature.
def func_10():
    return int(input())
    #The program returns an integer value that is provided by the user input.
#Overall this is what the function does:The function `func_10` accepts no parameters and returns an integer value provided by the user input.

#State of the program right berfore the function call: The function `func_11` does not take any parameters. It reads a line of input from the user, which is expected to contain space-separated values. The function returns a list of strings, where each string is one of the space-separated values from the input.
def func_11():
    return input().split()
    #The program returns a list of strings, where each string is one of the space-separated values from the user's input.
#Overall this is what the function does:The function reads a line of input from the user, which is expected to contain space-separated values, and returns a list of strings, where each string is one of the space-separated values from the input.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers, processing is a list of integers, da is an integer, and rank is a list of integers.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: `d` is a dictionary where keys are integers and values are lists of integers, `processing` is a list of integers, `da` is an integer, `rank` is a list of integers, `tmp` is `10`. The length of the list `d[da]` is greater than 1.
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: `d` is a dictionary where keys are integers and values are lists of integers, `processing` is a list of integers (all elements are `0`), `da` is an integer, `rank` is a list of integers, `tmp` is the minimum value returned by `func_12(d, processing, di, rank)` across all valid iterations.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns `tmp + 1`, where `tmp` is the minimum value returned by `func_12(d, processing, di, rank)` across all valid iterations.
#Overall this is what the function does:The function `func_12` calculates a rank for a given integer `da` based on a recursive evaluation of a dictionary `d` and a processing list. It updates the `rank` list with the calculated rank for `da`. The function returns `1` if the list associated with `da` in `d` contains only one element; otherwise, it returns the minimum rank value obtained from recursive calls plus one.

#State of the program right berfore the function call: a and b are integers such that a >= 0 and b >= 0.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns the tuple (1, 0, a) where 'a' is a non-negative integer
    #State: a and b are integers such that a >= 0 and b >= 0, and b is not equal to 0
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns `y`, `x - a // b * y`, and `g` where `x` and `y` are coefficients from the extended Euclidean algorithm for `a` and `b`, and `g` is the greatest common divisor of `a` and `b`.
#Overall this is what the function does:The function `func_13` accepts two non-negative integers `a` and `b`. It returns a tuple containing coefficients `x`, `y`, and the greatest common divisor `g` of `a` and `b`, as derived from the extended Euclidean algorithm. If `b` is 0, it specifically returns `(1, 0, a)`.

#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n.
def func_14():
    n, k = func_7()
    b = bin(n)[2:]
    l = len(b)
    if (k == 1) :
        if (n == 2) :
            return '1\n2'
            #The program returns the string '1\n2'
        #State: `k` equals 1, `n` is an integer such that `2 <= n <= 10^6` and `n` is not equal to 2, `b` is the binary string representation of `n` without the '0b' prefix, and `l` is the length of the binary string `b`.
        ans = [2, 3]
        for i in range(2, l):
            ans.append(2 ** i)
            
        #State: `k` equals 1, `n` is an integer such that `2 <= n <= 10^6` and `n` is not equal to 2, `b` is the binary string representation of `n` without the '0b' prefix, `l` is the length of the binary string `b`, `ans` is `[2, 3, 2^2, 2^3, ..., 2^(l-1)]`.
    else :
        bk = bin(k)[2:]
        ans = []
        lk = len(bk)
        for i in range(lk - 1):
            ans.append(2 ** i)
            
        #State: `n` and `k` are integers such that `2 <= n <= 10^6` and `1 < k <= n`; `b` is the binary string representation of `n` without the '0b' prefix; `l` is the length of the binary string `b`; `bk` is the binary string representation of `k` without the '0b' prefix; `lk` is the length of the binary string `bk`; `ans` is a list containing `[2
        ans.append(k - 1 - sum(ans))
        ans.append(k + 1)
        ans.append(2 * k + 1)
        for i in range(lk, l):
            ans.append(2 ** i)
            
        #State: `ans` is `[2, k - 3, k + 1, 2 * k + 1, 2
    #State: `n` and `k` are integers such that `2 <= n <= 10^6` and `1 <= k <= n`; `b` is the binary string representation of `n` without the '0b' prefix; `l` is the length of the binary string `b`. If `k` equals 1, `ans` is `[2, 3, 2^2, 2^3, ..., 2^(l-1)]`. Otherwise, `ans` is `[2, k - 3, k + 1, 2 * k + 1, 2]`.
    return ' '.join(map(str, ans))
    #The program returns a space-separated string of the list `ans`, where `ans` is `[2, 3, 2^2, 2^3, ..., 2^(l-1)]` if `k` equals 1, or `[2, k - 3, k + 1, 2 * k + 1, 2]` if `k` does not equal 1.
#Overall this is what the function does:The function accepts two integer parameters `n` and `k` such that `2 <= n <= 10^6` and `1 <= k <= n`. If `n` equals 2 and `k` equals 1, it returns the string '1\n2'. Otherwise, it returns a space-separated string of integers. If `k` equals 1, the string represents the list `[2, 3, 2^2, 2^3, ..., 2^(l-1)]`, where `l` is the number of bits in the binary representation of `n`. If `k` does not equal 1, the string represents the list `[2, k - 1 - sum([2^i for i in range(lk - 1)]), k + 1, 2 * k + 1, 2^lk, 2^(lk+1), ..., 2^(l-1)]`, where `lk` is the number of bits in the binary representation of `k`.

#State of the program right berfore the function call: This function does not have any parameters in its signature. It relies on other functions (`func_10` and `func_14`) to provide the necessary values for the number of test cases and the sequence generation logic, respectively.
def func_15():
    for _ in range(func_10()):
        sys.stdout.write(str(func_14()) + '\n')
        
    #State: the printed output of `func_14()` for each iteration, each followed by a newline character.
#Overall this is what the function does:The function `func_15` generates and prints a sequence of values, each on a new line, based on the number of test cases provided by `func_10` and the sequence generation logic provided by `func_14`.

