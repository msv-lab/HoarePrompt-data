#State of the program right berfore the function call: x and y are integers such that 3 ≤ y < x ≤ 100 000.
def func():
    x, y = map(int, input().split())
    print((x - y) // 2 + (x - y) % 2)
#Overall this is what the function does:The function accepts two integer parameters, `x` and `y`, as input from the user, calculates the ceiling of their difference divided by 2, and prints the result, without enforcing any specific constraints on the input values.

