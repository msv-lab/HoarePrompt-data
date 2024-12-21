#State of the program right berfore the function call: n, a, and b are positive integers, where 1 ≤ n, a, b ≤ 10 000 000.
def func_1():
    n = int(input())
    a = int(input())
    b = int(input())
    for x in range(n // a + 1):
        if (n - x * a) % b == 0:
            y = (n - x * a) // b
            print('YES')
            print(x, y)
            return
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `a` is a non-zero integer, `b` is an integer, and if the loop completes without returning, `x` equals `n // a`, indicating no suitable divisor was found for any `x` in the range.
    print('NO')
#Overall this is what the function does:The function accepts no parameters and reads three positive integers `n`, `a`, and `b` from the user. It checks if `n` can be expressed as a linear combination of `a` and `b` (i.e., `n = ax + by` for some integers `x` and `y`) by iterating over possible values of `x`. If such a combination is found, it prints 'YES' along with the corresponding values of `x` and `y`, and then returns without any explicit return value (i.e., it implicitly returns `None`). If no such combination is found after checking all possible values of `x`, it prints 'NO' and returns without any explicit return value (i.e., it implicitly returns `None`). The function does not handle potential edge cases such as non-integer or non-positive inputs, or cases where `a` or `b` is zero, which could lead to errors or unexpected behavior.

