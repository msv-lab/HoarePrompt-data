#State of the program right berfore the function call: a, b, and c are non-negative integers such that 1 <= a, b, c <= 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    max_lemons = min(a, b // 2, c // 4)
    total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
    print(total_fruits)
#Overall this is what the function does:The function reads three non-negative integers \(a\), \(b\), and \(c\) from the user, where each integer is between 1 and 1000 inclusive. It then calculates the maximum number of lemons that can be obtained from these integers under the following conditions: \(a\) lemons can be taken directly, \(\frac{b}{2}\) lemons can be obtained from half of \(b\) apples, and \(\frac{c}{4}\) lemons can be obtained from one-fourth of \(c\) oranges. The function prints the total number of fruits (lemons) that can be obtained based on these conditions.

