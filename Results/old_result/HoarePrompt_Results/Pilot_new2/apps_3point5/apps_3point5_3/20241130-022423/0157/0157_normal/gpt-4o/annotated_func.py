#State of the program right berfore the function call: 
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    max_lemons = min(a, b // 2, c // 4)
    total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
    print(total_fruits)
#Overall this is what the function does:The function func prompts the user to input three integer values. It calculates the maximum number of lemons that can be obtained based on certain conditions using the minimum of `a`, `b` divided by 2, and `c` divided by 4. Then, it computes the total number of fruits by multiplying the maximum lemons by 1, 2, and 4 respectively, and prints the result. The function does not accept any parameters and solely relies on user input for the calculations.

