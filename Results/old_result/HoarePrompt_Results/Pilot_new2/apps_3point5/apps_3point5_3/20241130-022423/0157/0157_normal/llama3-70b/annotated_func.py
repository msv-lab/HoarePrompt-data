#State of the program right berfore the function call: a, b, and c are positive integers such that 1 ≤ a, b, c ≤ 1000.**
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    min_lemon = min(a, b // 2, c // 4)
    print(min_lemon + min_lemon * 2 + min_lemon * 4)
#Overall this is what the function does:The function `func` reads three positive integers a, b, and c (1 ≤ a, b, c ≤ 1000) as input. It then calculates the minimum value among a, b divided by 2, and c divided by 4. Finally, it prints the result of adding this minimum value with itself multiplied by 2 and 4. The function does not explicitly return a value.

