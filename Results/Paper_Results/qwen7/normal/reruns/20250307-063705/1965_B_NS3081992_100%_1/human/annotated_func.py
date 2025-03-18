#State of the program right berfore the function call: None of the variables in the function `func_1()` are mentioned in the problem description, and the function does not take any arguments. It reads an integer from standard input (stdin) and returns it.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program reads an integer from standard input (stdin) and returns it.
#Overall this is what the function does:The function reads an integer from standard input (stdin) and returns it.

#State of the program right berfore the function call: None of the variables `t`, `n`, and `k` are mentioned in the provided function signature. However, based on the problem description, `t` is the number of test cases, and for each test case, `n` and `k` are the parameters described in the problem statement.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object containing integers read from the standard input buffer, split by spaces.
#Overall this is what the function does:The function reads a line of input from the standard input buffer, splits it into individual elements based on spaces, and converts these elements into integers. It then returns a map object containing these integer values.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, n and k are integers satisfying 2 <= n <= 10^6 and 1 <= k <= n.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of two integers, where the first integer is n (satisfying 2 <= n <= 10^6) and the second integer is k (satisfying 1 <= k <= n).
#Overall this is what the function does:The function reads two integers from standard input, converts them to a list of integers, and returns this list. The first integer in the list represents n (with 2 <= n <= 10^6), and the second integer represents k (with 1 <= k <= n).

#State of the program right berfore the function call: rows_number is a positive integer such that 1 <= rows_number <= 25.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #A list containing the result of `func_3()` called `rows_number` times
#Overall this is what the function does:The function accepts a positive integer `rows_number` (between 1 and 25) and returns a list. This list contains the result of calling another function `func_3()` exactly `rows_number` times.

#State of the program right berfore the function call: None of the variables in the provided function signature are present in the given code snippet. The function `func_5` reads a single line from standard input, strips the trailing newline character, and returns it as bytes. However, since the problem description and the function do not directly relate to the sequence generation requirements, there are no specific preconditions related to the function's input variables.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program reads a single line from standard input, removes the trailing newline character, and returns it as bytes.
#Overall this is what the function does:The function `func_5` reads a single line from standard input, removes the trailing newline character, and returns it as bytes.

#State of the program right berfore the function call: None of the variables in the function signature are provided in the given program. The function does not take any parameters and its purpose seems to read a line from standard input, strip trailing whitespace, and decode it from bytes to a string.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program reads a line from standard input, strips trailing whitespace, and decodes it from bytes to a string before returning it.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing whitespace, and converts the line from bytes to a string before returning it.

#State of the program right berfore the function call: None of the variables in the function signature are used within the provided code snippet. The function `func_7()` does not take any arguments and its purpose seems to be reading input, but it does not define any variables or use any variables passed to it.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers obtained by splitting the input string on spaces and converting each element to an integer.
#Overall this is what the function does:The function `func_7()` reads a space-separated string of integers from the user input, splits it into individual elements, converts each element to an integer, and returns a list of these integers.

#State of the program right berfore the function call: rows is a positive integer such that 1 <= rows <= 25.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #The program returns a list of length 'rows', where each element in the list is the result of calling the function 'func_7()'
#Overall this is what the function does:The function `func_8` accepts a positive integer `rows` (where 1 ≤ rows ≤ 25) and returns a list of length `rows`. Each element in the list is the result of calling another function `func_7()` one time for each element in the range from 0 to `rows-1`.

#State of the program right berfore the function call: None of the variables in the function signature are used within the function, and the function does not take any parameters.
def func_9():
    return input()
    #The program returns the user's input from the `input()` function call
#Overall this is what the function does:The function accepts no parameters and returns the user's input from the `input()` function call.

#State of the program right berfore the function call: None of the variables in the function signature are provided, and the function does not take any arguments. This function simply reads an integer input from the user and returns it.
def func_10():
    return int(input())
    #The program returns an integer input provided by the user.
