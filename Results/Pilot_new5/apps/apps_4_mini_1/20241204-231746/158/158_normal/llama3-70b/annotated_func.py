#State of the program right berfore the function call: a, b, and c are positive integers representing the number of lemons, apples, and pears respectively, where 1 ≤ a, b, c ≤ 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    min_lemon = min(a, b // 2, c // 4)
    print(min_lemon + min_lemon * 2 + min_lemon * 4)
#Overall this is what the function does:The function accepts no parameters and prompts the user to input three positive integers representing the quantities of lemons, apples, and pears. It calculates the minimum number of complete sets of fruits that can be made based on the ratios of 1 lemon, 2 apples, and 4 pears per set. It then prints the total value of these sets, calculated as `min_lemon + min_lemon * 2 + min_lemon * 4`, where `min_lemon` is the minimum number of sets that can be formed. The function does not return any value; it only outputs the result to the console.

