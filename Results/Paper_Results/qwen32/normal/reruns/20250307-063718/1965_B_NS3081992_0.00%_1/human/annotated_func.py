#State of the program right berfore the function call: No variables are provided in the function signature, so there is no precondition based on the function signature alone.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns an integer that is read from the standard input buffer.
#Overall this is what the function does:The function `func_1` reads an integer from the standard input buffer and returns it.

#State of the program right berfore the function call: The function `func_2` does not have any parameters. It reads a line from the standard input, splits it into components, converts each component to an integer, and returns these integers as a map object.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object containing integers that were obtained by reading a line from the standard input, splitting it into components, and converting each component to an integer.
#Overall this is what the function does:The function reads a line from the standard input, splits it into components, converts each component to an integer, and returns these integers as a map object.

#State of the program right berfore the function call: No specific variables are mentioned in the function signature, but based on the context, the function `func_3` is expected to read from standard input and return a list of integers. It is assumed that the input consists of a line of space-separated integers.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of integers that were provided as a space-separated string in the standard input.
#Overall this is what the function does:The function reads a line of space-separated integers from the standard input and returns them as a list of integers.

#State of the program right berfore the function call: rows_number is a positive integer representing the number of rows or test cases.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #The program returns a list containing the result of `func_3()` called `rows_number` times.
#Overall this is what the function does:The function accepts a positive integer `rows_number` and returns a list containing the result of `func_3()` called `rows_number` times.

#State of the program right berfore the function call: The function `func_5` does not have any parameters, and it returns a byte string representing a line read from standard input, with trailing whitespace removed.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns a byte string representing a line read from standard input, with trailing whitespace removed.
#Overall this is what the function does:The function `func_5` reads a line from standard input, returns it as a byte string, and removes any trailing whitespace.

#State of the program right berfore the function call: This function does not take any parameters and does not return any value. It reads a line from the standard input, removes any trailing whitespace, and decodes it from bytes to a string.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a string that is the result of reading a line from the standard input, removing any trailing whitespace, and decoding it from bytes to a string.
#Overall this is what the function does:The function reads a line from the standard input, removes any trailing whitespace, decodes it from bytes to a string, and returns the resulting string.

#State of the program right berfore the function call: The function `func_7` does not have any parameters. It reads a line of input from the standard input, splits it into a list of strings, converts each string to an integer, and returns the list of integers.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers that are converted from a line of input which is split into a list of strings.
#Overall this is what the function does:The function reads a line of input from the standard input, splits it into a list of strings, converts each string to an integer, and returns the list of integers.

#State of the program right berfore the function call: rows is a positive integer representing the number of test cases.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #The program returns a list with 'rows' number of elements, where each element is the result of a call to the function `func_7()`.
#Overall this is what the function does:The function accepts a positive integer `rows` representing the number of test cases and returns a list containing `rows` number of elements, where each element is the result of a call to the function `func_7()`.

#State of the program right berfore the function call: The function `func_9` does not have any parameters, as indicated by the empty parentheses in the function signature. Therefore, there are no variables to describe in terms of their values or relationships.
def func_9():
    return input()
    #The program returns the value provided by the user input.
#Overall this is what the function does:The function `func_9` prompts the user for input and returns the value provided by the user.

#State of the program right berfore the function call: This function does not have any parameters. It implicitly reads an integer from the input, which represents the number of test cases (t) and is expected to be between 1 and 1000 inclusive.
def func_10():
    return int(input())
    #The program returns an integer between 1 and 1000 inclusive, which represents the number of test cases.
#Overall this is what the function does:The function `func_10` reads an integer from the input, which represents the number of test cases, and returns this integer. The returned integer is guaranteed to be between 1 and 1000 inclusive.

#State of the program right berfore the function call: No variables in the function signature. The function `func_11` does not have any parameters, so there are no preconditions related to variables.
def func_11():
    return input().split()
    #The program returns a list of strings that are the words from the input provided by the user, split by whitespace.
