#State of the program right berfore the function call: a, b, and c are positive integers representing the number of lemons, apples, and pears respectively, with values 1 ≤ a, b, c ≤ 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    min_lemon = min(a, b // 2, c // 4)
    print(min_lemon + min_lemon * 2 + min_lemon * 4)
#Overall this is what the function does:The function accepts three positive integers a, b, and c, representing the number of lemons, apples, and pears respectively. It calculates the minimum number of complete sets of fruit that can be formed based on the available quantities, where each set requires 1 lemon, 2 apples, and 4 pears. The function then prints the total value of these sets: `min_lemon` sets yield `min_lemon + min_lemon * 2 + min_lemon * 4` as the total. However, the function does not return any value; it only prints the result. Additionally, there are no checks for the input values being within the specified range, which means if the input values are outside the range of 1 to 1000, it could lead to unexpected results.

