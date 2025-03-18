#State of the program right berfore the function call: x and y are integers such that 3 ≤ y < x ≤ 100,000.**
def func():
    x, y = map(int, input().split())
    print(abs(x - y))
#Overall this is what the function does:The function `func` reads two integer inputs x and y, where 3 ≤ y < x ≤ 100,000, computes the absolute difference between x and y, and prints the result.

