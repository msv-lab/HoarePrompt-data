#State of the program right berfore the function call: a, b, and c are positive integers representing the number of lemons, apples, and pears respectively, with 1 ≤ a, b, c ≤ 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    min_lemon = min(a, b // 2, c // 4)
    print(min_lemon + min_lemon * 2 + min_lemon * 4)
#Overall this is what the function does:The function accepts no parameters directly and prompts the user to input three positive integers representing the number of lemons (`a`), apples (`b`), and pears (`c`). It calculates the minimum number of complete sets of fruits that can be formed, where each set consists of 1 lemon, 2 apples, and 4 pears. The function prints the total value derived from these sets, which is computed as `min_lemon + min_lemon * 2 + min_lemon * 4`. However, the function does not return any value; it only prints the computed result. All inputs must be between 1 and 1000 inclusive, and the function does not handle cases where the inputs are outside this range.

