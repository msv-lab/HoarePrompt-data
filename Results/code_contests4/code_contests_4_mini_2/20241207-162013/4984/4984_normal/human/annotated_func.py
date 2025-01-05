#State of the program right berfore the function call: p is a positive integer representing the length of the desired number in decimal digits (1 ≤ p ≤ 10^6), and x is a positive integer (1 ≤ x ≤ 9) which represents the multiplication factor.
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
        
    #State of the program after the  for loop has been executed: `p` is a positive integer (1 ≤ `p` ≤ 10^6), `x` is a positive integer (1 ≤ `x` ≤ 9), `c` is a list containing the joined string representations of the reversed lists `a` for all values of `i` from 1 to 9 where `b` equals `i` and `s` is 0 after processing.
    c.sort()
    for r in c:
        if r[0] != '0':
            return r
        
    #State of the program after the  for loop has been executed: `p` is a positive integer, `x` is a positive integer, `s` is 0, `c` is a collection where all elements start with '0', and the loop will not return any element from `c`.
    return ''
    #The program returns an empty string ''
#Overall this is what the function does:The function accepts two positive integers, `p` (representing the length of the desired number in decimal digits) and `x` (a multiplication factor), and generates a list of numbers based on specific criteria. It returns the smallest valid number formed by digits from 1 to 9 that meets the criteria, or an empty string if no such number exists. The criteria require that the last digit of the number matches the starting digit and that the sum of the digits processed is zero. The function does not handle cases where inputs are out of the specified range, but it ensures that the returned number does not start with '0'.

#State of the program right berfore the function call: p is a positive integer representing the length of the number in decimal digits (1 ≤ p ≤ 10^6), and x is a positive integer representing the multiplication factor (1 ≤ x ≤ 9).
def func_2():
    p, x = map(int, raw_input().split())
    if (x == 5 and p % 42 == 0) :
        stdout.write(func_1(42, 5) * (p / 42))
        return
        #The program returns the result of func_1(42, 5) multiplied by (p / 42), where p is a positive integer divisible by 42.
    #State of the program after the if block has been executed: *`p` is a positive integer representing the length of the number in decimal digits; `x` is a positive integer representing the multiplication factor. `x` is not equal to 5 or `p` is not divisible by 42.
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
        
    #State of the program after the  for loop has been executed: `p` is a positive integer, `x` is a positive integer not equal to 5, `s` is None, `i` has iterated up to 1000 but no valid output was produced.
#Overall this is what the function does:The function accepts two positive integers, `p` (the length of the number in decimal digits) and `x` (a multiplication factor). If `x` is 5 and `p` is divisible by 42, it returns the result of `func_1(42, 5)` multiplied by `(p / 42)`. If `x` is not 5, it iterates from 1 to 999, calling `func_1(i, x)` for each `i`. If a non-None result `s` is obtained and `p` is divisible by the length of `s`, it outputs `s` repeated `(p / l)` times. If no valid output is produced after 1000 iterations, it returns 'Impossible'. The function does not handle the case where `p` is 0 or negative, which could lead to unexpected behavior.

