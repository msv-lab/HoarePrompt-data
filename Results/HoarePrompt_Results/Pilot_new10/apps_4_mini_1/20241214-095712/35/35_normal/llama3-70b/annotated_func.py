#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ a + b, a is an integer representing the number of pieces of the first cake (1 ≤ a ≤ 100), and b is an integer representing the number of pieces of the second cake (1 ≤ b ≤ 100).
def func():
    n, a, b = map(int, input().split())
    x = min(n, a, b)
    while True:
        if a >= x and b >= x and a - x + (b - x) >= x:
            break
        
        x -= 1
        
    #State of the program after the loop has been executed: `x` is equal to the maximum integer such that `a >= x`, `b >= x`, and `a - x + (b - x) >= x`, after at most `min(n, a, b)` decrements, `n`, `a`, `b` are integers with the conditions 2 ≤ n ≤ a + b, 1 ≤ a ≤ 100, 1 ≤ b ≤ 100.
    print(x)
#Overall this is what the function does:The function accepts three integers through user input—`n`, `a`, and `b`. It calculates the maximum integer `x` such that `x` does not exceed `n`, is less than or equal to both `a` and `b`, and still allows equal distribution of leftovers (`a - x` and `b - x`) to be at least `x`. The function then prints this calculated value of `x`. There is an implicit precondition that `2 ≤ n ≤ a + b`, `1 ≤ a ≤ 100`, and `1 ≤ b ≤ 100`. The function does not handle input errors, such as non-integer inputs.

