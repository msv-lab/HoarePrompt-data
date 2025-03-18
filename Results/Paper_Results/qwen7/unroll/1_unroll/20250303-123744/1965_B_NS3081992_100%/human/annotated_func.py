#State of the program right berfore the function call: None of the variables in the function signature are provided in the given code snippet. The function `func_1` does not take any arguments.
def func_1():
    return int(sys.stdin.buffer.readline())
    #The program reads an integer from standard input and returns it.
#Overall this is what the function does:The function reads an integer from standard input and returns it.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are integers satisfying 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n.
def func_2():
    return map(int, sys.stdin.buffer.readline().split())
    #The program returns a map object containing integers read from the standard input buffer, split by spaces.
#Overall this is what the function does:The function reads integers from the standard input buffer, splits them by spaces, and returns a map object containing these integers. This process is performed without requiring any input parameters.

#State of the program right berfore the function call: None of the variables `t`, `n`, and `k` are mentioned in the provided function signature. However, based on the problem description, `t` is the number of test cases, and for each test case, `n` and `k` are the parameters described in the problem statement.
def func_3():
    return list(map(int, sys.stdin.buffer.readline().split()))
    #The program reads a line from standard input, splits it into individual strings, converts each string to an integer, and returns a list of these integers.
#Overall this is what the function does:The function reads a line from standard input, splits it into individual strings, converts each string to an integer, and returns a list of these integers.

#State of the program right berfore the function call: rows_number is an integer such that 1 <= rows_number <= 25.
def func_4(rows_number):
    return [func_3() for _ in range(rows_number)]
    #A list of length `rows_number` containing the results of calling `func_3()` for each element in the range from 0 to `rows_number - 1`
#Overall this is what the function does:The function accepts an integer `rows_number` between 1 and 25 and returns a list of length `rows_number`. Each element in the list is the result of calling `func_3()` with the corresponding index from 0 to `rows_number - 1`.

#State of the program right berfore the function call: None of the variables in the provided function signature match those in the problem description. The function `func_5()` reads a line from standard input, but it does not take any parameters related to the problem, such as `t`, `n`, or `k`.
def func_5():
    return sys.stdin.buffer.readline().rstrip()
    #The program returns a line read from standard input and stripped of trailing whitespace.
#Overall this is what the function does:The function reads a line from standard input and returns it with trailing whitespace removed.

#State of the program right berfore the function call: None of the variables in the function signature are provided in the given code snippet. The function does not take any parameters.
def func_6():
    return sys.stdin.buffer.readline().rstrip().decode()
    #The program reads a line from standard input, removes the trailing newline character, and decodes it from bytes to a string before returning it.
#Overall this is what the function does:Functionality: The function reads a line from standard input, removes the trailing newline character, and decodes it from bytes to a string before returning it.

#State of the program right berfore the function call: None of the variables in the function signature are provided in the given program. The function `func_7()` does not take any parameters and its purpose seems to be reading input, which is typically done outside of the function body in the main program flow. However, based on the problem description and the context, it's implied that the function might be part of a larger solution and is expected to read two integers `t` and `n` from the input, where `t` is the number of test cases and for each test case, `n` and `k` are read.
def func_7():
    return [int(i) for i in input().split()]
    #The program returns a list of integers obtained by splitting the input string and converting each element to an integer.
#Overall this is what the function does:The function reads multiple integers from the input, specifically the number of test cases `t`, followed by pairs of integers `n` and `k` for each test case, and returns them as a list of integers.

#State of the program right berfore the function call: rows is a positive integer such that 1 <= rows <= 25.
def func_8(rows):
    return [func_7() for _ in range(rows)]
    #The program returns a list of length rows, where each element in the list is the result of calling func_7()
#Overall this is what the function does:The function `func_8` accepts a positive integer `rows` (with a constraint of 1 <= rows <= 25) and returns a list containing `rows` elements. Each element in the list is the result of calling another function `func_7`.

#State of the program right berfore the function call: This function does not take any parameters and it is not clear how it relates to the problem description. It seems to be returning input from the user, which is not used in the provided code snippet.
def func_9():
    return input()
    #The program returns the input provided by the user.
#Overall this is what the function does:The function `func_9` does not accept any parameters and returns the input provided by the user.

#State of the program right berfore the function call: None of the variables in the function signature are provided in the given code snippet. The function does not take any parameters.
def func_10():
    return int(input())
    #The program returns an integer input provided by the user.
#Overall this is what the function does:The function prompts the user to provide an integer input and returns this integer.

#State of the program right berfore the function call: None of the variables in the function signature are provided in the given program. The function does not take any arguments.
def func_11():
    return input().split()
    #The program returns a list of strings obtained by splitting the user input at the default delimiter (space)
#Overall this is what the function does:The function accepts no parameters and returns a list of strings obtained by splitting the user input at the default delimiter (space).

#State of the program right berfore the function call: d is a dictionary where keys are integers and values are lists of integers; processing is a list of zeros and ones with the same length as the maximum value in d (inclusive); da is an integer representing a key in the dictionary d; rank is a list of integers with the same length as the maximum key in d (inclusive).
def func_12(d, processing, da, rank):
    tmp = 10 ** 9
    if (len(d[da]) == 1) :
        return 1
        #The program returns 1
    #State: Postcondition: `tmp` is 1000000000, `d` is a dictionary where keys are integers and values are lists of integers; `processing` is a list of zeros and ones with the same length as the maximum value in `d` (inclusive); `da` is an integer representing a key in the dictionary `d`; `rank` is a list of integers with the same length as the maximum key in `d` (inclusive). The length of `d[da]` is not equal to 1.
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, func_12(d, processing, di, rank))
            processing[di - 1] = 0
        
    #State: `tmp` is the minimum value obtained from `func_12(d, processing, di, rank)` for each `di` in `d[da]` where `processing[di - 1]` was initially 0, `d` remains unchanged, `processing` is modified such that for each `di` in `d[da]`, if `processing[di - 1]` was 0, it is set to 1 and then back to 0, `da` remains unchanged, `rank` remains unchanged.
    rank[da - 1] = tmp + 1
    return tmp + 1
    #The program returns the value of `tmp` incremented by 1, where `tmp` is the minimum value obtained from `func_12(d, processing, di, rank)` for each `di` in `d[da]` where `processing[di - 1]` was initially 0.
