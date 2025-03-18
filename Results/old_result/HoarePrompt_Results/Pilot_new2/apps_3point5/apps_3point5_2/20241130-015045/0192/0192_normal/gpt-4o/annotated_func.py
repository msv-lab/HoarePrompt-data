#State of the program right berfore the function call: x and y are integers such that 3 <= y < x <= 100,000.**
def func():
    x, y = map(int, input().split())
    print((x - y) // 2 + (x - y) % 2)
#Overall this is what the function does:The function reads two integers `x` and `y` from input, then calculates and prints the result of ((x - y) // 2) + ((x - y) % 2). The function assumes that x and y are integers where 3 <= y < x <= 100,000. It calculates the sum of all integers between x and y. It does not return any value, only prints the result.

