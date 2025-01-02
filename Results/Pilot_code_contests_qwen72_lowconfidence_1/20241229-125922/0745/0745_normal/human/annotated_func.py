#State of the program right berfore the function call: The function reads from standard input, where each line contains an integer between -50 and 50, inclusive.
def func():
    f = []
    for i in range(11):
        f.append(int(raw_input()))
        
    #State of the program after the  for loop has been executed: `f` is a list containing 11 integer values, each value being an integer between -50 and 50, inclusive, `i` is 10
    f.reverse()
    for x in f:
        y = abs(x)
        
        z = sqrt(y) + x ** 3 * 5
        
        if z < 400:
            print('f(%d) = %.2f' % (x, z))
        else:
            print('f(%d) = MAGNA NIMIS!' % x)
        
    #State of the program after the  for loop has been executed: `f` is a list containing 11 integer values, each value being an integer between -50 and 50, inclusive, in reverse order, `i` is 10, `x` is the last element of `f`, `y` is `abs(f[10])`, `z` is `sqrt(abs(f[10])) + f[10]
#Overall this is what the function does:The function `func` reads 11 integers from standard input, where each integer is between -50 and 50, inclusive. It stores these integers in a list `f`. The list is then reversed. For each integer `x` in the reversed list, it calculates `y` as the absolute value of `x`, and `z` as the square root of `y` plus five times the cube of `x`. If `z` is less than 400, it prints `f(x) = z` formatted to two decimal places. Otherwise, it prints `f(x) = MAGNA NIMIS!`. After the function completes, the list `f` contains 11 integers in reverse order, and the program has printed the results for each integer in `f`. The function does not return any value. Edge cases include handling negative numbers and the boundary condition where `z` is exactly 400, which would still trigger the "MAGNA NIMIS!" message.

