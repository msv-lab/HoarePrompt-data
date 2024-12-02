#State of the program right berfore the function call: a, b, and c are positive integers representing the number of lemons, apples, and pears respectively, with 1 ≤ a, b, c ≤ 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    min_lemon = min(a, b // 2, c // 4)
    print(min_lemon + min_lemon * 2 + min_lemon * 4)
#Overall this is what the function does:The function reads three positive integers representing the number of lemons, apples, and pears, computes the maximum number of complete sets of fruits that can be created, and prints the total number of fruits used in those sets. It does not handle invalid input cases, such as non-positive integers or non-integer values.

