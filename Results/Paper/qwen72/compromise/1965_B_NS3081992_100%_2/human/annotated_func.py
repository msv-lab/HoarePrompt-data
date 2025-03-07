#State of the program right berfore the function call: None. This function does not take any parameters.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns an integer read from the standard input.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns an integer read from the standard input. The final state of the program after the function concludes is that an integer has been read from the standard input and is returned to the caller.

#State of the program right berfore the function call: This function does not have any input parameters. It reads a line from standard input, splits the line into parts, and maps each part to an integer. The line should contain at least one integer.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object that contains integers, which are the result of splitting a line read from standard input and converting each part to an integer. The line should contain at least one integer.
#Overall this is what the function does:The function `func_2` reads a line from standard input, splits the line into parts, converts each part to an integer, and returns a map object containing these integers. The line must contain at least one integer.

#State of the program right berfore the function call: This function does not take any input parameters. It is used to read a line of input from stdin, which is expected to contain integers separated by spaces. The function returns a list of integers.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of integers, where each integer is read from a single line of input from stdin, and the integers are separated by spaces.
#Overall this is what the function does:Reads a line of input from stdin, which is expected to contain integers separated by spaces, and returns a list of these integers.

#State of the program right berfore the function call: rows_number is a non-negative integer.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #The program returns a list containing `rows_number` elements, where each element is the result of calling `func_3()`.
#Overall this is what the function does:The function `func_4` accepts a non-negative integer `rows_number` and returns a list containing `rows_number` elements, where each element is the result of calling `func_3()`. If `rows_number` is 0, the function returns an empty list.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns the next line of input from the standard input, with trailing whitespace removed.
#Overall this is what the function does:The function `func_5` does not accept any parameters. It reads the next line from the standard input, removes any trailing whitespace from the line, and returns the resulting string. The state of the program after the function concludes is that the next line of input from the standard input has been consumed and the function has returned the line with trailing whitespace removed.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns the next line of input from the standard input (stdin) after stripping the trailing newline and decoding it to a string.
#Overall this is what the function does:The function `func_6` does not accept any parameters. It reads the next line of input from the standard input (stdin), strips any trailing newline characters, decodes the result from bytes to a string, and returns this string.

#State of the program right berfore the function call: None. The function `func_7` does not take any parameters and is used to read input, which is expected to be a line of space-separated integers.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers, where each integer is derived from the space-separated integers input by the user.
#Overall this is what the function does:The function `func_7` reads a line of space-separated integers from the user input and returns a list of integers. The function does not take any parameters. After the function concludes, the user's input is converted into a list of integers, and this list is the final state of the program.

#State of the program right berfore the function call: rows is a non-negative integer.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #The program returns a list containing the result of `func_7()` called `rows` times, where `rows` is a non-negative integer.
#Overall this is what the function does:The function `func_8` accepts a non-negative integer `rows` and returns a list containing the result of `func_7()` called `rows` times. The final state of the program is that it has a list with `rows` elements, each element being the result of a call to `func_7()`.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_9():
    return input()
    #The program returns the input provided by the user.
#Overall this is what the function does:The function `func_9` does not accept any parameters and returns the input provided by the user. After the function concludes, the program state includes the user's input as the return value.

#State of the program right berfore the function call: None
def func_10():
    return int(input())
    #The program returns an integer value that is input by the user.
#Overall this is what the function does:The function `func_10` does not accept any parameters and returns an integer value that is input by the user. After the function concludes, the program state includes the returned integer, which is the user's input converted to an integer.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_11():
    return input().split()
    #The program returns a list of strings, where each string is a part of the input provided by the user, split by whitespace.
#Overall this is what the function does:The function `func_11` does not accept any parameters and returns a list of strings, where each string is a part of the input provided by the user, split by whitespace. The function effectively reads a line of input from the user and splits it into a list of substrings based on whitespace characters (spaces, tabs, newlines). After the function concludes, the program state includes the returned list of strings, and any variables that were not part of the function call remain unchanged.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers, processing is a list of integers of length at least max(da, max(d[da])) initialized to 0, da is an integer key present in d, and rank is a list of integers of length at least max(da, max(d[da])) initialized to 0.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1.
    #State: d is a dictionary where keys are integers and values are lists of integers, processing is a list of integers of length at least max(da, max(d[da])) initialized to 0, da is an integer key present in d, rank is a list of integers of length at least max(da, max(d[da])) initialized to 0, tmp is 1000000000, and the length of the list d[da] is greater than 1.
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: The dictionary `d` remains unchanged. The list `processing` will have some of its elements set to 1 and then reset to 0 by the end of the loop, so it will be the same as the initial state. The integer `da` remains unchanged. The list `rank` remains unchanged. The variable `tmp` will be updated to the minimum value returned by `func_12(d, processing, di, rank)` for all `di` in `d[da]` where `processing[di - 1]` was initially 0.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns the minimum value returned by `func_12(d, processing, di, rank)` for all `di` in `d[da]` where `processing[di - 1]` was initially 0, plus 1.
#Overall this is what the function does:The function `func_12` accepts four parameters: `d` (a dictionary where keys are integers and values are lists of integers), `processing` (a list of integers of length at least the maximum value of `da` and the maximum integer in `d[da]`, initialized to 0), `da` (an integer key present in `d`), and `rank` (a list of integers of length at least the maximum value of `da` and the maximum integer in `d[da]`, initialized to 0). If the list `d[da]` has exactly one element, the function returns 1. Otherwise, it recursively processes each element in `d[da]` that has not been processed yet (as indicated by `processing[di - 1]` being 0), and updates the `rank[da - 1]` with the minimum value returned by these recursive calls plus 1. The function ultimately returns this minimum value plus 1. The dictionary `d` and the list `processing` remain unchanged by the end of the function, while the list `rank` is updated.

