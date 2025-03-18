#State of the program right berfore the function call: a, b, and c are positive integers representing the number of lemons, apples, and pears respectively, with the constraints 1 ≤ a, b, c ≤ 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    max_lemons = min(a, b // 2, c // 4)
    total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
    print(total_fruits)
#Overall this is what the function does:The function accepts three positive integer inputs representing the number of lemons (`a`), apples (`b`), and pears (`c`). It calculates the maximum number of sets of fruits that can be made, where each set consists of 1 lemon, 2 apples, and 4 pears, based on the available quantities. The function then computes the total number of fruits in these sets and prints that total. Note that the function does not have defined return values; instead, it prints the result directly.

