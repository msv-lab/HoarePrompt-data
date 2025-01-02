#State of the program right berfore the function call: T is an integer such that 1 ≤ T ≤ 100, n is an integer such that 2 ≤ n ≤ 10^5, and a is a list of n integers such that 1 ≤ a_i ≤ n. Each bag description contains at least one pair of indices i and j such that 1 ≤ i, j ≤ n and i ≠ j but a_i = a_j.
def func_1():
    return int(input())
    #The program returns an integer input from the user
#Overall this is what the function does:The function `func_1` accepts no parameters and reads an integer input from the user. After executing, the program will return this integer input. There are no preconditions specified for the input other than it being an integer. This function does not perform any validation on the input, so any integer value can be accepted. No additional actions are performed within the function.

#State of the program right berfore the function call: T is an integer representing the number of bags, and for each bag, n is an integer representing the number of patty-cakes in the bag, followed by a list of n integers a_1, a_2, …, a_n representing the fillings of the patty-cakes. It is guaranteed that each bag contains at least two patty-cakes with the same filling, and the sum of n over all bags does not exceed 10^5.
def func_2():
    return float(input())
    #The program returns a float input from the user
#Overall this is what the function does:The function prompts the user to input a floating-point number and returns this value. The function does not use any of the input parameters related to the number of bags or patty-cakes. There are no postconditions mentioned in the code or annotations that would modify these input parameters. This implies that after the function execution, the values of `T`, `n`, and the list of fillings `a` remain unchanged. The function solely interacts with the user to obtain a floating-point input and returns it.

#State of the program right berfore the function call: T is an integer representing the number of bags, n is an integer representing the number of patty-cakes in a bag, and a is a list of integers where each integer represents the filling of a patty-cake (1 ≤ a_i ≤ n).
def func_3():
    return input()
    #The program returns input from the user
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns input from the user. The function's overall behavior is to prompt the user for input and return whatever the user inputs. There are no edge cases or missing functionalities in the provided code since it only contains a single return statement without any preceding code to modify the input or handle different scenarios.

#State of the program right berfore the function call: T is an integer such that 1 ≤ T ≤ 100, and for each bag, n is an integer such that 2 ≤ n ≤ 10^5, and the following n integers represent the fillings of the patty-cakes where each filling is an integer between 1 and n inclusive.
def func_4():
    return map(str, input().split())
    #The program returns a map object of strings split from user input, where each string represents a filling of the patty-cakes
#Overall this is what the function does:The function `func_4()` reads a line of space-separated integers from the user input, splits it into individual strings, and returns a map object containing these strings. Each string represents a filling of the patty-cakes. The function assumes that the input follows the format specified (an integer \(T\) indicating the number of test cases, followed by \(T\) lines, each containing an integer \(n\) indicating the number of patty-cakes, and then \(n\) integers representing the fillings). However, the function does not handle the case where the input does not conform to this format. Specifically, it does not validate the number of test cases \(T\), nor does it validate that the subsequent lines contain the correct number of patty-cake fillings.

#State of the program right berfore the function call: T is an integer such that 1 ≤ T ≤ 100, n is an integer such that 2 ≤ n ≤ 10^5, and the subsequent input lines contain n integers representing the fillings of the patty-cakes, where each integer is between 1 and n inclusive.
def func_5():
    return map(int, input().split())
    #The program returns a map object containing integers entered by the user, split from a single line of input
#Overall this is what the function does:The function `func_5()` reads a single line of space-separated integers from the user input and returns a map object containing these integers. There are no parameters accepted by the function, and the return type is a map object. The function does not modify any external variables; it only processes the input provided by the user. Potential edge cases include the input being empty (though this would raise a `ValueError` when calling `map(int, input().split())`) or the input containing non-integer values (which would also raise a `ValueError`).

