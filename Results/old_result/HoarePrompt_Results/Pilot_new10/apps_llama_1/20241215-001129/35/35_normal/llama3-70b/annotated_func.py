#State of the program right berfore the function call: n, a, and b are integers such that n is the number of people (including Ivan) at the celebration, a is the number of pieces of the first cake, and b is the number of pieces of the second cake, where 1 ≤ a, b ≤ 100 and 2 ≤ n ≤ a + b.
def func():
    n, a, b = map(int, input().split())
    x = min(n, a, b)
    while True:
        if a >= x and b >= x and a - x + (b - x) >= x:
            break
        
        x -= 1
        
    #State of the program after the loop has been executed: `n` is the number of people at the celebration, `a` is the number of pieces of the first cake, `b` is the number of pieces of the second cake, and `x` is the largest value such that `a >= x`, `b >= x`, and `a - x + (b - x) >= x` are all true, which represents the maximum number of pieces that can be distributed under the given conditions.
    print(x)
#Overall this is what the function does:The function calculates and prints the maximum number of cake pieces that can be distributed among a specified number of people, considering the number of pieces of two different cakes, such that each cake has at least the distributed number of pieces and the remaining pieces from both cakes combined are at least the distributed number of pieces.

