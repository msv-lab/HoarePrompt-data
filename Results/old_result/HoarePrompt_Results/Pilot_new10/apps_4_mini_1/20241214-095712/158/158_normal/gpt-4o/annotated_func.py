#State of the program right berfore the function call: a, b, and c are positive integers such that 1 ≤ a, b, c ≤ 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    max_lemons = min(a, b // 2, c // 4)
    total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
    print(total_fruits)
#Overall this is what the function does:The function accepts three positive integers `a`, `b`, and `c` through user input, representing quantities of fruits. It calculates the maximum number of lemons that can be made using these fruits—where 1 lemon requires 1 unit of `a`, 2 units of `b`, and 4 units of `c`. It then computes the total number of fruits used based on the maximum number of lemons that can be made and prints this total. The function does not return any value.

