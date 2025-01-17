#State of the program right berfore the function call: a is an integer representing the power of the spell, and b is an integer representing the number of students.
def func_1(a, b):
    return (a + 2) * (b + 4) - 1 if a >= b else (a + 5) * (b + 1) - 1
    #`(a + 2) * (b + 4) - 1` if a is greater than or equal to b else `(a + 5) * (b + 1) - 1`
#Overall this is what the function does:The function `func_1` accepts two parameters, `a` and `b`, both of which are integers. It evaluates a condition to determine whether `a` is greater than or equal to `b`. Based on this condition, the function returns one of two possible expressions: `(a + 2) * (b + 4) - 1` if `a` is greater than or equal to `b`, or `(a + 5) * (b + 1) - 1` otherwise. There are no additional actions or side effects performed by the function. The final state of the program after the function concludes is that the function has returned one of the two specified expressions, depending on the values of `a` and `b`.

