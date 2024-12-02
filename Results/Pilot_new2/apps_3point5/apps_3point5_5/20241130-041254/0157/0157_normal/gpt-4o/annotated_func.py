#State of the program right berfore the function call: **
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    max_lemons = min(a, b // 2, c // 4)
    total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
    print(total_fruits)
#Overall this is what the function does:The function reads three integers from the user inputs, calculates the maximum number of lemons that can be made based on the minimum of ratios provided, computes the total number of fruits considering different lemonade recipes, and prints the total number of fruits. However, the function does not accept any parameters and does not return any value.

