#State of the program right berfore the function call: the inputs are positive integers, a (number of lemons), b (number of apples), and c (number of pears), such that 1 <= a, b, c <= 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    max_lemons = min(a, b // 2, c // 4)
    total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
    print(total_fruits)
#Overall this is what the function does:The function takes three positive integers as inputs from the user, representing the number of lemons, apples, and pears, and calculates the maximum number of lemons that can be used to make a fruit combination where each combination consists of 1 lemon, 2 apples, and 4 pears. It then calculates the total number of fruits in this combination and prints the result. The function does not handle cases where the input values are not positive integers or are outside the range of 1 to 1000, and it does not provide any error messages for invalid inputs. The final state of the program is that it has printed the total number of fruits in the calculated combination, without modifying the original input values or retaining any information about the input or calculation beyond the printed output.

