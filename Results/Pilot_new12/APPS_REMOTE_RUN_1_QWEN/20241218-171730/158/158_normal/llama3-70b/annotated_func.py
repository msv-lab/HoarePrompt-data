#State of the program right berfore the function call: a, b, and c are integers such that 1 ≤ a, b, c ≤ 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    min_lemon = min(a, b // 2, c // 4)
    print(min_lemon + min_lemon * 2 + min_lemon * 4)
#Overall this is what the function does:The function reads three integers `a`, `b`, and `c` from the user input where each integer is between 1 and 1000. It then calculates the minimum value among `a`, `b // 2`, and `c // 4`. The function prints the result of adding the minimum value to itself twice and four times, which is equivalent to printing `8 * min_lemon`, where `min_lemon` is the minimum of `a`, `b // 2`, and `c // 4`. The function does not return any value explicitly.

