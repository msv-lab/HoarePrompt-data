#State of the program right berfore the function call: t is a positive integer. For each test case, n is a positive integer, x is an integer such that 2 <= x <= 10^9, and a_i (1 <= i <= n) are positive integers.**
def func_1():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        
        a = [int(ai) for ai in input().split()]
        
        pow_x = [0] * n
        
        for i, ai in enumerate(a):
            cnt = 0
            while ai % x == 0:
                cnt += 1
                ai //= x
            pow_x[i] = cnt
        
        min_pow = min(pow_x)
        
        min_idx = pow_x.index(min_pow)
        
        func_2(sum(a) * (min_pow + 1) + sum(a[:min_idx]))
        
    #State of the program after the  for loop has been executed: `t` is a positive integer, `n` and `x` are assigned input integers, `a` is a list of integers, `pow_x` is a list of integers where each element represents the count of how many times the corresponding element in `a` was divisible by `x` until it's no longer divisible, `min_pow` is the minimum value from `pow_x`, `min_idx` is the index of the minimum value in `pow_x`, `func_2` remains unchanged, and the result of `func_2(sum(a) * (min_pow + 1) + sum(a[:min_idx]))` is returned for each test case
#Overall this is what the function does:The function `func_1` reads an input integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `x`, followed by a list of positive integers `a` with length `n`. It calculates the count of divisions of each element in `a` by `x`, finds the minimum count, and then calculates a specific value based on the sum of `a`, the minimum count, and a subset of `a`. This calculated value is passed to a function `func_2` for each test case. The function does not directly return any value.

#State of the program right berfore the function call: **Precondition**: The input consists of t test cases, where each test case has an integer n representing the length of the array and an integer x (2 ≤ x ≤ 10^9) representing the value used by the robot. The array a contains n integers (1 ≤ a_i ≤ 10^9). It is guaranteed that the sum of values of n over all test cases does not exceed 10^5.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `at_start` is False
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`at_start` is False. If 'flush' is popped from kwargs or False, the function will update the state accordingly. Otherwise, there is no change in the state of the program variables.
#Overall this is what the function does:The function func_2() processes t test cases, where each case contains an integer n representing the length of an array, an integer x representing a value used by a robot, and an array a. The function prints the values to a stream, separating them by a space, and ending each case with a newline character. If the 'flush' parameter is provided and set to True, the function will flush the output stream. The function accounts for the input constraints specified.