#State of the program right berfore the function call: T is a positive integer such that 1 <= T <= 100. Each bag description starts with an integer n representing the number of patty-cakes (2 <= n <= 10^5), followed by a list of n integers a_1, a_2, …, a_n representing the fillings of the patty-cakes (1 <= a_i <= n). It is guaranteed that each bag contains at least two patty-cakes with the same filling and the sum of n over all bags does not exceed 10^5.
def func_6():
    return list(func_5())
    #The program returns a list generated by func_5(), which is not defined in the provided code snippet.
#Overall this is what the function does:- If `func_5()` is not defined or if its implementation is incomplete, the function `func_6()` would raise a `NameError` upon execution.
- The annotation mentions that each bag has at least two patty-cakes with the same filling, but it does not specify how `func_5()` handles the case where multiple bags share the same filling. It is possible that `func_6()` might return a flattened list of all duplicate fillings, or it could handle duplicates differently depending on the implementation of `func_5()`.
- The code does not mention handling the case where a filling appears in more than one bag, but if `func_5()` is expected to find all unique duplicate fillings across all bags, then it should be able to handle this scenario.

#State of the program right berfore the function call: T is an integer representing the number of bags, n is an integer representing the number of patty-cakes in a bag, and a is a list of integers representing the fillings of the patty-cakes where same fillings are represented by the same integers. Additionally, it is guaranteed that each bag contains at least two patty-cakes with the same filling, and the sum of n over all bags does not exceed 10^5.
def func_7():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
#Overall this is what the function does:The function `func_7()` reads input from a file named 'input.txt' and writes output to a file named 'output.txt'. It does not directly process the parameters `T`, `n`, and `a` as described in the annotations; instead, it changes the standard input and output streams. After executing, the program's standard input is redirected to 'input.txt' and standard output is redirected to 'output.txt'. There are no operations performed on the input parameters `T`, `n`, and `a`, and no output is generated based on these parameters. The function does not return any value, and the final state of the program includes the standard input and output streams being redirected to files.

#State of the program right berfore the function call: x and y are positive integers where x >= y, and the function calculates the greatest common divisor (GCD) of x and y using the Euclidean algorithm.
def func_8(x, y):
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: `x` is the GCD of the original values of `x` and `y`, `y` is 0
    return x
    #The program returns x which is the GCD of the original values of x and y, and y which is 0
#Overall this is what the function does:The function `func_8` accepts two parameters `x` and `y`, both positive integers with `x >= y`. It calculates their greatest common divisor (GCD) using the Euclidean algorithm. After the loop terminates, `x` contains the GCD of the original values of `x` and `y`, and `y` is set to 0. The function returns `x` (the GCD) and `y` (which is 0). The function correctly handles the case when `y` becomes 0, which is the termination condition of the loop. There are no apparent missing functionalities or edge cases in the provided code.

#State of the program right berfore the function call: x and y are positive integers.
def func_9(x, y):
    return x * y // func_8(x, y)
    #The program returns x * y // func_8(x, y), where `x` and `y` are positive integers
#Overall this is what the function does:The function `func_9` accepts two parameters `x` and `y`, both positive integers. It returns the result of `x * y` divided by the result of calling `func_8(x, y)`. If `func_8(x, y)` returns zero, the function will raise a `ZeroDivisionError`. There are no explicit edge cases mentioned in the annotations or code, but the function assumes that `func_8(x, y)` will not return zero to avoid division by zero.

#State of the program right berfore the function call: b is an integer representing the base, m is an integer representing the modulus such that b > 1 and m > 1.
def func_10(b, m):
    g = func_8(b, m)
    if (g != 1) :
        return -1
        #The program returns -1
    else :
        return pow(b, m - 2, m)
        #The program returns the value of \( b^{m-2} \mod m \)
