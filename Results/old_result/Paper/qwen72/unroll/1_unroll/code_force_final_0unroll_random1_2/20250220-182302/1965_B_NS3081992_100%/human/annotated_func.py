#State of the program right berfore the function call: None. This function does not take any parameters and is used to read an integer from standard input.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns an integer read from standard input.
#Overall this is what the function does:The function reads an integer from standard input and returns it. The function does not take any parameters. After the function concludes, the program has read one line from the standard input and converted it to an integer, which is then returned.

#State of the program right berfore the function call: None. This function does not take any parameters and is used to read input from stdin, which is expected to be a line of space-separated integers.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns an iterator that converts each space-separated integer from the input line into an integer.
#Overall this is what the function does:The function `func_2` reads a line of space-separated integers from standard input (stdin) and returns an iterator that yields each integer in the line. The function does not take any parameters and does not modify any external state. After the function concludes, the user can iterate over the returned iterator to access the integers.

#State of the program right berfore the function call: This function does not take any parameters and is used to read a line of input that contains integers. The input is expected to be a space-separated list of integers.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of integers, where each integer is derived from a space-separated value in the input line.
#Overall this is what the function does:Reads a line of input containing a space-separated list of integers and returns a list of integers.

#State of the program right berfore the function call: rows_number is a non-negative integer.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #The program returns a list containing `rows_number` elements, where each element is the result of calling `func_3()`.
#Overall this is what the function does:The function `func_4` accepts a non-negative integer `rows_number` and returns a list containing `rows_number` elements, where each element is the result of calling `func_3()`. If `rows_number` is 0, the function returns an empty list.

#State of the program right berfore the function call: None of the variables in the function signature are used; the function reads a line from standard input and returns it after stripping trailing whitespace.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns a line read from standard input after stripping any trailing whitespace.
#Overall this is what the function does:The function reads a line from standard input and returns it after removing any trailing whitespace.

#State of the program right berfore the function call: None of the variables in the function signature are used. The function reads a single line from standard input, decodes it, and returns the result.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a string that is the result of reading a single line from standard input, removing trailing whitespace, and decoding it.
#Overall this is what the function does:The function `func_6` does not accept any parameters. It reads a single line from standard input, removes any trailing whitespace, decodes it from bytes to a string, and returns the resulting string. The function does not modify any external variables or state.

#State of the program right berfore the function call: None. The function `func_7` does not take any parameters and is used to read input, which is assumed to be a line of space-separated integers.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers, where each integer is derived from the space-separated integers provided as input.
#Overall this is what the function does:The function `func_7` reads a line of input from the user, which is expected to be a sequence of space-separated integers, and returns a list of integers. The function does not take any parameters and does not modify any external state. After the function concludes, the program has a list of integers derived from the input.

#State of the program right berfore the function call: rows is a non-negative integer.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #The program returns a list of length `rows`, where each element is the result of calling `func_7()`.
#Overall this is what the function does:The function `func_8` accepts a non-negative integer `rows` and returns a list of length `rows`, where each element in the list is the result of calling `func_7()`. The function does not modify any external state or variables.

#State of the program right berfore the function call: None of the variables are used in the function signature. The function is designed to read input, presumably for the values of n and k, but does not specify or validate these inputs within the function itself.
def func_9():
    return input()
    #The program returns the input provided by the user.
#Overall this is what the function does:The function `func_9` reads a line of input from the user and returns it as a string. The function does not accept any parameters and does not modify any external variables. After the function concludes, the program has the user's input available as the return value of the function.

#State of the program right berfore the function call: None. This function does not take any parameters and is used to read an integer from the input, likely representing the number of test cases.
def func_10():
    return int(input())
    #The program returns an integer value that is input by the user, likely representing the number of test cases.
#Overall this is what the function does:The function `func_10` does not accept any parameters. It reads an integer value from the user input and returns this integer value. The function is typically used to obtain the number of test cases or similar integer inputs from the user. The final state of the program after the function concludes is that it has an integer value that was provided by the user.

