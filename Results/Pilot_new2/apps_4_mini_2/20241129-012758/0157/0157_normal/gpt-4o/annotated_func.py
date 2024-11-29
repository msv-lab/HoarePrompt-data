#State of the program right berfore the function call: a, b, and c are positive integers such that 1 ≤ a, b, c ≤ 1000, representing the number of lemons, apples, and pears, respectively.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    max_lemons = min(a, b // 2, c // 4)
    total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
    print(total_fruits)
#Overall this is what the function does:The function accepts three positive integers `a`, `b`, and `c` representing the quantities of lemons, apples, and pears, respectively. It calculates the number of maximum possible fruit combinations based on these inputs, where each combination requires 1 lemon, 2 apples, and 4 pears. It prints the total number of fruits that can be formed from these combinations. The function does not return any value but directly prints the result. No validation for the input range is implemented inside the function, assuming that the user will provide valid inputs as stated in the annotations.

