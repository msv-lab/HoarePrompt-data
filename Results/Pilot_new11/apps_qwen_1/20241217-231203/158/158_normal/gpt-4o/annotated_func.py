#State of the program right berfore the function call: a, b, and c are non-negative integers such that 1 <= a, b, c <= 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    max_lemons = min(a, b // 2, c // 4)
    total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
    print(total_fruits)
#Overall this is what the function does:The function reads three non-negative integers \(a\), \(b\), and \(c\) (where \(1 \leq a, b, c \leq 1000\)) from the user. It then calculates the maximum number of lemons that can be obtained under the conditions that the number of lemons cannot exceed \(a\), half of \(b\), or one-fourth of \(c\). Based on this maximum number of lemons, it computes the total number of fruits (lemons, twice the number of lemons, and four times the number of lemons) and prints the result. If any of the inputs are outside the specified range, the function will still execute but will raise a `ValueError`.

