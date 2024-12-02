#State of the program right berfore the function call: 
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    min_lemon = min(a, b // 2, c // 4)
    print(min_lemon + min_lemon * 2 + min_lemon * 4)
#Overall this is what the function does:The function `func` takes three integer inputs `a`, `b`, and `c` from the user. It calculates the minimum number of lemons that can be bought with these inputs based on a specific formula. However, the code does not return any value. Therefore, the functionality of the function `func` is to calculate the minimum number of lemons based on the inputs provided and print the result without returning any value.

