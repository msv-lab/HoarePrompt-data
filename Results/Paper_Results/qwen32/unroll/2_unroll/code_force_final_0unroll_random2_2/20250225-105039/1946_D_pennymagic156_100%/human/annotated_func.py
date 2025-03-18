#State of the program right berfore the function call: No variables in the function signature. This function reads input from the standard input and returns a list of integers.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers that were provided as input, split by spaces.
#Overall this is what the function does:The function reads a line of input from the standard input, splits it into components based on spaces, converts each component into an integer, and returns a list of these integers.

#State of the program right berfore the function call: The function `func_2` does not take any parameters.
def func_2():
    return int(input())
    #The program returns an integer value that is input by the user.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns an integer value that is input by the user.

#State of the program right berfore the function call: The function `func_3` does not have any parameters. It reads input from the standard input and returns a map object that applies the `int` function to each item in the input split by whitespace.
def func_3():
    return map(int, input().split())
    #The program returns a map object that applies the `int` function to each item in the input split by whitespace.
#Overall this is what the function does:The function reads a line of input from the standard input, splits it into components based on whitespace, converts each component to an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: The function `func_4` does not take any parameters and returns a string, which is the stripped input from the user.
def func_4():
    return input().strip()
    #The program returns a string that is the user's input with leading and trailing whitespace removed.
#Overall this is what the function does:The function `func_4` prompts the user for input, removes any leading and trailing whitespace from the input, and returns the resulting string.

#State of the program right berfore the function call: n is a positive integer representing the length of the array a, and x is a non-negative integer representing the favorite number. a is a list of non-negative integers of length n.
def func_5():
    n, x = func_3()
    a = func_1()
    t, ans = [], -1
    for i in range(29, -1, -1):
        u, v = x >> i & 1, sum([(val >> i & 1) for val in a])
        
        if u == v == 0:
            continue
        
        if u == 0:
            if v % 2:
                return ans
            else:
                op = ai = 0
                for val in a:
                    op ^= val >> i & 1
                    ai ^= val
                    if not op:
                        t.append(ai)
                        ai = 0
                a, t = t, []
        elif v % 2:
            continue
        elif v:
            op = cnt = 0
            for val in a:
                op ^= val >> i & 1
                if not op:
                    cnt += 1
            ans = max(ans, cnt)
        else:
            break
        
    #State: `n` is a positive integer returned by `func_3()`, `x` is a non-negative integer returned by `func_3()`, `a` is a list of non-negative integers (possibly empty), `t` is an empty list, `ans` is the maximum count of elements in `a` whose `i`-th bit, when XORed, results in `0`.
    return max(ans, len(a))
    #The program returns the maximum value between `ans` and the length of list `a`.
#Overall this is what the function does:The function computes and returns the maximum value between a variable `ans` and the length of a list `a` of non-negative integers. The list `a` and the integer `x` are obtained from other functions `func_1()` and `func_3()`, respectively. The variable `ans` is derived through a series of bitwise operations and comparisons involving the elements of `a` and the bits of `x`.