#State of the program right berfore the function call: None. This function does not take any parameters and is used to read input, which is not directly related to the variables n and k.
def func_11():
    return input().split()
    #The program returns a list of strings, where each string is a part of the input provided by the user, split by whitespace.
#Overall this is what the function does:The function `func_11` does not accept any parameters. It reads input from the user and returns a list of strings, where each string is a part of the input split by whitespace. The function does not modify any external state or variables. After the function concludes, the user's input is split into a list of strings, and this list is the final output of the function.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers, processing is a list of integers of length at least max(da, max(d[da])) initialized to 0, da is an integer key present in d, rank is a list of integers of length at least max(da, max(d[da])) initialized to 0.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1.
    #State: `d` is a dictionary where keys are integers and values are lists of integers, `processing` is a list of integers of length at least max(`da`, max(`d[da]`)) initialized to 0, `da` is an integer key present in `d`, `rank` is a list of integers of length at least max(`da`, max(`d[da]`)) initialized to 0, `tmp` is 1000000000, and the length of `d[da]` is not equal to 1.
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: `processing` is a list of integers of length at least max(`da`, max(`d[da]`)) with the elements at indices `di - 1` for each `di` in `d[da]` temporarily set to 1 during the loop and then reset to 0, `rank` remains a list of integers of length at least max(`da`, max(`d[da]`)) initialized to 0, `tmp` is the minimum value of `func_12(d, processing, di, rank)` for each `di` in `d[da]` where `processing[di - 1]` was 0, and `d` and `da` remain unchanged.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns the value of `tmp + 1`, where `tmp` is the minimum value of `func_12(d, processing, di, rank)` for each `di` in `d[da]` where `processing[di - 1]` was 0, and `rank[da - 1]` is set to `tmp + 1`.
#Overall this is what the function does:The function `func_12` accepts a dictionary `d` with integer keys and lists of integers as values, a list `processing` initialized to 0, an integer key `da` present in `d`, and a list `rank` initialized to 0. It returns `1` if the list `d[da]` contains exactly one element. Otherwise, it recursively processes each element in `d[da]` that has not been processed yet (as indicated by `processing`), and returns the minimum value of these recursive calls plus 1. Additionally, it updates `rank[da - 1]` to this minimum value plus 1. The lists `processing` and `rank` are modified during the function's execution, but `d` and `da` remain unchanged.

#State of the program right berfore the function call: a and b are non-negative integers, and b is not zero.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns (1, 0, a), where 'a' is a non-negative integer.
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns a tuple containing the value `y` (which is the second value returned by `func_13(b, a % b)`), the value `x - a // b * y` (where `x` is the first value returned by `func_13(b, a % b)` and `a // b` is the integer division of `a` by `b`), and the value `g` (which is the third value returned by `func_13(b, a % b)`).
#Overall this is what the function does:The function `func_13` accepts two non-negative integers `a` and `b` (where `b` is not zero) and returns a tuple `(x, y, g)`. If `b` is 0, the function returns `(1, 0, a)`. Otherwise, it recursively calls itself with `b` and `a % b` and returns a tuple containing the second value from the recursive call, the result of `x - a // b * y` (where `x` and `y` are the first and second values from the recursive call, respectively), and the third value from the recursive call. The final state of the program after the function concludes is that it has computed and returned the tuple `(x, y, g)`, which represents the coefficients and the greatest common divisor (GCD) of `a` and `b` in the context of the Extended Euclidean Algorithm.

