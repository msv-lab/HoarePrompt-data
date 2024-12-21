#State of the program right berfore the function call: a, b, and c are positive integers representing the number of lemons, apples, and pears Nikolay has, respectively, with 1 ≤ a, b, c ≤ 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    min_lemon = min(a, b // 2, c // 4)
    print(min_lemon + min_lemon * 2 + min_lemon * 4)
#Overall this is what the function does:The function reads three integer inputs representing the quantities of lemons, apples, and pears (denoted by `a`, `b`, and `c` respectively). It computes the minimum value among the number of lemons available, half the number of apples, and a quarter of the number of pears. The function then calculates a total based on this minimum value, using the formula `min_lemon + min_lemon * 2 + min_lemon * 4`, which simplifies to `min_lemon * 7`. Finally, it prints this total. The function does not return any value and lacks validation for the input ranges stated in the annotations (1 ≤ a, b, c ≤ 1000), nor does it handle edge cases outside these constraints.

