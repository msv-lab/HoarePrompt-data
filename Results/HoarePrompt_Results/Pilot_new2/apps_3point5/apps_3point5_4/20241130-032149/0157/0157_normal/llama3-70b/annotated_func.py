#State of the program right berfore the function call: a, b, and c are positive integers such that 1 <= a, b, c <= 1000.**
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    min_lemon = min(a, b // 2, c // 4)
    print(min_lemon + min_lemon * 2 + min_lemon * 4)
#Overall this is what the function does:The function does not accept any parameters. It reads three positive integers a, b, and c from the user input (1 <= a, b, c <= 1000). It then calculates the minimum of a, b divided by 2, and c divided by 4, assigns it to min_lemon, and prints the result of min_lemon added to itself multiplied by 2 and 4.

