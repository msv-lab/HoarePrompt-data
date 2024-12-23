#State of the program right berfore the function call: n is an integer such that 1 <= n <= 10^9.
def func_1(n):
    min_segments_needed = float('inf')
    for a in range(1, int(math.sqrt(n)) + 1):
        b = (n + a - 1) // a
        
        segments_needed = 2 * (a + b)
        
        min_segments_needed = min(min_segments_needed, segments_needed)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 10^9\); `min_segments_needed` is the minimum value of `2 * (a + b)` for all `a` in the range \(1 \leq a \leq \text{int}(\sqrt{n}) + 1`
    return min_segments_needed
    #`The program returns the minimum value of 2 * (a + b) for all a in the range 1 to int(sqrt(n)) + 1`
#Overall this is what the function does:The function `func_1` accepts an integer `n` such that \(1 \leq n \leq 10^9\) and returns the minimum value of \(2 \times (a + b)\) for all integers `a` in the range \(1 \leq a \leq \text{int}(\sqrt{n}) + 1\). For each `a`, `b` is calculated as \((n + a - 1) // a\). The function iterates over all possible values of `a` in the given range and updates `min_segments_needed` to the smallest value of \(2 \times (a + b)\) found during the iteration. The function handles the case where `n` is exactly a perfect square, ensuring that `a` can reach \(\text{int}(\sqrt{n}) + 1\).

