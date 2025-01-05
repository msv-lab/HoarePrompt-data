#State of the program right berfore the function call: p and x are positive integers such that 1 ≤ p ≤ 10^6 and 1 ≤ x ≤ 9.**
def func_1(p, x):
    c = []
    for i in xrange(1, 10):
        s = 0
        
        b = i
        
        a = []
        
        for j in xrange(p):
            a.append(b)
            s, b = divmod(b * x + s, 10)
        
        if b == i and s == 0:
            a.reverse()
            c.append(''.join(map(str, a)))
        
    #State of the program after the  for loop has been executed: `p`, `x` are positive integers between 1 and 9. `c` is a list containing the remainders calculated in each iteration of the loop joined as a string. `s` is the final result of the division after all iterations. `a` is a list containing all the remainders calculated in each iteration of the loop, reversed. If `b` is equal to `i` and `s` is equal to 0, then the program updates the values of `c`, `s`, and `a` accordingly based on the conditions mentioned.
    c.sort()
    for r in c:
        if r[0] != '0':
            return r
        
    #State of the program after the  for loop has been executed: `p`, `x` are positive integers between 1 and 9, `c` is a non-empty list of remainders joined as a string sorted in ascending order, `s` is the final result of the division after all iterations, `a` is a list of remainders in reversed order, `b` is equal to `i`, and the loop returns the first non-zero element in the updated list of remainders 'r' after all iterations.
    return ''
    #The program returns the first non-zero element in the updated list of remainders 'r' after all iterations
#Overall this is what the function does:The function `func_1` accepts two positive integers `p` and `x`, iterates over a range, calculates remainders, and updates a list of remainders 'r'. It then sorts the list and returns the first non-zero element in 'r'. The code does not implement cases mentioned in the annotations such as returning the list of remainders 'r', returning the updated list of remainders `r` after iterations, or returning the updated list of remainders 'r' after all iterations.

#State of the program right berfore the function call: p and x are positive integers such that 1 <= p <= 10^6 and 1 <= x <= 9.**
def func_2():
    p, x = map(int, raw_input().split())
    if (x == 5 and p % 42 == 0) :
        stdout.write(func_1(42, 5) * (p / 42))
        return
        #The program returns a value after the calculation when p is a positive integer such that p is divisible by 42 and x is a positive integer such that x equals 5
    #State of the program after the if block has been executed: *`p` and `x` are positive integers such that 1 <= p <= 10^6 and 1 <= x <= 9. Either x is not equal to 5 or p is not divisible by 42
    for i in xrange(1, 1000):
        s = func_1(i, x)
        
        if not s:
            continue
        
        l = len(s)
        
        if p % l == 0:
            stdout.write(s * (p / l))
        else:
            stdout.write('Impossible')
        
        return
        
    #State of the program after the  for loop has been executed: The program will print something if the variable `p` divided by `l` does not have a remainder of 0. If `p` divided by `l` has a remainder of 0, 'Impossible' will be printed to the standard output.
#Overall this is what the function does:The function `func_2` reads two positive integers `p` and `x` as input. If `x` is equal to 5 and `p` is divisible by 42, it calls another function `func_1` and calculates a value based on the result. If these conditions are not met, it iterates through a loop and calculates a value based on the return value of `func_1` for different inputs. If the division of `p` by the length of the returned value is not zero, it prints the calculated value. Otherwise, it prints 'Impossible'. Therefore, the functionality involves conditionally calculating values based on input integers `p` and `x`, and printing the results or 'Impossible' accordingly.

