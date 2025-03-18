#State of the program right berfore the function call: None. This function does not take any parameters and is used to read an integer from standard input.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns an integer read from standard input.
#Overall this is what the function does:The function reads an integer from standard input and returns it. The function does not take any parameters. After the function concludes, the program has an integer value that was read from the standard input.

#State of the program right berfore the function call: None. This function does not take any parameters and is used to read input from stdin, which is expected to be a line of space-separated integers.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns an iterator that yields the integers read from a line of space-separated integers in stdin.
#Overall this is what the function does:The function `func_2` reads a line of space-separated integers from standard input (stdin) and returns an iterator that yields these integers. The function does not take any parameters. After the function concludes, the returned iterator can be used to access the integers one by one.

#State of the program right berfore the function call: This function does not take any parameters, and it reads a line from standard input, which is expected to contain space-separated integers.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of integers, where each integer is read from a single line of standard input and was originally space-separated.
#Overall this is what the function does:The function `func_3` reads a line of input from standard input, which is expected to contain space-separated integers, and returns a list of integers. The function does not take any parameters. After the function concludes, the program has a list of integers that were originally space-separated in the input line.

#State of the program right berfore the function call: rows_number is a non-negative integer.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #The program returns a list of length `rows_number`, where each element is the result of calling `func_3()`.
#Overall this is what the function does:The function `func_4` accepts a non-negative integer `rows_number` and returns a list of length `rows_number`, where each element is the result of calling `func_3()`. The function does not modify any external state or variables.

#State of the program right berfore the function call: This function does not take any input parameters.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns the next line of input from the standard input stream, excluding the trailing newline character.
#Overall this is what the function does:The function `func_5` does not accept any parameters and returns the next line of input from the standard input stream, excluding the trailing newline character.

#State of the program right berfore the function call: None of the variables in the function signature are used. The function reads a line from standard input, which is expected to be a string.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a string read from standard input, with trailing whitespace removed.
#Overall this is what the function does:Reads a line from standard input, removes trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: None of the variables in the function signature are used, but the function assumes that the input provided is a string that can be split and converted into a list of integers.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers, where each integer is derived from splitting the input string by spaces and converting each split part into an integer.
#Overall this is what the function does:The function `func_7` accepts no parameters and returns a list of integers. It reads a string from the user input, splits the string by spaces, and converts each resulting substring into an integer. The final state of the program after the function concludes is that it has a list of integers derived from the input string.

#State of the program right berfore the function call: rows is a non-negative integer.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #The program returns a list containing the results of calling `func_7()` `rows` times, where `rows` is a non-negative integer.
#Overall this is what the function does:The function `func_8` accepts a parameter `rows`, which is a non-negative integer, and returns a list containing the results of calling `func_7()` `rows` times. The final state of the program is that it has a list of `rows` elements, each element being the result of a call to `func_7()`.

#State of the program right berfore the function call: None of the variables used in the function signature are relevant to the problem description. The function `func_9` does not take any parameters and is not directly related to solving the problem of finding a sequence of non-negative integers with specific subsequence sum constraints.
def func_9():
    return input()
    #The program returns the input provided by the user.
#Overall this is what the function does:The function `func_9` does not accept any parameters and returns the input provided by the user. After the function concludes, the program state is such that the user's input is returned as the result of the function call.

#State of the program right berfore the function call: None. This function does not take any parameters and is used to read an integer from the input, which could be the number of test cases or any other integer input.
def func_10():
    return int(input())
    #The program returns an integer input by the user.
#Overall this is what the function does:The function `func_10` does not accept any parameters. It reads an integer from the user input and returns this integer. The final state of the program after the function concludes is that it has an integer value that was provided by the user.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_11():
    return input().split()
    #The program returns a list of strings, where each string is a part of the input provided by the user, split by whitespace.
#Overall this is what the function does:The function `func_11` does not accept any parameters. It reads a line of input from the user and returns a list of strings, where each string is a part of the input split by whitespace. The function does not modify any external state or variables.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers, processing is a list of integers of length at least max(da, max(d[da])) initialized to 0, da is a positive integer, and rank is a list of integers of length at least max(da, max(d[da])) initialized to 0.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns the integer 1.
    #State: d is a dictionary where keys are integers and values are lists of integers, processing is a list of integers of length at least max(da, max(d[da])) initialized to 0, da is a positive integer, rank is a list of integers of length at least max(da, max(d[da])) initialized to 0, tmp is 1000000000, and the length of the list d[da] is greater than 1.
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: The dictionary `d` remains unchanged. The list `processing` will have some of its elements set to 1 at the indices corresponding to the elements in `d[da]` minus 1, but these elements will be reset to 0 by the end of the loop. The list `rank` remains unchanged. The variable `tmp` will be updated to the minimum value returned by `func_12(d, processing, di, rank)` for all elements `di` in `d[da]` where `processing[di - 1]` was initially 0.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns the value of `tmp + 1`, where `tmp` is the minimum value returned by `func_12(d, processing, di, rank)` for all elements `di` in `d[da]` where `processing[di - 1]` was initially 0, and `rank[da - 1]` is updated to this value.
#Overall this is what the function does:The function `func_12` accepts a dictionary `d` with integer keys and lists of integers as values, a list `processing` initialized to 0, a positive integer `da`, and a list `rank` initialized to 0. It returns 1 if the list `d[da]` contains only one element. Otherwise, it returns the minimum value of recursive calls to `func_12` for elements in `d[da]` where `processing[di - 1]` is 0, incremented by 1, and updates `rank[da - 1]` to this value. The dictionary `d` and the list `rank` remain unchanged except for the update to `rank[da - 1]`. The list `processing` is used to track processed elements but is reset to its initial state by the end of the function.

