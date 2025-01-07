#State of the program right berfore the function call: a, b, and c are positive integers representing the number of lemons, apples, and pears respectively, where 1 ≤ a, b, c ≤ 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    max_lemons = min(a, b // 2, c // 4)
    total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
    print(total_fruits)
#Overall this is what the function does:The function accepts three integer inputs representing the number of lemons (a), apples (b), and pears (c). It calculates the maximum possible number of sets of fruit that can be made, where each set requires 1 lemon, 2 apples, and 4 pears. The total number of fruits used in these sets is then printed. The function does not return any value and does not handle invalid inputs or situations where the maximum number of sets is zero.