#Overall this is what the function does:The function `func_11` prompts the user for input, splits the input string by whitespace, and returns a list of the resulting words.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers, processing is a list of integers, da is an integer, and rank is a list of integers.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: `d` is a dictionary where keys are integers and values are lists of integers, `processing` is a list of integers, `da` is an integer, `rank` is a list of integers, `tmp` is 1,000,000,000. The length of `d[da]` is not equal to 1.
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: `d` is unchanged, `processing` has all elements corresponding to indices in `d[da]` reset to 0, `da` is unchanged, `rank` is unchanged, `tmp` holds the minimum value returned by `func_12` for all processed elements in `d[da]`.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns `tmp + 1`, where `tmp` holds the minimum value returned by `func_12` for all processed elements in `d[da]`.
#Overall this is what the function does:The function `func_12` processes a dictionary `d` and a list `processing` to determine a value based on the structure of `d` and the state of `processing`. It returns `1` if the list associated with the key `da` in `d` contains only one element. Otherwise, it recursively processes each element in `d[da]`, updating the `processing` list and calculating a minimum value `tmp`. Finally, it sets `rank[da - 1]` to `tmp + 1` and returns this value.

#State of the program right berfore the function call: a and b are integers, where a is the dividend and b is the divisor in the context of the Extended Euclidean Algorithm.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns (1, 0, a)
    #State: *a and b are integers, where a is the dividend and b is the divisor in the context of the Extended Euclidean Algorithm. b is not equal to 0
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns (y, x - a // b * y, g)
#Overall this is what the function does:The function `func_13` computes the greatest common divisor (GCD) of two integers `a` and `b` using the Extended Euclidean Algorithm. It returns a tuple containing the coefficients `x` and `y` such that `ax + by = GCD(a, b)`, along with the GCD itself. If `b` is 0, it returns `(1, 0, a)`. Otherwise, it returns the coefficients and the GCD as determined by the algorithm.

#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n.
def func_14():
    n, k = func_7()
    b = bin(n)[2:]
    l = len(b)
    if (k == 1) :
        if (n == 2) :
            return '1\n2'
            #The program returns the string '1\n2'
        #State: `n` and `k` are integers returned by `func_7()`, where `2 <= n <= 10^6` and `k` is equal to 1; `b` is the binary string representation of `n` without the '0b' prefix; `l` is the length of the binary string `b`. Additionally, `n` is not equal to 2.
        ans = [2, 3]
        for i in range(2, l):
            ans.append(2 ** i)
            
        #State: [2, 3, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]
    else :
        bk = bin(k)[2:]
        ans = []
        lk = len(bk)
        for i in range(lk - 1):
            ans.append(2 ** i)
            
        #State: `n` and `k` are integers returned by `func_7()` where `2 <= n <= 10^6` and `1 < k <= n`; `b` is the binary string representation of `n` without the '0b' prefix; `l` is the length of the binary string `b`; `bk` is the binary string representation of `k` without the '0b' prefix; `lk` is the length of the binary string `bk`; `ans` is `[1, 2, 4, ..., 2
        ans.append(k - 1 - sum(ans))
        ans.append(k + 1)
        ans.append(2 * k + 1)
        for i in range(lk, l):
            ans.append(2 ** i)
            
        #State: [1, 2, 4, ..., 2^(log2(k-1)), k - 1 - sum([1, 2, 4, ..., 2^(log2(k-1))]), k + 1, 2 * k + 1, 2^lk, 2^(lk+1), ..., 2^(l-1)]
    #State: `n` and `k` are integers returned by `func_7()`, where `2 <= n <= 10^6` and `1 <= k <= n`; `b` is the binary string representation of `n` without the '0b' prefix; `l` is the length of the binary string `b`. If `k == 1`, the program does not modify `n` or `k`. Otherwise, `k` is updated to a sequence starting from 1, including powers of 2 up to `2^(log2(k-1))`, followed by `k - 1 - sum([1, 2, 4, ..., 2^(log2(k-1))])`, then `k + 1`, `2 * k + 1`, and powers of 2 from `2^lk` to `2^(l-1)`.
    return ' '.join(map(str, ans))
    #The program returns a space-separated string of the sequence 'ans' which is derived based on the transformations applied to 'k' as described.
#Overall this is what the function does:The function `func_14` generates and returns a string based on the values of two integers `n` and `k` obtained from `func_7()`. If `k` is 1 and `n` is 2, it returns the string '1\n2'. Otherwise, it constructs a sequence of integers derived from transformations involving powers of 2 and specific arithmetic operations on `k`, and returns this sequence as a space-separated string.

#State of the program right berfore the function call: No variables are present in the function signature of `func_15()`.
def func_15():
    for _ in range(func_10()):
        sys.stdout.write(str(func_14()) + '\n')
        
    #State: The value returned by `func_14()` printed `func_10()` times, each on a new line.
#Overall this is what the function does:The function `func_15` does not accept any parameters. It prints the value returned by `func_14()` to the standard output, `func_10()` times, each on a new line.