#Overall this is what the function does:The function `func_10` accepts two parameters `b` and `m`, where both are integers such that `b > 1` and `m > 1`. It first calls another function `func_8(b, m)` to compute `g`. If `g` is not equal to 1, the function returns `-1`. Otherwise, it computes and returns the value of \( b^{m-2} \mod m \). This function essentially checks if `g` (which is likely a result related to the order of `b` modulo `m`) is 1, and if so, calculates the modular inverse of `b` modulo `m` using Fermat's Little Theorem. The potential edge case is when `g` is not 1, in which case the function returns `-1` instead of performing the modular exponentiation.

#State of the program right berfore the function call: a is an integer, b is an integer, and m is a positive integer such that \(1 \leq a, b < m\).
def func_11(a, b, m):
    a = a % m
    inv = func_10(b, m)
    if (inv == -1) :
        return -999999999
        #The program returns -999999999
    else :
        return inv * a % m
        #`inv * a % m` where `inv` is the result of `func_10(b, m)` and is not equal to -1
#Overall this is what the function does:The function `func_11` accepts three parameters: `a`, `b`, and `m`. It first computes `a % m` and then calls `func_10(b, m)` to get the modular inverse of `b` modulo `m`. If the modular inverse does not exist (i.e., `func_10(b, m)` returns -1), the function returns -999999999. Otherwise, it returns the product of the modular inverse and `a`, taken modulo `m`.

#State of the program right berfore the function call: T is a positive integer representing the number of bags. For each bag, n is a positive integer representing the number of patty-cakes in the bag, and a is a list of n positive integers where each integer represents the filling of a patty-cake. Each bag contains at least two patty-cakes with the same filling, and the sum of n over all bags does not exceed 10^5.
def func_12():
    for _ in range(func_1()):
        n = func_1()
        
        a = func_6()
        
        a.sort(reverse=True)
        
        f = [0] * 100005
        
        for i in range(n):
            f[a[i]] += 1
        
        s = 0
        
        s = max(f)
        
        if s == n:
            func_13(0)
            continue
        
        if f.count(1) == n - s:
            if s == 2:
                ans = n - s
            else:
                ans = (n - 1) // (s + 1)
                ans += 1
            func_13(ans)
            continue
        
        ans = (n - 1) // (s + 1)
        
        ans += 1
        
        func_13(ans)
        
    #State of the program after the  for loop has been executed: 
#Overall this is what the function does:The function processes multiple bags, each containing patty-cakes with various fillings. For each bag, it checks if there are at least two patty-cakes with the same filling. If this condition holds for all bags, the function calls `func_13(True)` and returns `True`. Otherwise, it calculates a value based on the frequency of fillings and calls `func_13()` with this value, returning `False`. The function iterates over all bags, and for each bag, it sorts the fillings in descending order, counts the frequency of each filling, and uses these counts to determine the result.

#State of the program right berfore the function call: T is a positive integer representing the number of bags. For each bag, n is a positive integer representing the number of patty-cakes in the bag, and a list of n positive integers a_1, a_2, ..., a_n where each a_i represents the filling of the i-th patty-cake. It is guaranteed that 2 <= n <= 10^5, each bag contains at least two patty-cakes with the same filling, and the sum of n over all bags does not exceed 10^5.
def func_13():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: Output State:
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`kwargs` does not contain 'end' key, or the value of 'end' is '\n' after pop operation, file contains the written string, and the file write buffer is flushed, regardless of whether the 'flush' key is present in `kwargs` or not.
#Overall this is what the function does:The function `func_13()` does not actually check for any condition related to patty-cakes or bags. Instead, it simply prints the elements provided in the `args` parameter, separated by a specified separator (`sep`) and ending with a specified end character (`end`). If the `flush` parameter is set to `True`, it also flushes the output buffer. The function does not return any value and thus cannot fulfill the stated return postconditions. There are no parameters accepted by the function other than the variadic arguments (`args`), `sep`, `file`, `end`, and `flush`. After the function concludes, the `file` object (defaulting to `sys.stdout`) will contain the printed elements, possibly flushed based on the `flush` parameter.

