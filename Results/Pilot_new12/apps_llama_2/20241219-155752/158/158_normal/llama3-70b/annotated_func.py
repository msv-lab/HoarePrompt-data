#State of the program right berfore the function call: The input consists of three positive integers a, b, and c, where 1 ≤ a, b, c ≤ 1000, representing the number of lemons, apples, and pears Nikolay has, respectively.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    min_lemon = min(a, b // 2, c // 4)
    print(min_lemon + min_lemon * 2 + min_lemon * 4)
#Overall this is what the function does:The function reads three positive integers from the user, representing the number of lemons, apples, and pears, and calculates the minimum number of lemons that can be used based on the available fruits. It then prints the total number of fruits that can be used to make a juice, assuming 1 lemon, 2 apples, and 4 pears are needed for each juice. The function does not handle cases where the input values are not within the specified range of 1 to 1000 or are not positive integers, and it does not return any value, only prints the result. The state of the program after it concludes is that the user has been presented with the maximum number of juices that can be made with the available fruits, and the original input values of lemons, apples, and pears remain unchanged.

