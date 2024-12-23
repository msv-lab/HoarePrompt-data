#State of the program right berfore the function call: a, b, and c are positive integers such that 1 ≤ a, b, c ≤ 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    max_lemons = min(a, b // 2, c // 4)
    total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
    print(total_fruits)
#Overall this is what the function does:The function reads three positive integers, a, b, and c, from user input, which must each be in the range of 1 to 1000. It calculates the maximum number of lemon-based fruits that can be created based on the constraints that each lemon requires 1 unit of a, 2 units of b, and 4 units of c. It computes the total number of fruits produced by multiplying the maximum number of lemons by a scaling factor depending on the fruit type: 1 for lemon, 2 for lime, and 4 for lemon-lime. Finally, the function prints the total number of fruits produced. Notably, there are no checks for invalid input or to handle cases where the inputs are out of the expected range. Furthermore, the function does not return any value; it merely outputs the result to the console.

