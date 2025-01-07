#State of the program right berfore the function call: the input variables are three positive integers a, b, and c, representing the number of lemons, apples, and pears respectively, such that 1 <= a <= 1000, 1 <= b <= 1000, and 1 <= c <= 1000. The ratio of lemons, apples, and pears is 1:2:4.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    min_lemon = min(a, b // 2, c // 4)
    print(min_lemon + min_lemon * 2 + min_lemon * 4)
#Overall this is what the function does:The function accepts three positive integers representing the number of lemons, apples, and pears, calculates the minimum number of complete sets of fruits that can be formed, and prints the total number of fruits in these sets, without enforcing the 1:2:4 ratio or handling invalid inputs.

