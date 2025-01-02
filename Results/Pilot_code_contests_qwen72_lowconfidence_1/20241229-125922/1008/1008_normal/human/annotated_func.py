#State of the program right berfore the function call: None of the variables are passed as arguments to the function `func_1`. This function reads input from standard input (stdin) and returns a map object containing integers parsed from the input. The input is expected to be a single line of space-separated integers.
def func_1():
    return map(int, sys.stdin.readline().strip().split())
    #The program returns a map object containing integers parsed from a single line of space-separated integers read from standard input (stdin).
#Overall this is what the function does:The function `func_1` reads a single line of input from standard input (stdin), which is expected to contain space-separated integers. It parses these integers and returns a map object containing the parsed integers. If the input contains non-integer values, a `ValueError` will be raised. If the input is empty, the returned map object will be empty.

#State of the program right berfore the function call: None. This function does not take any parameters and reads input from stdin, which is expected to be a line of space-separated integers.
def func_2():
    return list(map(int, sys.stdin.readline().strip().split()))
    #The program returns a list of integers converted from a line of space-separated integers read from stdin.
#Overall this is what the function does:The function `func_2` reads a single line of input from standard input (stdin), expecting the line to contain space-separated integers. It converts these integers from strings to integers and returns them as a list. If the input contains non-integer values, the function will raise a `ValueError`. If the input line is empty, the function will return an empty list. The function does not handle multiple lines of input or any other form of input validation.

#State of the program right berfore the function call: None of the variables are used in the function signature.
def func_3():
    return sys.stdin.readline().strip()
    #The program returns a line of input from the standard input (stdin) with trailing whitespace removed.
#Overall this is what the function does:The function `func_3` does not accept any parameters. It reads a line of input from the standard input (stdin) and returns the line with trailing whitespace removed. If the input is empty or only contains whitespace, the function will return an empty string.

#State of the program right berfore the function call: x and y are integers.
def func_4(x, y):
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: `x` is the GCD of the original values of `x` and `y`, `y` is 0
    return x
    #The program returns the GCD of the original values of `x` and `y`
#Overall this is what the function does:The function `func_4` accepts two integer parameters `x` and `y`. It computes and returns the Greatest Common Divisor (GCD) of the original values of `x` and `y`. After the function executes, `x` holds the GCD of the original values of `x` and `y`, and `y` is 0. The function handles all integer inputs, including negative integers and zero, correctly computing the GCD in all cases.

#State of the program right berfore the function call: x and y are positive integers.
def func_5(x, y):
    return x * y // func_4(x, y)
    #The program returns the integer division result of (x * y) by the value returned from `func_4(x, y)`, where `x` and `y` are positive integers.
#Overall this is what the function does:The function `func_5` accepts two parameters `x` and `y`, both expected to be positive integers. It returns the integer division result of `(x * y)` by the value returned from `func_4(x, y)`. If `func_4(x, y)` returns 0, a `ZeroDivisionError` will occur. Additionally, if `x` or `y` are not positive integers, the behavior is undefined and could lead to unexpected results or errors.

#State of the program right berfore the function call: rows, cols, and k are positive integers such that 2 ≤ rows, cols ≤ 300 and 2 ≤ 2k ≤ rows * cols.
def func_6():
    rows, cols, k = func_1()
    curr_x = curr_y = 0
    turn = 0
    store = []
    for i in range(rows):
        if not turn:
            for j in range(cols):
                store.append([i + 1, j + 1])
        else:
            for j in range(cols - 1, -1, -1):
                store.append([i + 1, j + 1])
        
        turn ^= 1
        
    #State of the program after the  for loop has been executed: `rows` is a positive integer such that 2 ≤ `rows` ≤ 300, `cols` is a positive integer such that 2 ≤ `cols` ≤ 300, `k` is a positive integer such that 2 ≤ 2`k` ≤ `rows` * `cols`, `curr_x` is 0, `curr_y` is 0, `i` is `rows - 1`, `turn` is 0 if `rows` is even and 1 if `rows` is odd, `store` contains a list of pairs representing the coordinates in a zigzag pattern: for even `i`, `[[i + 1, 1], [i + 1, 2], ..., [i + 1, cols]]`, and for odd `i`, `[[i + 1, cols], [i + 1, cols - 1], ..., [i + 1, 1]]`.
    i = 0
    count = 0
    while count < k - 1:
        print(2, end=' ')
        
        print(*store[i], end=' ')
        
        print(*store[i + 1])
        
        i += 2
        
        count += 1
        
    #State of the program after the loop has been executed: `rows` is a positive integer such that 2 ≤ `rows` ≤ 300, `cols` is a positive integer such that 2 ≤ `cols` ≤ 300, `k` is a positive integer such that 2 ≤ 2`k` ≤ `rows` * `cols`, `curr_x` is 0, `curr_y` is 0, `i` is 2 * (`k` - 1), `turn` is 0 if `rows` is even and 1 if `rows` is odd, `store` contains a list of pairs representing the coordinates in a zigzag pattern, `count` is `k` - 1, 2 has been printed `k` - 1 times, and the first 2 * (`k` - 1) pairs of coordinates from `store` have been printed.
    print(rows * cols - 2 * (k - 1), end=' ')
    while i < rows * cols:
        if i == rows * cols - 1:
            print(*store[i])
        else:
            print(*store[i], end=' ')
        
        i += 1
        
    #State of the program after the loop has been executed: `rows` is a positive integer such that 2 ≤ `rows` ≤ 300, `cols` is a positive integer such that 2 ≤ `cols` ≤ 300, `k` is a positive integer such that 2 ≤ 2`k` ≤ `rows` * `cols`, `curr_x` is 0, `curr_y` is 0, `i` is `rows * cols`, `turn` is 0 if `rows` is even and 1 if `rows` is odd, `store` contains a list of pairs representing the coordinates in a zigzag pattern, `count` is `k` - 1, 2 has been printed `k` - 1 times, the first 2 * (`k` - 1) pairs of coordinates from `store` have been printed, `rows * cols - 2 * (k - 1)` has been printed followed by a space, and all elements from `store` from index `2 * (k - 1)` to `rows * cols - 2` have been printed followed by a space, and the last element of `store` (index `rows * cols - 1`) has been printed without a trailing space.
#Overall this is what the function does:The function `func_6` generates and prints a sequence of numbers and coordinates based on the parameters `rows`, `cols`, and `k` provided by the function `func_1()`. The function performs the following actions:

1.

