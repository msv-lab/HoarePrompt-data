#State of the program right berfore the function call: a, b, and c are positive integers representing the number of lemons, apples, and pears Nikolay has, respectively, where 1 ≤ a, b, c ≤ 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    min_lemon = min(a, b // 2, c // 4)
    print(min_lemon + min_lemon * 2 + min_lemon * 4)
#Overall this is what the function does:The function accepts three positive integers from user input representing the number of lemons (a), apples (b), and pears (c). It calculates the minimum number of complete sets of fruit that can be made, considering that each set requires 1 lemon, 2 apples, and 4 pears. It then calculates and prints the total value of these sets, where each set is valued at 1 for lemons, 2 for apples, and 4 for pears. The function does not handle invalid inputs or cases where any of the inputs are less than the required quantities for a complete set.

