#State of the program right berfore the function call: a, b, and c are non-negative integers such that 1 <= a, b, c <= 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    min_lemon = min(a, b // 2, c // 4)
    print(min_lemon + min_lemon * 2 + min_lemon * 4)
#Overall this is what the function does:The function reads three non-negative integers `a`, `b`, and `c` (where 1 <= a, b, c <= 1000), calculates `min_lemon` as the minimum value among `a`, `b // 2`, and `c // 4`, and prints the result of the expression `min_lemon + min_lemon * 2 + min_lemon * 4`.

