#State of the program right berfore the function call: a, b, c are positive integers such that 1 ≤ a ≤ 1000, 1 ≤ b ≤ 1000, and 1 ≤ c ≤ 1000.**
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    max_lemons = min(a, b // 2, c // 4)
    total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
    print(total_fruits)
#Overall this is what the function does:The function `func` reads three input integers a, b, and c. It then calculates the maximum number of lemons that can be obtained based on the minimum of a, b divided by 2, and c divided by 4. After that, it computes the total number of fruits by considering the quantity of lemons, oranges (2 lemons per orange), and apples (4 lemons per apple). Finally, it prints the total number of fruits obtained. The function does not handle any edge cases or errors related to input validation or division by zero, so these scenarios are missing from the implementation.

