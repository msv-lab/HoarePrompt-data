#State of the program right berfore the function call: **Precondition**: **a, b, and c are positive integers such that 1 ≤ a, b, c ≤ 1000.**
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    max_lemons = min(a, b // 2, c // 4)
    total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
    print(total_fruits)
#Overall this is what the function does:The function takes three positive integers a, b, and c as input, calculates the maximum number of lemons that can be obtained based on the constraints, and then calculates the total number of fruits by multiplying the maximum number of lemons with their respective values (1, 2, and 4). Finally, it prints the total number of fruits obtained.

