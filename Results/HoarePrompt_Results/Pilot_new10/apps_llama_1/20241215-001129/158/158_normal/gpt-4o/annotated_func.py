#State of the program right berfore the function call: a, b, and c are positive integers such that 1 <= a, b, c <= 1000, representing the number of lemons, apples, and pears respectively, and the ratio of lemons to apples to pears in the compote should be 1:2:4.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    max_lemons = min(a, b // 2, c // 4)
    total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
    print(total_fruits)
#Overall this is what the function does:The function accepts three positive integers as input, calculates the maximum number of lemons that can be used to make a compote with a 1:2:4 ratio of lemons to apples to pears, calculates the total number of fruits that can be used to make the compote, and prints this total, without explicitly handling invalid inputs or input ranges.

