#State of the program right berfore the function call: a, b, and c are positive integers representing the number of lemons, apples, and pears respectively, with 1 ≤ a, b, c ≤ 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    min_lemon = min(a, b // 2, c // 4)
    print(min_lemon + min_lemon * 2 + min_lemon * 4)
#Overall this is what the function does:The function accepts three positive integers as input: the number of lemons (a), apples (b), and pears (c). It calculates the minimum quantity of lemonade that can be made based on the number of apples and pears, where each apple can make 2 servings and each pear can make 4 servings. The function then outputs the total number of servings possible, which is computed as the minimum servings multiplied by a factor of 7 (1 for lemons, 2 for apples, and 4 for pears). The function does not return any value; it only prints the result. Importantly, since the inputs are taken from user input, there are no parameters to the function itself.

