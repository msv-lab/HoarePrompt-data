#State of the program right berfore the function call: x is a positive integer such that 1 ≤ x ≤ 1,000,000.
def func():
    print(input() + 4) / 5
#Overall this is what the function does:The function does not accept any parameters and attempts to read input, add 4 to it, and divide the result by 5. However, it does not return any value, and the input is not validated, so if the input is not a number, it will raise a runtime error. Additionally, the print statement will output the result of the operation instead of returning it. Therefore, the function's behavior is to print an unvalidated result of the arithmetic operation without returning anything.

