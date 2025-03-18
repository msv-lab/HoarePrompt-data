#State of the program right berfore the function call: No variables in the function signature.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns an integer that is read from the standard input buffer.
#Overall this is what the function does:The function `func_1` reads an integer from the standard input buffer and returns it.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2()`, thus no precondition can be specified based on the variables.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object that contains integers obtained by splitting the input line from sys.stdin.buffer.readline()
#Overall this is what the function does:The function `func_2` reads a line from the standard input, splits it into components, converts those components into integers, and returns a map object containing these integers.

#State of the program right berfore the function call: The function `func_3` does not have any parameters. It reads a line from the standard input, splits it into components, converts each component to an integer, and returns the resulting list of integers.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of integers that were read from the standard input, split by whitespace, and converted to integers.
#Overall this is what the function does:The function reads a line of input from the standard input, splits it into components based on whitespace, converts each component to an integer, and returns the resulting list of integers.

#State of the program right berfore the function call: rows_number is a positive integer representing the number of rows or test cases to process.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #The program returns a list containing the result of `func_3()` called `rows_number` times. Each element in the list is the result of one call to `func_3()`.
#Overall this is what the function does:The function accepts a positive integer `rows_number` and returns a list containing the result of `func_3()` called `rows_number` times, with each element in the list being the result of one call to `func_3()`.

#State of the program right berfore the function call: No variables are present in the function signature.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns a string that is read from the standard input, with any trailing newline characters removed.
#Overall this is what the function does:The function `func_5` reads a line of text from the standard input, removes any trailing newline characters, and returns the resulting string.

#State of the program right berfore the function call: No variables are present in the function signature of `func_6`.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a string that is the next line of input from standard input, with any trailing newline characters removed and decoded from bytes to a string.
#Overall this is what the function does:The function `func_6` reads the next line of input from standard input, removes any trailing newline characters, decodes the input from bytes to a string, and returns the resulting string.

#State of the program right berfore the function call: No variables in the function signature. This function reads input and returns a list of integers.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers that are obtained by splitting the input string and converting each split part to an integer.
#Overall this is what the function does:The function `func_7` reads a line of input from the user, splits it into parts based on whitespace, converts each part to an integer, and returns a list of these integers.

#State of the program right berfore the function call: rows is a positive integer representing the number of test cases.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #The program returns a list containing the result of `func_7()` called `rows` number of times.
#Overall this is what the function does:The function accepts a positive integer `rows` and returns a list containing the result of `func_7()` called `rows` number of times.

#State of the program right berfore the function call: This function does not have parameters. It reads input from the standard input.
def func_9():
    return input()
    #The program returns the input read from the standard input.
#Overall this is what the function does:The function `func_9` reads input from the standard input and returns it.

#State of the program right berfore the function call: The function `func_10` does not have any parameters. It reads and returns an integer from the input.
def func_10():
    return int(input())
    #The program returns an integer read from the input.
#Overall this is what the function does:The function `func_10` reads an integer from the input and returns it.

#State of the program right berfore the function call: No specific variables are present in the function signature of `func_11()`. Therefore, there are no preconditions related to the variables in the function signature.
def func_11():
    return input().split()
    #The program returns a list of strings, where each string is a substring from the user's input, split by whitespace.
#Overall this is what the function does:The function `func_11` does not accept any parameters. It prompts the user for input, splits the input string by whitespace, and returns a list of the resulting substrings.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers, processing is a list of integers, da is an integer, and rank is a list of integers.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: `d` is a dictionary where keys are integers and values are lists of integers, `processing` is a list of integers, `da` is an integer, `rank` is a list of integers, `tmp` is 1000000000, and the length of `d[da]` is not equal to 1
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: `d` is a dictionary where keys are integers and values are lists of integers, `processing` is a list of integers, `da` is an integer, `rank` is a list of integers, `tmp` is the minimum value returned by `func_12` across all iterations.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns `tmp + 1`, where `tmp` is the minimum value returned by `func_12` across all iterations.
#Overall this is what the function does:The function `func_12` processes a dictionary `d` where keys are integers and values are lists of integers, a list of integers `processing`, an integer `da`, and a list of integers `rank`. It recursively evaluates the structure defined by `d` and updates the `rank` list. The function returns 1 if the list associated with `da` in `d` contains exactly one element. Otherwise, it returns the minimum value obtained from recursive calls to `func_12` plus one, updating the `rank` list with this value.

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
    #The program returns (y, x - a // b * y, g)
