#State of the program right berfore the function call: **Precondition**: **a, b, and c are positive integers such that 1 ≤ a,b,c ≤ 1000.**
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    min_lemon = min(a, b // 2, c // 4)
    print(min_lemon + min_lemon * 2 + min_lemon * 4)
#Overall this is what the function does:The function `func` prompts the user to input three positive integers `a`, `b`, and `c`. It then calculates the minimum number of lemons that can be bought given the constraints that 1 ≤ a, b, c ≤ 1000. The function computes the total cost of purchasing these lemons and prints the result, which is the sum of the minimum number of lemons needed at different prices. The function does not have a specific return value specified.

