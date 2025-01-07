#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ a + b, a is an integer representing the number of pieces of the first cake (1 ≤ a ≤ 100), and b is an integer representing the number of pieces of the second cake (1 ≤ b ≤ 100).
def func():
    n, a, b = map(int, input().split())
    x = min(n, a, b)
    while True:
        if a >= x and b >= x and a - x + (b - x) >= x:
            break
        
        x -= 1
        
    #State of the program after the loop has been executed: `x` is a non-negative integer, where the original value of `x` was equal to min(`n`, `a`, `b`) and has been decreased until either `a >= x`, `b >= x`, and `a - x + (b - x) >= x` holds true, or `x` reaches 0. If the loop executed successfully, then the final values of `a` and `b` must remain greater than or equal to the final value of `x`. If `x` reaches 0 without breaking, the last values of `a` and `b` still fulfill the balance condition for at least one piece from both cakes.
    print(x)
#Overall this is what the function does:The function reads three integers, \(n\), \(a\), and \(b\), from user input. It determines the maximum number \(x\) of cake pieces that can be distributed such that there are enough pieces available from both cakes to satisfy the conditions: both cakes must have at least \(x\) pieces left after distribution, and the total remaining pieces after distribution must also be at least \(x\). The value \(x\) starts from the minimum of \(n\), \(a\), and \(b\) and decreases until these conditions are met or until \(x\) reaches zero. The function then outputs the determined value of \(x\