#Overall this is what the function does:The function `func_13` computes and returns a tuple `(y, x - a // b * y, g)` where `a` and `b` are integers, with `a` as the dividend and `b` as the divisor. If `b` is 0, it returns `(1, 0, a)`. Otherwise, it recursively calculates values based on the Euclidean algorithm, ultimately returning the coefficients of Bézout's identity and the greatest common divisor (GCD) of `a` and `b`.

#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n.
def func_14():
    n, k = func_7()
    b = bin(n)[2:]
    l = len(b)
    if (k == 1) :
        if (n == 2) :
            return '1\n2'
            #The program returns the string '1\n2'
        #State: `n` and `k` are the values returned by `func_7()`, `b` is the binary string representation of `n` without the '0b' prefix, `l` is the length of `b`, and `k` is equal to 1. Additionally, `n` is not equal to 2.
        ans = [2, 3]
        for i in range(2, l):
            ans.append(2 ** i)
            
        #State: `n` is 10, `k` is 1, `b` is '1010', `l` is 4, `ans` is `[2, 3, 4, 8]`.
    else :
        bk = bin(k)[2:]
        ans = []
        lk = len(bk)
        for i in range(lk - 1):
            ans.append(2 ** i)
            
        #State: `ans` is a list containing `[1, 2, 4, ..., 2^{(lk-2)}]`. The values of `n`, `k`, `b`, `l`, `bk`, and `lk` remain unchanged.
        ans.append(k - 1 - sum(ans))
        ans.append(k + 1)
        ans.append(2 * k + 1)
        for i in range(lk, l):
            ans.append(2 ** i)
            
        #State: [1, 2, 4, ..., 2^{(lk-2)}, k - 2^{(lk-1)}, k + 1, 2 * k + 1, 2^{lk}, 2^{(lk+1)}, ..., 2^{(l-1)}]
    #State: `n` and `k` are the values returned by `func_7()`, `b` is the binary string representation of `n` without the '0b' prefix, `l` is the length of `b`. If `k` is 1, then `n` is 10, `b` is '1010', `l` is 4, and `ans` is `[2, 3, 4, 8]`. Otherwise, `ans` is `[1, 2, 4, ..., 2^{(lk-2)}, k - 2^{(lk-1)}, k + 1, 2 * k + 1, 2^{lk}, 2^{(lk+1)}, ..., 2^{(l-1)}]`.
    return str(len(ans)) + '\n' + ' '.join(map(str, ans))
    #4
    #2 3 4 8
#Overall this is what the function does:The function `func_14` generates and returns a string based on the values of `n` and `k` returned by `func_7()`. If `k` is 1 and `n` is 2, it returns the string '1\n2'. Otherwise, it constructs a list of integers and returns a string starting with the length of the list followed by the integers in the list separated by spaces.

#State of the program right berfore the function call: This function does not take any parameters directly related to the problem description. It seems to be a high-level function that orchestrates the solution by calling other functions (`func_10` and `func_14`). No specific precondition can be derived from the signature alone.
def func_15():
    for _ in range(func_10()):
        sys.stdout.write(str(func_14()) + '\n')
        
    #State: The function writes the string representation of the value returned by `func_14()` to the standard output, followed by a newline character, for `func_10()` number of times.
#Overall this is what the function does:The function `func_15` does not accept any parameters. It writes the string representation of the value returned by `func_14()` to the standard output, followed by a newline character, for a number of times equal to the value returned by `func_10()`.

