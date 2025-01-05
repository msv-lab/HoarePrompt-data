#State of the program right berfore the function call: p is a strictly positive integer representing the length of the decimal number (1 ≤ p ≤ 10^6), and x is a positive integer (1 ≤ x ≤ 9).
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
        
    #State of the program after the  for loop has been executed: `p` is a strictly positive integer, `c` contains all valid strings of length `p` that can be formed by the digits 1 to 9, where each string starts and ends with the same digit and is formed by repeatedly multiplying by `x` and summing the previous digits.
    c.sort()
    for r in c:
        if r[0] != '0':
            return r
        
    #State of the program after the  for loop has been executed: `p` is a strictly positive integer, `c` contains valid strings of length `p`, and `r` is the first valid string in `c` that starts with a digit from 1 to 9.
    return ''
    #The program returns an empty string ''
#Overall this is what the function does:The function accepts a strictly positive integer `p`, representing the length of a decimal number, and a positive integer `x`. It generates all valid strings of length `p` formed by the digits 1 to 9, where each string starts and ends with the same digit and is generated through a specific multiplication and summation process. The function returns the first valid string that does not start with '0', or an empty string if no valid strings are found. It does not handle cases where valid strings may start with '0' after sorting since the return condition explicitly checks for strings starting with '0' as invalid.

#State of the program right berfore the function call: p is a positive integer representing the length of the decimal number, and x is an integer between 1 and 9.
def func_2():
    p, x = map(int, raw_input().split())
    if (x == 5 and p % 42 == 0) :
        stdout.write(func_1(42, 5) * (p / 42))
        return
        #The program returns no specific value as the return statement is empty
    #State of the program after the if block has been executed: *`p` is a positive integer; `x` is an integer between 1 and 9. Either `x` is not equal to 5, or `p` is not divisible by 42.
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
        
    #State of the program after the  for loop has been executed: The program does not return any value as the return statement is empty, `i` is 1000, `s` is the result of func_1(999, x), and `p` is a positive integer.
#Overall this is what the function does:The function accepts two parameters: a positive integer `p` (representing the length of a decimal number) and an integer `x` (between 1 and 9). It checks if `x` is 5 and if `p` is divisible by 42. If both conditions are met, it writes the result of `func_1(42, 5)` multiplied by `p / 42`. If not, it iterates through integers from 1 to 999, calling `func_1(i, x)` and checking if the result is non-empty. If the length of the result divides `p`, it writes the result repeated `p / l` times; otherwise, it writes 'Impossible'. If none of these conditions are met, the function ultimately does not return any specific value.