#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n.
def func_14():
    n, k = func_7()
    b = bin(n)[2:]
    l = len(b)
    if (k == 1) :
        if (n == 2) :
            return '1\n2'
            #The program returns the string '1\n2'.
        #State: *`n` and `k` are integers such that 2 <= n <= 10^6 and 1 <= k <= n, `b` is the binary representation of `n` as a string without the '0b' prefix, `l` is the length of the string `b`, and the current value of `k` is 1. Additionally, `n` is not equal to 2.
        ans = [2, 3]
        for i in range(2, l):
            ans.append(2 ** i)
            
        #State: `n` and `k` remain unchanged, `b` is the binary representation of `n` as a string without the '0b' prefix, `l` is the length of the string `b`, `ans` is [2, 3, 4, 8, 16, 32, 64, 128, 256, 512, ...] (up to 2
    else :
        bk = bin(k)[2:]
        ans = []
        lk = len(bk)
        for i in range(lk - 1):
            ans.append(2 ** i)
            
        #State: `n` and `k` remain unchanged, `b` is the binary representation of `n` as a string without the '0b' prefix, `l` is the length of the string `b`, `bk` is the binary representation of `k` as a string without the '0b' prefix, `ans` is a list containing the powers of 2 from 2^0 to 2^(lk-2), `lk` is the length of the string `bk`.
        ans.append(k - 1 - sum(ans))
        ans.append(k + 1)
        ans.append(2 * k + 1)
        for i in range(lk, l):
            ans.append(2 ** i)
            
        #State: `n` and `k` remain unchanged, `b` is the binary representation of `n` as a string without the '0b' prefix, `l` is the length of the string `b`, `bk` is the binary representation of `k` as a string without the '0b' prefix, `lk` is the length of the string `bk`, `ans` is a list containing the powers of 2 from 2^0 to 2^(lk-2) followed by the value `k - 1 - sum(ans)`, and then `k + 1`, `2 * k + 1`, and the powers of 2 from 2^lk to 2^(l-1).
    #State: `n` and `k` remain unchanged, `b` is the binary representation of `n` as a string without the '0b' prefix, `l` is the length of the string `b`. If `k == 1`, `ans` is a list containing the powers of 2 from 2 to 512 (up to 2^9). Otherwise, `ans` is a list containing the powers of 2 from 2^0 to 2^(lk-2) followed by the value `k - 1 - sum(ans)`, and then `k + 1`, `2 * k + 1`, and the powers of 2 from 2^lk to 2^(l-1), where `bk` is the binary representation of `k` as a string without the '0b' prefix and `lk` is the length of the string `bk`.
    return str(len(ans)) + '\n' + ' '.join(map(str, ans))
    #The program returns a string that consists of the length of the list `ans` followed by a newline and then the elements of `ans` separated by spaces. The length of `ans` and the elements in `ans` depend on the value of `k` and the binary representation of `n` and `k`. If `k == 1`, `ans` contains the powers of 2 from 2 to 512 (up to 2^9), resulting in a list of 10 elements. Otherwise, `ans` contains the powers of 2 from 2^0 to 2^(lk-2), followed by `k - 1 - sum(ans)`, and then `k + 1`, `2 * k + 1`, and the powers of 2 from 2^lk to 2^(l-1), where `lk` is the length of the binary representation of `k` without the '0b' prefix.
#Overall this is what the function does:The function `func_14` takes no parameters and returns a string. It internally uses the values of `n` and `k` obtained from the function `func_7` where `n` and `k` are integers such that 2 <= n <= 10^6 and 1 <= k <= n. If `k` is 1 and `n` is 2, the function returns the string '1\n2'. If `k` is 1 and `n` is not 2, the function returns a string containing the length of a list `ans` followed by a newline and then the elements of `ans` separated by spaces, where `ans` is a list of the powers of 2 from 2 to 512 (up to 2^9), resulting in a list of 10 elements. If `k` is not 1, the function returns a string containing the length of a list `ans` followed by a newline and then the elements of `ans` separated by spaces, where `ans` is a list containing the powers of 2 from 2^0 to 2^(lk-2), followed by the value `k - 1 - sum(ans)`, and then `k + 1`, `2 * k + 1`, and the powers of 2 from 2^lk to 2^(l-1), where `lk` is the length of the binary representation of `k` without the '0b' prefix and `l` is the length of the binary representation of `n` without the '0b' prefix.

#State of the program right berfore the function call: None of the variables are used in the function signature.
def func_15():
    for _ in range(func_10()):
        sys.stdout.write(str(func_14()) + '\n')
        
    #State: The loop will print the value returned by `func_14()` `n` times, each on a new line.
#Overall this is what the function does:The function `func_15` does not accept any parameters. It prints the value returned by `func_14` a number of times equal to the value returned by `func_10`, each value on a new line. The function does not return any specific value.

