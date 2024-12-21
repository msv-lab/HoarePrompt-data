#State of the program right berfore the function call: a, b, and c are positive integers representing the number of lemons, apples, and pears respectively, with 1 ≤ a, b, c ≤ 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    max_lemons = min(a, b // 2, c // 4)
    total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
    print(total_fruits)
#Overall this is what the function does:The function reads three positive integers from the input, representing the quantities of lemons, apples, and pears. It then calculates the maximum number of complete fruit combinations that can be made using these fruits: each combination requires 1 lemon, 2 apples, and 4 pears. The function determines the maximum number of combinations based on the available fruits and prints the total number of fruits used in these combinations. The total is calculated as the sum of the fruits in all combinations made (1 lemon, 2 apples, and 4 pears for each combination). Note that the function does not return any values; it outputs the result directly. Additionally, failure to provide valid integer inputs could cause the function to raise an exception, but this potential issue is not handled in the code. It also does not consider cases where inputs might be zero, negatives, or non-integers, despite the initial state indicating all inputs are positive integers between 1 and 1000.

