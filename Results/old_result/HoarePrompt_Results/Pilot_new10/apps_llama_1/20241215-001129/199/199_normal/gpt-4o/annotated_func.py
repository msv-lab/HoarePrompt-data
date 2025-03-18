#State of the program right berfore the function call: n is a positive integer.
def func_1(n):
    if (n < 6) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: n is a positive integer, and n is greater than or equal to 6
    count = 0
    for a in range(1, n // 4 + 1):
        b = a
        
        rem = n - 2 * (a + b)
        
        if rem > 0 and rem % 2 == 0:
            if a != rem // 2:
                count += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `count` is the number of times the conditions `n - 4 * a > 0`, `n - 4 * a` is even, and `a` is not equal to `(n - 4 * a) // 2` are met for `a` in the range from 1 to `n // 4`, `a` is `n // 4`, `b` is `n // 4`.
    return count
    #The program returns the number of times the conditions `n - 4 * a > 0`, `n - 4 * a` is even, and `a` is not equal to `(n - 4 * a) // 2` are met for `a` in the range from 1 to `n // 4`.
#Overall this is what the function does:The function accepts a positive integer `n` and returns 0 if `n` is less than 6, or the count of integers `a` in the range from 1 to `n // 4` where `n - 4 * a > 0`, `n - 4 * a` is even, and `a` is not equal to `(n - 4 * a) // 2`, otherwise