#Overall this is what the function does:The function reads an integer input from the user and returns it.

#State of the program right berfore the function call: None of the variables in the function signature are provided, and the function does not take any parameters. However, it returns a list of strings obtained by splitting the input from standard input.
def func_11():
    return input().split()
    #The program returns a list of strings obtained by splitting the input received from standard input.
#Overall this is what the function does:The function reads a line of input from the standard input and splits it into a list of strings based on whitespace. It then returns this list of strings.

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers. da is an integer representing a key in the dictionary d. processing is a list of integers of length equal to the maximum possible value in the lists of d, initialized to 0s. rank is a list of integers of length equal to the maximum possible value in the keys of d, initialized to 0s.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: `d` is a dictionary where keys are integers and values are lists of integers, `da` is an integer representing a key in the dictionary `d`, `processing` is a list of integers of length equal to the maximum possible value in the lists of `d`, initialized to 0s, `rank` is a list of integers of length equal to the maximum possible value in the keys of `d`, initialized to 0s, `tmp` is set to 10, and the length of `d[da]` is not equal to 1
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: Output State: `d` is a dictionary where keys are integers and values are lists of integers, `da` is an integer representing a key in the dictionary `d`, `processing` is a list of integers of length equal to the maximum possible value in the lists of `d`, initialized to 0s, `rank` is a list of integers of length equal to the maximum possible value in the keys of `d`, initialized to 0s, `tmp` is updated to the minimum value between its current value and the result of `func_12(d, processing, di, rank)` for each iteration of `di` in `d[da]`, and `d[da]` remains unchanged, with all elements in `d[da]` having been processed.
    #
    #In simpler terms, after the loop has executed all its iterations, `d`, `da`, `processing`, and `rank` will remain as they were initially. However, `tmp` will be updated to the smallest value it achieved during any of the iterations of the loop, where the value is determined by calling `func_12(d, processing, di, rank)` for each `di` in `d[da]`. All elements in `d[da]` will have been processed at least once.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns a value that is `tmp + 1`, where `tmp` is equal to the minimum value between its current value and the result of `func_12(d, processing, di, rank)` for each iteration of `di` in `d[da]`.
#Overall this is what the function does:The function accepts a dictionary `d` where keys are integers and values are lists of integers, an integer `da` representing a key in the dictionary `d`, a list `processing` of integers initialized to 0s, and a list `rank` of integers initialized to 0s. It returns either 1 or a value that is `tmp + 1`, where `tmp` is the minimum value between its current value and the result of recursively calling itself for each element `di` in `d[da]` if `processing[di - 1]` is 0. The function updates the `rank` list based on the computed `tmp` value.

#State of the program right berfore the function call: a and b are non-negative integers such that b != 0.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns x which is 1, y which is 0, and a which is a non-negative integer.
    #State: a and b are non-negative integers such that b is not equal to 0
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns y, x - a // b * y, g
#Overall this is what the function does:The function `func_13` accepts two non-negative integers `a` and `b`, where `b` is not zero. It returns a tuple containing three values. If `b` is zero, it returns `(1, 0, a)`. Otherwise, it recursively computes values `x`, `y`, and `g` and returns `(y, x - a // b * y, g)`.

