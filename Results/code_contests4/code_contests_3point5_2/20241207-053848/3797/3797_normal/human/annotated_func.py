#State of the program right berfore the function call: q is a positive integer. For each query, a and b are positive integers such that 1 ≤ b < a ≤ 3 ⋅ 10^5. The string s consists of characters '.' and 'X' with a length between 1 and 3 ⋅ 10^5.**
def func_1():
    for _ in range(int(input())):
        a, b = func_3()
        
        s = list(input())
        
        s.append('X')
        
        cnt = 0
        
        this = 0
        
        flag = False
        
        try:
            for c in s:
                if c == 'X' and this > 0:
                    if b <= this < a or a + 4 * b - 1 <= this:
                        raise
                    if 2 * b <= this:
                        if flag:
                            raise
                        flag = True
                        if this < a:
                            raise
                    cnt += 1
                    this = 0
                elif c == '.':
                    this += 1
            print('NO' if cnt % 2 else 'YES')
        except:
            print('NO')
        
    #State of the program after the  for loop has been executed: `q` and `_` are positive integers, `a` and `b` are within the range of the input integer, `s` is a list of characters from the input string with 'X' appended at the end. `cnt` will be the total count of occurrences where 'X' is followed by a number greater than 0, `this` will be 0 after each occurrence of 'X'. `flag` will be True if 2 * `b` is less than or equal to `this` at any point in the loop. The code will print 'NO' if `cnt` is even and 'YES' if `cnt` is odd.
#Overall this is what the function does:The function `func_1` processes multiple queries, each consisting of parameters `q`, `a`, `b`, and `s`. It iterates through the queries, calculates the count of occurrences where 'X' is followed by a number greater than 0, and prints 'YES' if the count is odd and 'NO' if it is even. The code handles the cases where specific conditions related to `a` and `b` are met during the iteration. If any of the conditions are violated, it prints 'NO'.

#State of the program right berfore the function call: 
def func_2(x, y):
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: The loop will continue to execute as long as `y` evaluates to True. After all iterations have completed, `x` will hold the greatest common divisor (GCD) of the initial values of `x` and `y`, and `y` will be 0.
    return x
    #The program returns the greatest common divisor (GCD) of the initial values of `x` and `y`, where `y` becomes 0 after executing the loop
#Overall this is what the function does:The function `func_2` accepts two parameters `x` and `y`. It calculates the greatest common divisor (GCD) of the initial values of `x` and `y` using the Euclidean algorithm. After executing the loop, the program returns the GCD of `x` and `y`, where `y` becomes 0. The functionality accurately reflects the code logic.

#State of the program right berfore the function call: **
def func_3():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained by mapping the input values after splitting them
#Overall this is what the function does:The function `func_3` does not accept any parameters. It reads input values, splits them, converts them to integers, and returns a list of these integers. Therefore, the functionality of the function is to return a list of integers obtained by mapping the input values after splitting them.

#State of the program right berfore the function call: Each query consists of two integers a and b (1 ≤ b < a ≤ 3 ⋅ 10^5), and a string s of length at most 3 ⋅ 10^5 consisting of characters . and X.**
def func_4(f):
    return [func_4(f, *dim[1:]) for _ in range(dim[0])] if dim else f()
    #The program returns a list of values calculated by calling function func_4 with arguments unpacked from dim[1:], repeated dim[0] times if dim is not empty, otherwise calling function f()
#Overall this is what the function does:The function func_4 accepts a function `f` as a parameter. It returns a list of values calculated by calling function `func_4` with arguments unpacked from dim[1:], repeated dim[0] times if dim is not empty. If dim is empty, it returns the result of calling function `f()`.

#State of the program right berfore the function call: **
def func_5(start, step, count):
    return range(start, start + step * count, step)
    #The program returns a range starting from 'start' and ending at 'start + step * count' with a step size of 'step'
#Overall this is what the function does:The function accepts three integer parameters: start, step, and count, and returns a range starting from 'start' and ending at 'start + step * count' with a step size of 'step'. The function does not handle cases where step is 0, which would result in an invalid range.

#State of the program right berfore the function call: **
def func_6(l, start, end):
    return range(start, len(l) + end)
    #The program returns a range starting from 'start' to the length of list 'l' plus 'end'
#Overall this is what the function does:The function func_6 accepts a list 'l', an integer 'start', and an integer 'end'. It returns a range starting from 'start' to the length of list 'l' plus 'end'. However, the code does not handle cases where 'start' or 'end' are negative, which could lead to unexpected results or errors. It also does not account for cases where 'l' is empty, potentially causing issues with the range calculation.

#State of the program right berfore the function call: **
def func_7(n):
    return 2 ** (n - 1).bit_length()
    #The program returns the result of 2 raised to the power of (n - 1)'s bit length.
#Overall this is what the function does:The function func_7 accepts an integer parameter n and returns the result of 2 raised to the power of the bit length of (n - 1).

#State of the program right berfore the function call: - q is a positive integer.
def func_8(x, r):
    return (x + r - 1) // r
    #The program returns the result of the expression (x + r - 1) divided by r using integer division
#Overall this is what the function does:The function accepts two parameters x and r where q is a positive integer. It calculates the result of the expression (x + r - 1) divided by r using integer division.

