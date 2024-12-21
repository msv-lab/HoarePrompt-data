#State of the program right berfore the function call: The function takes no arguments, but it is implied that it will receive and operate on three positive integers: a, b, and c, where 1 ≤ a ≤ 1000, 1 ≤ b ≤ 1000, and 1 ≤ c ≤ 1000, representing the number of lemons, apples, and pears, respectively.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    max_lemons = min(a, b // 2, c // 4)
    total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
    print(total_fruits)
#Overall this is what the function does:The function takes three positive integers as input from the user, representing the number of lemons, apples, and pears, and calculates the maximum number of lemons that can be used to make a combination of fruits where each lemon requires half an apple and a quarter of a pear. It then calculates the total number of fruits used in this combination and prints the result. The function does not handle cases where the input values are not positive integers or where the number of apples or pears is insufficient to make the combination, it simply assumes that the inputs will be valid. After execution, the program will have printed the total number of fruits used in the combination to the console, and the input variables will have been used and discarded.

