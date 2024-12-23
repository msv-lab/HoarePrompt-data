#State of the program right berfore the function call: a, b, and c are non-negative integers such that 1 <= a, b, c <= 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    max_lemons = min(a, b // 2, c // 4)
    total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
    print(total_fruits)
#Overall this is what the function does:The function takes three non-negative integer inputs \(a\), \(b\), and \(c\) (where \(1 \leq a, b, c \leq 1000\)), calculates the maximum number of lemons that can be taken under the given conditions (\(a\) lemons, \(\frac{b}{2}\) lemons, and \(\frac{c}{4}\) lemons), and then computes the total number of fruits (lemons, apples, and oranges) that can be obtained based on the maximum number of lemons. It prints the total number of fruits. If any of the inputs are invalid (not integers or outside the specified range), the function will behave unpredictably since it relies on user input and no validation is performed.