#State of the program right berfore the function call: (n, k) are integers such that 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n.
def func_14():
    n, k = func_7()
    b = bin(n)[2:]
    l = len(b)
    if (k == 1) :
        if (n == 2) :
            return '1\n2'
            #The program returns the string '1\n2'
        #State: Postcondition: `b` is the binary representation of `n` without the '0b' prefix, `k` is 1, `l` is the length of `b`, and `n` is not equal to 2
        ans = [2, 3]
        for i in range(2, l):
            ans.append(2 ** i)
            
        #State: The list `ans` will contain the elements [2, 3, 2, 16, 32, 128]. The variable `i` will be 6, and `l` will be the length of the binary representation of `n` without the '0b' prefix.
    else :
        bk = bin(k)[2:]
        ans = []
        lk = len(bk)
        for i in range(lk - 1):
            ans.append(2 ** i)
            
        #State: Output State: `i` is equal to `lk - 2`; `ans` contains the list `[1, 2, 4, ..., 2^(lk-2)]`; `lk` is greater than or equal to `lk`.
        #
        #Explanation: The loop runs from `i = 0` to `i = lk - 2`. This means that if `lk` is the length of the binary representation of `k`, then `i` will take on all integer values from `0` to `lk - 2`. Therefore, `i` will be equal to `lk - 2` after the last iteration. Each iteration appends `2^i` to the list `ans`, so `ans` will contain the list `[1, 2, 4, ..., 2^(lk-2)]`. The condition `lk` must be greater than or equal to `lk` is redundant since `lk` cannot be less than itself.
        ans.append(k - 1 - sum(ans))
        ans.append(k + 1)
        ans.append(2 * k + 1)
        for i in range(lk, l):
            ans.append(2 ** i)
            
        #State: Output State: `i` is `lk + (lk - 2)`, `ans` contains the list `[1, 2, 4, ..., 2^(lk-2), k + 1, 2 * k + 1, 2^lk, 2^(lk+1), ..., 2^(2*(lk-2)+lk)]`.
        #
        #In natural language: After the loop has executed all its iterations, the variable `i` will be equal to `lk + (lk - 2)`. The list `ans` will contain the initial elements `[1, 2, 4, ..., 2^(lk-2), k + 1, 2 * k + 1]` followed by additional elements generated by the loop, specifically `2^lk, 2^(lk+1), ..., 2^(2*(lk-2)+lk)`.
    #State: `b` is the binary representation of `n` without the '0b' prefix, `k` is the return value of `func_7()`, `l` is the length of `b`, `i` is `lk + (lk - 2)`, and `ans` contains the list `[1, 2, 4, ..., 2^(lk-2), k + 1, 2 * k + 1]` followed by additional elements generated by the loop, specifically `2^lk, 2^(lk+1), ..., 2^(2*(lk-2)+lk)` if `k == 1`. If `k != 1`, `i` remains 6 and `l` remains the length of the binary representation of `n` without the '0b' prefix.
    return str(len(ans)) + '\n' + ' '.join(map(str, ans))
    #The program returns the length of the list `ans` as a string, followed by the elements of `ans` joined by spaces.
#Overall this is what the function does:The function takes no explicit parameters and returns either the string '1\n2' or a sequence of numbers formatted as a space-separated string. If \( k = 1 \) and \( n = 2 \), it returns '1\n2'. Otherwise, it constructs a list `ans` based on the binary representations of \( n \) and \( k \), and returns the length of this list followed by its elements.

#State of the program right berfore the function call: There is no integer in the output that sums to k, but every integer from 1 to n (excluding k) can be represented as a subsequence sum. The output sequence has a length m such that 1 <= m <= 25.
def func_15():
    for _ in range(func_10()):
        sys.stdout.write(str(func_14()) + '\n')
        
    #State: Output State: The loop will execute `func_10()` times, and each iteration will write a positive integer returned by `func_14()` to the standard output. Since `func_10()` is not specified, we cannot determine the exact number of iterations. However, given that the loop executes 3 times and continues to execute based on `func_10()`, it will continue to write positive integers until `func_10()` iterations are completed.
    #
    #Each written integer is a positive integer, and the loop does not modify any state other than appending these integers to the output. Therefore, the final output state will be a sequence of positive integers, with the total number of integers being equal to the value returned by `func_10()`.
#Overall this is what the function does:The function accepts no parameters and returns a sequence of positive integers. The length of the sequence is determined by the value returned by `func_10()`, which is between 1 and 25. Each integer in the sequence is a positive integer, and the sequence contains no integer that sums to `k`. The function writes each integer in the sequence to the standard output.

