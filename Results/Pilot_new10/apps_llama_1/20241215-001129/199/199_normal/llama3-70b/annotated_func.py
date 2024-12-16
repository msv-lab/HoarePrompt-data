#State of the program right berfore the function call: n is a positive integer greater than or equal to 4.
def func_1(n):
    ways = 0
    for a in range(1, n // 2 + 1):
        for b in range(a, (n - a) // 2 + 1):
            if a != b and 2 * (a + b) == n:
                ways += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer greater than or equal to 4, `ways` is the number of pairs of distinct positive integers `(a, b)` where `a` is in the range from 1 to `n // 2`, `b` is in the range from `a` to `(n - a) // 2`, and `2 * (a + b) == n`.
    return ways
    #The program returns the number of pairs of distinct positive integers (a, b) where a is from 1 to n//2, b is from a to (n-a)//2, and 2*(a+b) equals n, for a given positive integer n greater than or equal to 4.
#Overall this is what the function does:The function accepts a positive integer `n` greater than or equal to 4 and returns the number of distinct positive integer pairs `(a, b)` where `a` is from 1 to `n//2`, `b` is from `a` to `(n-a)//2`, and `2*(a+b)` equals `n`, or returns 0 if no such pairs exist, and may not be well-defined for `n` less than 4 or for non-integer or non-positive inputs

