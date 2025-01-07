#State of the program right berfore the function call: a, b, and c are positive integers representing the number of lemons, apples, and pears respectively, with 1 ≤ a, b, c ≤ 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    min_lemon = min(a, b // 2, c // 4)
    print(min_lemon + min_lemon * 2 + min_lemon * 4)
#Overall this is what the function does:The function accepts three positive integers `a`, `b`, and `c` from user input, which represent the number of lemons, apples, and pears respectively. It calculates the minimum value among `a`, half of `b`, and a quarter of `c`. The function then computes and prints a total based on this minimum value, specifically `min_lemon + min_lemon * 2 + min_lemon * 4`, which results in `7 * min_lemon`. The function does not return any value; instead, it outputs the result directly.

