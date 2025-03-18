#State of the program right berfore the function call: a, b, and c are positive integers such that 1 ≤ a, b, c ≤ 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    min_lemon = min(a, b // 2, c // 4)
    print(min_lemon + min_lemon * 2 + min_lemon * 4)
#Overall this is what the function does:The function accepts three positive integers via standard input (a, b, and c), computes the minimum of a, b/2, and c/4, and prints the result of `min_lemon + min_lemon * 2 + min_lemon * 4`, which effectively calculates and displays the total quantity derived from `min_lemon` in a specific formula. The function does not return any values; it only prints the output.

