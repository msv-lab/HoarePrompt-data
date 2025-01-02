#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 3·10^5, and x1, x2, ..., xn are distinct integers such that 1 ≤ xi ≤ 10^9.
def func():
    n = int(raw_input())
    s = sorted(map(int, raw_input().split()))
    r = 0
    for i in xrange(n):
        r += s[i] * (2 ** (n - 1 - i) - 1 - (2 ** i - 1)) % (1000000000 + 7)
        
    #State of the program after the  for loop has been executed: `n` is an integer within the range \( 1 \leq n \leq 3 \times 10^5 \), `s` is a sorted list of integers, `r` is the sum of each element in the list \( s \) multiplied by its corresponding term derived from the loop \(\sum_{i=0}^{n-1} s[i] \cdot 2^i \cdot (2^{(n - 2i - 1)} - 1) \mod (1000000000 + 7)\).
    print - r
#Overall this is what the function does:The function accepts an input integer `n` representing the length of a list `x` (1 ≤ n ≤ 3·10^5) and a list `x` of `n` distinct integers (1 ≤ xi ≤ 10^9). It first reads `n` and the list `x` from standard input, then sorts the list `x`. Next, it computes the sum of each element in the sorted list `x` multiplied by a term derived from the loop index, specifically \( \sum_{i=0}^{n-1} x[i] \cdot 2^i \cdot (2^{(n - 2i - 1)} - 1) \mod (1000000000 + 7) \). Finally, it prints the negative of this computed value. Potential edge cases include the input list violating the constraints on `n` or the elements of `x`. If these constraints are violated, the function's behavior is undefined based on the provided code.

