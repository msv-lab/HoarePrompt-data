#State of the program right berfore the function call: a, b, and c are positive integers representing the number of lemons, apples, and pears respectively, with values in the range 1 ≤ a, b, c ≤ 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    max_lemons = min(a, b // 2, c // 4)
    total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
    print(total_fruits)
#Overall this is what the function does:The function accepts three positive integers representing the number of lemons (`a`), apples (`b`), and pears (`c`). It calculates the maximum number of complete sets of fruits that can be made using the available lemons (1 per set), apples (2 per set), and pears (4 per set), and then calculates the total number of fruits in those sets. The function prints the total number of fruits, but it does not return any value. It also does not handle any input validation or exceptions, meaning if the inputs are not integers or are out of the specified range, the function could fail or produce unexpected results.

