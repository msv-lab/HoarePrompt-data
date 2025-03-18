#State of the program right berfore the function call: a, b, and c are positive integers such that 1 ≤ a ≤ 1000, 1 ≤ b ≤ 1000, and 1 ≤ c ≤ 1000.**
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    max_lemons = min(a, b // 2, c // 4)
    total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
    print(total_fruits)
#Overall this is what the function does:The function prompts the user to input three positive integers a, b, and c. It then calculates the maximum number of lemons that can be obtained based on the minimum of a, b divided by 2, and c divided by 4. It further calculates the total number of fruits obtained by summing the squares of the lemons, twice the lemons, and four times the lemons. Finally, it prints the total number of fruits.

