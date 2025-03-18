#State of the program right berfore the function call: a, b, and c are positive integers representing the number of lemons, apples, and pears respectively, where 1 ≤ a, b, c ≤ 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    max_lemons = min(a, b // 2, c // 4)
    total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
    print(total_fruits)
#Overall this is what the function does:The function accepts three positive integer inputs representing the number of lemons, apples, and pears. It calculates the maximum number of "fruit combinations" that can be made using the available fruits, where each combination requires 1 lemon, 2 apples, and 4 pears. The function then computes the total number of fruits used in these combinations and prints this total, which is derived from the maximum number of combinations multiplied by 1 (lemons), 2 (apples), and 4 (pears). The function does not explicitly return any values; it only prints the result.

