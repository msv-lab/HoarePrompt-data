#State of the program right berfore the function call: a, b, and c are positive integers such that 1 <= a, b, c <= 1000.**
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    min_lemon = min(a, b // 2, c // 4)
    print(min_lemon + min_lemon * 2 + min_lemon * 4)
#Overall this is what the function does:The function `func` prompts the user to input three positive integers a, b, and c where 1 <= a, b, c <= 1000. It then calculates the minimum number of lemons that can be bought based on specific constraints involving a, b, and c. The function prints the total cost of these lemons, which is calculated as min_lemon + min_lemon * 2 + min_lemon * 4. The function does not explicitly return any value.

