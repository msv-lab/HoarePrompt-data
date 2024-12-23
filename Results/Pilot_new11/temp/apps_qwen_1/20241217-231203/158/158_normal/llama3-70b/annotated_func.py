#State of the program right berfore the function call: a, b, and c are non-negative integers such that 1 <= a, b, c <= 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    min_lemon = min(a, b // 2, c // 4)
    print(min_lemon + min_lemon * 2 + min_lemon * 4)
#Overall this is what the function does:The function reads three non-negative integers `a`, `b`, and `c` from the user, each constrained between 1 and 1000. It then calculates the minimum value among `a`, `b // 2`, and `c // 4`. This minimum value is referred to as `min_lemon`. The function then prints the sum of `min_lemon`, `min_lemon * 2`, and `min_lemon * 4`. The function does not return a value, but instead outputs the calculated sum. There are no explicit return statements in the provided code, but the behavior can be inferred from the print statement.