#State of the program right berfore the function call: a and b are non-negative integers, and b is not equal to 0.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns the values 1, 0, and a non-negative integer `a`.
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns a tuple containing the value of `y`, the result of `x - (a // b) * y`, and the value of `g`. Here, `x`, `y`, and `g` are the values returned by the function `func_13(b, a % b)`.
#Overall this is what the function does:The function `func_13` accepts two non-negative integers `a` and `b` (where `b` is not 0). It returns a tuple `(x, y, g)` where `g` is the greatest common divisor (GCD) of `a` and `b`, and `x` and `y` are integers such that `a * x + b * y = g`. If `b` is 0, the function returns `(1, 0, a)`. Otherwise, it recursively computes the values of `x`, `y`, and `g` using the Euclidean algorithm.

#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n.
def func_14():
    n, k = func_7()
    b = bin(n)[2:]
    l = len(b)
    if (k == 1) :
        if (n == 2) :
            return '1\n2'
            #The program returns the string '1\n2'.
        #State: `n` and `k` are updated to the values returned by `func_7()`, 2 <= n <= 10^6 and 1 <= k <= n still holds true, `b` is the binary representation of `n` without the '0b' prefix, `l` is the length of `b`, the current value of `k` is 1, and `n` is not equal to 2.
        ans = [2, 3]
        for i in range(2, l):
            ans.append(2 ** i)
            
        #State: `n` and `k` are updated to the values returned by `func_7()`, 2 <= n <= 10^6 and 1 <= k <= n still holds true, `b` is the binary representation of `n` without the '0b' prefix, `l` is the length of `b`, `k` is 1, `n` is not equal to 2, `ans` is [2, 3, 4, 8, 16, 32, 64, 128, ..., 2^(l-1)].
    else :
        bk = bin(k)[2:]
        ans = []
        lk = len(bk)
        for i in range(lk - 1):
            ans.append(2 ** i)
            
        #State: `n` and `k` remain unchanged, `b` remains the binary representation of `n` without the '0b' prefix, `l` remains the length of `b`, `k` is not equal to 1, `bk` remains the binary representation of `k` without the '0b' prefix, `ans` is a list containing the powers of 2 from 2^0 to 2^(lk-2), `lk` remains the length of `bk`.
        ans.append(k - 1 - sum(ans))
        ans.append(k + 1)
        ans.append(2 * k + 1)
        for i in range(lk, l):
            ans.append(2 ** i)
            
        #State: `n` and `k` remain unchanged, `b` remains the binary representation of `n` without the '0b' prefix, `l` remains the length of `b`, `k` is not equal to 1, `bk` remains the binary representation of `k` without the '0b' prefix, `lk` remains the length of `bk`, `ans` now contains the powers of 2 from 2^0 to 2^(lk-2), followed by `k - 1 - sum(ans)`, `k + 1`, `2 * k + 1`, and then the powers of 2 from 2^lk to 2^(l-1).
    #State: *`n` and `k` are updated to the values returned by `func_7()`, 2 <= n <= 10^6 and 1 <= k <= n still holds true, `b` is the binary representation of `n` without the '0b' prefix, `l` is the length of `b`. If `k` is 1, `n` is not equal to 2, and `ans` is [2, 3, 4, 8, 16, 32, 64, 128, ..., 2^(l-1)]. Otherwise, `n` and `k` remain unchanged, `b` remains the binary representation of `n` without the '0b' prefix, `l` remains the length of `b`, `bk` remains the binary representation of `k` without the '0b' prefix, `lk` remains the length of `bk`, and `ans` now contains the powers of 2 from 2^0 to 2^(lk-2), followed by `k - 1 - sum(ans)`, `k + 1`, `2 * k + 1`, and then the powers of 2 from 2^lk to 2^(l-1).
    return ' '.join(map(str, ans))
    #The program returns a string containing the elements of `ans` separated by spaces. If `k` is 1, `ans` is a list of powers of 2 from 2 to 2^(l-1), where `l` is the length of the binary representation of `n` without the '0b' prefix. Otherwise, `ans` is a list that starts with the powers of 2 from 2^0 to 2^(lk-2), followed by `k - 1 - sum(ans)`, `k + 1`, `2 * k + 1`, and then the powers of 2 from 2^lk to 2^(l-1), where `lk` is the length of the binary representation of `k` without the '0b' prefix.
#Overall this is what the function does:The function `func_14` accepts no parameters and implicitly uses two integer values `n` and `k` obtained from the function `func_7`, where `2 <= n <= 10^6` and `1 <= k <= n`. It returns a string. If `k` is 1 and `n` is 2, the function returns the string '1\n2'. If `k` is 1 and `n` is not 2, the function returns a string containing the powers of 2 from 2 to 2^(l-1) separated by spaces, where `l` is the length of the binary representation of `n` without the '0b' prefix. If `k` is not 1, the function returns a string containing a sequence of numbers starting with the powers of 2 from 2^0 to 2^(lk-2), followed by `k - 1 - sum(ans)`, `k + 1`, `2 * k + 1`, and then the powers of 2 from 2^lk to 2^(l-1), where `lk` is the length of the binary representation of `k` without the '0b' prefix.

#State of the program right berfore the function call: No variables are passed to the function func_15().
def func_15():
    for _ in range(func_10()):
        sys.stdout.write(str(func_14()) + '\n')
        
    #State: The loop will print the value `m` `n` times, each on a new line.
#Overall this is what the function does:The function `func_15` does not accept any parameters. It prints the value returned by `func_14` a number of times equal to the value returned by `func_10`, each value on a new line. The function does not return any value.

