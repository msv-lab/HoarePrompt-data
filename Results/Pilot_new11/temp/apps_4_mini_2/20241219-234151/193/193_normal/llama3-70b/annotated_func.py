#State of the program right berfore the function call: x and y are integers such that 3 ≤ y < x ≤ 100000.
def func():
    x, y = map(int, input().split())
    print(abs(x - y))
#Overall this is what the function does:The function reads two integers x and y from user input. It calculates and prints the absolute difference between these two integers. The function does not accept any parameters and operates with the assumption that the integers provided will meet the constraints 3 ≤ y < x ≤ 100000. However, the function lacks error handling for inputs outside of these constraints, as it assumes valid input is always provided. After execution, the program outputs the non-negative difference between x and y.