#State of the program right berfore the function call: a and b are non-negative integers, and b is not equal to 0.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns the values (1, 0, a), where 'a' is a non-negative integer.
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns a tuple containing `y`, `x - (a // b) * y`, and `g`, where `x`, `y`, and `g` are the values returned by `func_13(b, a % b)`.
#Overall this is what the function does:The function `func_13` accepts two non-negative integers `a` and `b` (where `b` is not 0). It returns a tuple `(x, y, g)` where `g` is the greatest common divisor (GCD) of `a` and `b`, and `x` and `y` are integers such that `a * x + b * y = g`. If `b` is 0, the function returns `(1, 0, a)`. Otherwise, it recursively computes the values by calling itself with `b` and `a % b`.

#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n.
def func_14():
    n, k = func_7()
    b = bin(n)[2:]
    l = len(b)
    if (k == 1) :
        if (n == 2) :
            return '1\n2'
            #The program returns the string '1\n2'.
        #State: *`n` and `k` are the values returned by `func_7()`, `b` is the binary representation of `n` without the '0b' prefix, `l` is the length of `b`. The current value of `k` is 1, and `n` is not equal to 2.
        ans = [2, 3]
        for i in range(2, l):
            ans.append(2 ** i)
            
        #State: `n` remains the same, `k` is 1, `b` remains the binary representation of `n` without the '0b' prefix, `l` remains the length of `b`, `ans` is [2, 3, 4, 8, ..., 2
    else :
        bk = bin(k)[2:]
        ans = []
        lk = len(bk)
        for i in range(lk - 1):
            ans.append(2 ** i)
            
        #State: `ans` is a list containing powers of 2 from \(2^0\) to \(2^{lk-2}\), `n` and `k` remain unchanged, `b` remains the binary representation of `n` without the '0b' prefix, `l` remains the length of `b`, `bk` remains the binary representation of `k` without the '0b' prefix, and `lk` remains the length of `bk`.
        ans.append(k - 1 - sum(ans))
        ans.append(k + 1)
        ans.append(2 * k + 1)
        for i in range(lk, l):
            ans.append(2 ** i)
            
        #State: `ans` is a list containing powers of 2 from \(2^0\) to \(2^{l-1}\); `n` and `k` remain unchanged; `b` remains the binary representation of `n` without the '0b' prefix; `l` remains the length of `b`; `bk` remains the binary representation of `k` without the '0b' prefix; and `lk` remains the length of `bk`.
    #State: *`n` and `k` are the values returned by `func_7()`. `b` remains the binary representation of `n` without the '0b' prefix, and `l` remains the length of `b`. If `k` is 1, `ans` is [2, 3, 4, 8, ..., 2]. Otherwise, `ans` is a list containing powers of 2 from \(2^0\) to \(2^{l-1}\); `bk` remains the binary representation of `k` without the '0b' prefix; and `lk` remains the length of `bk`.
    return str(len(ans)) + '\n' + ' '.join(map(str, ans))
    #The program returns a string that consists of the length of the list `ans` followed by a newline character and then the elements of `ans` separated by spaces. If `k` is 1, `ans` is a list containing the number 2 repeated `l` times, where `l` is the length of the binary representation of `n` without the '0b' prefix. Otherwise, `ans` is a list containing powers of 2 from \(2^0\) to \(2^{l-1}\), where `l` is the length of the binary representation of `n` without the '0b' prefix.
#Overall this is what the function does:The function `func_14` takes no parameters and returns a string. The string returned depends on the values of `n` and `k` obtained from the function `func_7()`. If `k` is 1 and `n` is 2, the function returns the string '1\n2'. Otherwise, it constructs a list `ans` and returns a string that consists of the length of `ans` followed by a newline character and then the elements of `ans` separated by spaces. If `k` is 1, `ans` is a list containing the number 2 repeated `l` times, where `l` is the length of the binary representation of `n` without the '0b' prefix. If `k` is not 1, `ans` is a list containing powers of 2 from \(2^0\) to \(2^{lk-2}\), followed by `k - 1 - sum(ans)`, `k + 1`, `2 * k + 1`, and then powers of 2 from \(2^{lk-1}\) to \(2^{l-1}\), where `l` is the length of the binary representation of `n` and `lk` is the length of the binary representation of `k`.

#State of the program right berfore the function call: This function does not take any parameters, and it relies on the output of `func_10()` and `func_14()` to determine the number of test cases and the sequence for each test case, respectively.
def func_15():
    for _ in range(func_10()):
        sys.stdout.write(str(func_14()) + '\n')
        
    #State: The loop will execute `func_10()` times, and for each iteration, it will write the output of `func_14()` followed by a newline character to the standard output. The state of `func_10()` and `func_14()` remains unchanged, as they are not modified within the loop.
#Overall this is what the function does:The function `func_15` does not accept any parameters. It writes the output of `func_14()` to the standard output, followed by a newline character, for a number of times equal to the value returned by `func_10()`. After the function concludes, the standard output will contain the results of `func_14()` for each test case, each on a new line. The state of `func_10()` and `func_14()` remains unchanged.