#Overall this is what the function does:The function accepts a dictionary `d` where keys are integers and values are lists of integers, a list `processing` of zeros and ones with the same length as the maximum value in `d` (inclusive), an integer `da` representing a key in the dictionary `d`, and a list `rank` of integers with the same length as the maximum key in `d` (inclusive). If the length of `d[da]` is 1, the function returns 1. Otherwise, it recursively processes each element `di` in `d[da]` where `processing[di - 1]` is initially 0, updating `processing` and `tmp` accordingly. Finally, it sets `rank[da - 1]` to `tmp + 1` and returns this value.

#State of the program right berfore the function call: a and b are non-negative integers such that b != 0.
def func_13(a, b):
    if (b == 0) :
        x = 1
        y = 0
        return x, y, a
        #The program returns 1 as x, 0 as y, and a as a non-negative integer.
    #State: a and b are non-negative integers such that b is not equal to 0
    x, y, g = func_13(b, a % b)
    return y, x - a // b * y, g
    #The program returns y, x - a // b * y, g
#Overall this is what the function does:The function `func_13` accepts two non-negative integers `a` and `b` (with `b` not equal to 0) and returns a tuple of three values. If `b` is 0, it returns `(1, 0, a)`. Otherwise, it recursively calculates and returns `(y, x - a // b * y, g)` using the Extended Euclidean Algorithm, which finds integers `x` and `y` such that `ax + by = gcd(a, b)`, where `gcd(a, b)` is the greatest common divisor of `a` and `b`.

#State of the program right berfore the function call: (n, k) are integers such that 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n.
def func_14():
    n, k = func_7()
    b = bin(n)[2:]
    l = len(b)
    if (k == 1) :
        if (n == 2) :
            return '1\n2'
            #The program returns the string '1\n2'
        #State: `b` is the binary representation of `n` without the '0b' prefix, `k` is 1, `l` is the length of `b`, `k` is the second return value of `func_7()`, and `n` is not equal to 2
        ans = [2, 3]
        for i in range(2, l):
            ans.append(2 ** i)
            
        #State: Output State: `ans` is `[2, 3, 4, 8]`, `k` is 1, `l` is 4, `n` is not equal to 2.
        #
        #Explanation: The loop starts with `i` being 2 and runs until `i` is less than `l`. Given `l` is the length of `b`, and initially `ans` is `[2, 3]`, we can infer that `l` is initially 2 (since the length of `[2, 3]` is 2). However, the loop starts from `i = 2` and goes up to `l - 1`, so it will run once for `i = 2` and once for `i = 3`, appending `2 ** 2 = 4` and `2 ** 3 = 8` to `ans`. After the loop, `ans` becomes `[2, 3, 4, 8]`, `k` remains 1, `l` is now 4 (since we appended two more elements to `ans`), and `n` remains not equal to 2.
    else :
        bk = bin(k)[2:]
        ans = []
        lk = len(bk)
        for i in range(lk - 1):
            ans.append(2 ** i)
            
        #State: ans is [1, 2, 4].
        ans.append(k - 1 - sum(ans))
        ans.append(k + 1)
        ans.append(2 * k + 1)
        for i in range(lk, l):
            ans.append(2 ** i)
            
        #State: ans is [1, 2, 4, 2, k + 1, 2 * k + 1, 2
    #State: `ans` is a list containing the powers of 2, starting from \(2^2\) up to \(2^{l-1}\), where \(l\) is the length of the binary representation `b` of `n`. `k` is either 1 or `k + 1`, and `n` is not equal to 2.
    return str(len(ans)) + '\n' + ' '.join(map(str, ans))
    #The program returns the length of the list `ans` as a string followed by a newline character, then the elements of `ans` joined by spaces.
#Overall this is what the function does:The function does not accept any parameters and returns either the string '1\n2' or a string representing the length of the list `ans` followed by the elements of `ans` joined by spaces. If `k` is 1 and `n` is not 2, it returns '1\n2'. Otherwise, it constructs a list `ans` containing specific values based on the binary representation of `n` and the value of `k`, and then returns the length of this list along with its elements formatted as described.

#State of the program right berfore the function call: There is no integer `k` such that `1 <= k <= 10^6` and the sum of any subsequence of `a` equals `k`. For all integers `v` in the range `1 <= v <= n` where `v != k`, there exists a subsequence of `a` whose sum equals `v`. The length of the sequence `a` is at most 25.
def func_15():
    for _ in range(func_10()):
        sys.stdout.write(str(func_14()) + '\n')
        
    #State: Output State: The output state consists of the numbers printed by `func_14()` for each iteration of the loop, with each number written on a new line. The total number of lines will be equal to the return value of `func_10()`. Each number printed is determined by the implementation of `func_14()`. Since the exact behavior of `func_10()` and `func_14()` is not specified, the specific numbers cannot be determined, but they will form a sequence of integers based on the function definitions.
#Overall this is what the function does:The function does not accept any parameters and does not return any value. Instead, it prints a sequence of integers to the standard output. The number of integers printed is determined by the return value of `func_10()`, and each integer is generated by calling `func_14()`. The specific values printed depend on the implementations of `func_10()` and `func_14()`, but they form a sequence of integers.

