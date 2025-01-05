#State of the program right berfore the function call: a, b, and c are positive integers such that 1 ≤ a, b, c ≤ 10^9.**
def func():
    a, b, c = map(int, raw_input().split())
    print(a + b) + 2 * c
#Overall this is what the function does:The function `func` reads three integers a, b, and c from the user input and prints the sum of a and b added to 2 times c. However, the code has an issue where the addition operation for a and b is not properly enclosed in parentheses, leading to incorrect output. Additionally, the function does not explicitly return any value.

