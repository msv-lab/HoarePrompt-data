#State of the program right berfore the function call: No variables in the function signature. The function `func_1` is expected to read an integer from the standard input.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program returns an integer read from the standard input.
#Overall this is what the function does:The function `func_1` reads an integer from the standard input and returns this integer.

#State of the program right berfore the function call: No variables are present in the function signature provided. The function `func_2` reads input from standard input and returns a map object of integers.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object containing integers that were read from standard input, split by whitespace.
#Overall this is what the function does:The function `func_2` reads a line of input from standard input, splits the line into substrings based on whitespace, converts each substring to an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: No variables are defined in the function signature. The function `func_3` is not related to the problem description provided and seems to be a utility function to read integers from standard input.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program returns a list of integers that were read from the standard input, split by whitespace.
#Overall this is what the function does:The function reads a line of input from the standard input, splits it by whitespace, converts each split segment into an integer, and returns a list of these integers.

#State of the program right berfore the function call: rows_number is a positive integer representing the number of test cases.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #The program returns a list of length `rows_number` where each element is the result of calling `func_3()`
#Overall this is what the function does:The function accepts a positive integer `rows_number` and returns a list of length `rows_number`, where each element is the result of calling `func_3()`.

#State of the program right berfore the function call: No variables are present in the function signature of `func_5`. The function does not take any parameters and does not have a defined relationship with the problem variables `n` and `m`.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns a string that is read from the standard input, with any trailing newline characters removed.
#Overall this is what the function does:The function `func_5` reads a line of input from the standard input, removes any trailing newline characters, and returns the resulting string.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program returns a string that is read from standard input, stripped of any trailing newline characters, and decoded from bytes to a string.
#Overall this is what the function does:The function reads a line from standard input, removes any trailing newline characters, decodes it from bytes to a string, and returns the resulting string.

#State of the program right berfore the function call: No variables in the function signature. This function is not directly related to the core logic of solving the problem but might be used to read input values.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers, where each integer is derived from the input string split by spaces.
#Overall this is what the function does:The function `func_7` reads a line of input from the user, splits it by spaces, converts each split segment into an integer, and returns a list of these integers.

#State of the program right berfore the function call: rows is a positive integer representing the number of test cases.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #The program returns a list of results from `func_7()` called `rows` number of times.
#Overall this is what the function does:The function accepts a parameter `rows`, which is a positive integer representing the number of test cases. It returns a list containing the results of calling `func_7()` a total of `rows` number of times.

#State of the program right berfore the function call: The function `func_9` does not take any parameters.
def func_9():
    return input()
    #The program returns the value provided by the user as input.
#Overall this is what the function does:The function `func_9` does not accept any parameters and returns the value provided by the user as input.

#State of the program right berfore the function call: There are no variables in the function signature. The function `func_10` does not take any parameters and is likely to be used to read input for the number of test cases.
def func_10():
    return int(input())
    #The program returns an integer value that is input by the user.
#Overall this is what the function does:The function `func_10` prompts the user to input a value and returns that value as an integer.

#State of the program right berfore the function call: No variables in the function signature. The function `func_11` does not take any parameters and is likely used to read input values from the standard input.
def func_11():
    return input().split()
    #The program returns a list of strings, where each string is a part of the input line split by whitespace.
#Overall this is what the function does:The function `func_11` reads a line of input from the standard input, splits this line into parts based on whitespace, and returns a list of these parts as strings.

#State of the program right berfore the function call: d is a dictionary where each key maps to a list of integers, processing is a list of integers representing a visited state (0 or 1) for each node, da is an integer representing the current node being processed, and rank is a list of integers representing the rank of each node.
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: `d` is a dictionary where each key maps to a list of integers, `processing` is a list of integers representing a visited state (0 or 1) for each node, `da` is an integer representing the current node being processed, `rank` is a list of integers representing the rank of each node, `tmp` is 10, and the length of the list `d[da]` is not equal to 1
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: `d` is a dictionary where each key maps to a list of integers, `processing` is a list of integers representing a visited state (0 or 1) for each node, `da` is an integer representing the current node being processed, `rank` is a list of integers representing the rank of each node, `tmp` is the minimum value returned by `func_12` for all unprocessed nodes in `d[da]`.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns `tmp + 1`, where `tmp` is the minimum value returned by `func_12` for all unprocessed nodes in `d[da]`.
#Overall this is what the function does:The function `func_12` calculates and assigns a rank to each node in a graph represented by the dictionary `d`. It returns 1 if the node `da` has only one neighbor. Otherwise, it recursively processes all unvisited neighbors of `da`, calculates the minimum rank among them, and assigns `tmp + 1` to `rank[da - 1]`, where `tmp` is the minimum rank found among the neighbors. The function modifies the `processing` list to keep track of visited nodes and updates the `rank` list with the calculated ranks.

#State of the program right berfore the function call: a and b are non-negative integers.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns the tuple (1, 0, a) where 1 is the current value of x, 0 is the current value of y, and a is a non-negative integer.
    #State: a and b are non-negative integers, and b is greater than 0
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns `y`, `x - a // b * y`, and `g`.
#Overall this is what the function does:The function `func_13` accepts two non-negative integer parameters `a` and `b`. It calculates and returns a tuple containing three values: the coefficients `y` and `x - a // b * y`, and the greatest common divisor `g` of `a` and `b`. If `b` is zero, it returns the tuple (1, 0, a).

#State of the program right berfore the function call: a is a list of integers, n and m are positive integers such that 0 <= n <= len(a) and m is a positive integer, k is an integer.
def func_14(a, n, m, k):
    for i in range(n):
        if a[i] < m:
            k -= m - a[i]
        
    #State: a is a list of integers, n and m are positive integers such that 0 <= n <= len(a) and m is a positive integer, k is an integer decremented by the sum of (m - a[i]) for all i where a[i] < m and 0 <= i < n.
    if (k >= 0) :
        return 1
        #The program returns 1
    #State: a is a list of integers, n and m are positive integers such that 0 <= n <= len(a) and m is a positive integer, k is an integer decremented by the sum of (m - a[i]) for all i where a[i] < m and 0 <= i < n, and k is less than 0
    return -1
    #The program returns -1
#Overall this is what the function does:The function `func_14` takes a list of integers `a`, a positive integer `n` such that 0 <= n <= len(a), a positive integer `m`, and an integer `k`. It returns 1 if the integer `k` is non-negative after decrementing it by the sum of `(m - a[i])` for all `i` where `a[i] < m` and `0 <= i < n`. Otherwise, it returns -1.

