#State of the program right berfore the function call: a, b, and c are positive integers representing the number of lemons, apples, and pears Nikolay has, respectively, with the constraints 1 ≤ a, b, c ≤ 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    max_lemons = min(a, b // 2, c // 4)
    total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
    print(total_fruits)
#Overall this is what the function does:The function accepts three positive integers `a`, `b`, and `c`, which represent the number of lemons, apples, and pears, respectively. It calculates the maximum number of complete sets of fruits that can be formed, with 1 lemon, 2 apples, and 4 pears per set, and prints the total number of fruits in all sets. However, it does not return any value; it only prints the result. Additionally, it does not handle cases where the inputs are outside the specified constraints or invalid input types, which could lead to runtime errors.

