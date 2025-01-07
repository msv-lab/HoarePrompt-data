#State of the program right berfore the function call: a, b, and c are positive integers such that 1 ≤ a, b, c ≤ 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    min_lemon = min(a, b // 2, c // 4)
    print(min_lemon + min_lemon * 2 + min_lemon * 4)
#Overall this is what the function does:The function takes three positive integer inputs (a, b, and c) from the user, all constrained between 1 and 1000. It calculates the minimum value of a, half of b, and a quarter of c. Using this minimum value, it computes a result by adding it to itself multiplied by 2 and multiplied by 4, and then prints this final result. However, the function does not handle scenarios where any of the inputs are not positive integers or out of the specified range, nor does it return values to another part of a program—it solely prints the output without any form of validation or error handling.

