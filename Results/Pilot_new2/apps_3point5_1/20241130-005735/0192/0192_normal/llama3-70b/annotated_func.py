#State of the program right berfore the function call: x and y are integers such that 3 ≤ y < x ≤ 100,000.**
def func():
    x, y = map(int, input().split())
    print(abs(x - y))
#Overall this is what the function does:The function `func` reads two integers x and y from the input, and then prints the absolute difference between x and y. The function operates under the constraints that x and y are integers such that 3 ≤ y < x ≤ 100,000. This function does not return any value, it simply prints the absolute difference between x and y.

