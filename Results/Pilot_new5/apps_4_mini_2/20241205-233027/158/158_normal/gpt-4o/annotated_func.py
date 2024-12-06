#State of the program right berfore the function call: a, b, and c are positive integers representing the number of lemons, apples, and pears Nikolay has, respectively, with values ranging from 1 to 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    max_lemons = min(a, b // 2, c // 4)
    total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
    print(total_fruits)
#Overall this is what the function does:The function accepts three positive integers representing the quantities of lemons, apples, and pears. It calculates the maximum number of lemons that can be made based on the available fruits (limited by half the number of apples and one-quarter of the number of pears) and prints the total number of fruits that can be made, with each lemon contributing one fruit, each apple contributing two, and each pear contributing four. The function does not handle invalid input or cases where the inputs are outside the specified range.

