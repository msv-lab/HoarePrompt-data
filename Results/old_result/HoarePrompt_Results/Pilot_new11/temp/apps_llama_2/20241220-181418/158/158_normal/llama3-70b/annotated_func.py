#State of the program right berfore the function call: a, b, and c are positive integers representing the number of lemons, apples, and pears respectively, where 1 <= a, b, c <= 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    min_lemon = min(a, b // 2, c // 4)
    print(min_lemon + min_lemon * 2 + min_lemon * 4)
#Overall this is what the function does:The function reads three positive integers from the user, representing the number of lemons, apples, and pears, calculates the minimum quantity that can be used to make a lemon-apple-pear combination (with a ratio of 1:2:4), and prints the total quantity of the combination. The function does not validate if the input integers are within the specified range of 1 to 1000, and it does not handle cases where the user inputs non-integer or non-positive values. The function's output is the total quantity of the combination, which is the sum of the minimum quantity of lemons, twice the minimum quantity of lemons (representing apples), and four times the minimum quantity of lemons (representing pears). The function does not return any value, as it prints the result directly to the console.

