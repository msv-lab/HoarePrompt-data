#State of the program right berfore the function call: **
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
        
    #State of the program after the  for loop has been executed: The loop will execute based on the input value. `a`, `b`, `s`, `cnt`, `this`, `flag` will have values assigned from func_3() and loop operations. `s` will be a list with 'X' appended, `cnt` will be the count of 'X' elements followed by a sequence of '.', `this` will be the count of consecutive '.' before 'X', `flag` will be True if there are two consecutive '.', otherwise False. The program will print 'NO' if an exception is raised during the iteration, otherwise it will print 'YES' if cnt is odd and 'NO' if cnt is even.
#Overall this is what the function does:The function func_1 reads an integer input and iterates a loop that performs various operations based on the input values and the values returned from func_3. It handles a sequence of characters in a list, counts occurrences of specific characters, and determines whether to print 'YES' or 'NO' based on certain conditions. The function does not accept any parameters and does not return any value.

#State of the program right berfore the function call: **Precondition**: **q is a positive integer. For each query, a and b are positive integers such that 1 ≤ b < a ≤ 3 ⋅ 10^5. s is a string of length at most 3 ⋅ 10^5, consisting of only characters '.' and 'X'.**
def func_2(x, y):
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: Both x and y will be assigned the greatest common divisor of the initial values of x and y. The loop will terminate when y becomes 0, and at that point, x will hold the greatest common divisor of the initial x and y values, while y will be 0.
    return x
    #The program returns the greatest common divisor of the initial values of x and y
#Overall this is what the function does:The function `func_2` accepts two positive integers `x` and `y` and calculates the greatest common divisor of their initial values using the Euclidean algorithm. It continuously updates the values of `x` and `y` until `y` becomes 0, at which point it returns the greatest common divisor. The function adheres to the precondition that `q` is a positive integer, and for each query, `a` and `b` are positive integers such that 1 ≤ b < a ≤ 3 ⋅ 10^5. `s` is a string of length at most 3 ⋅ 10^5, consisting only of characters '.' and 'X'.

#State of the program right berfore the function call: **
def func_3():
    return list(map(int, input().split()))
    #The program returns a list of integers after converting the input values to integers using the map function and splitting the input
#Overall this is what the function does:The function `func_3` does not accept any parameters. It converts the input values to integers using the map function and splits the input to return a list of integers.

#State of the program right berfore the function call: **Precondition**: **q is a positive integer. For each query, a and b are positive integers such that 1 ≤ b < a ≤ 3 ⋅ 10^5. s is a string of length at most 3 ⋅ 10^5, consisting of only characters . and X.**
def func_4(f):
    return [func_4(f, *dim[1:]) for _ in range(dim[0])] if dim else f()
    #The program returns a list of values calculated by calling func_4 with arguments from dim[1:], repeated dim[0] times if dim is not empty, otherwise it returns the result of calling f()
#Overall this is what the function does:The function func_4 accepts a function f as a parameter. It then returns a list of values calculated by calling func_4 with arguments from dim[1:], repeated dim[0] times if dim is not empty. If dim is empty, it returns the result of calling f().

#State of the program right berfore the function call: **Precondition**: **start, step, and count are positive integers such that 1 <= step < start <= 3*10^5.**
def func_5(start, step, count):
    return range(start, start + step * count, step)
    #The program returns a range starting from 'start' up to 'start + step * count' with a step size of 'step'.
#Overall this is what the function does:The function accepts positive integers start, step, and count, and returns a range starting from 'start' up to 'start + step * count' with a step size of 'step'. The code accurately implements this functionality. No edge cases or missing functionality are apparent based on the provided code and annotations.

#State of the program right berfore the function call: l is a list of tuples where each tuple contains two integers representing a and b such that 1 ≤ b < a ≤ 3 ⋅ 10^5. start and end are non-negative integers representing the starting and ending positions of the substring in the string.**
def func_6(l, start, end):
    return range(start, len(l) + end)
    #The program returns a range starting from position 'start' up to the length of list 'l' plus 'end'.
#Overall this is what the function does:The function `func_6` accepts a list `l` of tuples and two integers `start` and `end`. It then returns a range starting from position `start` up to the length of list `l` plus `end`. The function does not consider the contents of the tuples within the list `l`, it solely operates based on the length of the list and the provided `start` and `end` values.

#State of the program right berfore the function call: **
def func_7(n):
    return 2 ** (n - 1).bit_length()
    #The program returns the result of 2 raised to the power of the length of (n - 1) in binary representation
#Overall this is what the function does:The function accepts an integer parameter `n` and returns the result of 2 raised to the power of the length of (n - 1) in binary representation. It does not account for any edge cases or potential errors such as negative values of `n`.

#State of the program right berfore the function call: **
def func_8(x, r):
    return (x + r - 1) // r
    #The program returns the value of (x + r - 1) divided by r, rounded down to the nearest integer
#Overall this is what the function does:The function accepts two integer parameters x and r, calculates the value of (x + r - 1) divided by r, and returns the result rounded down to the nearest integer.

