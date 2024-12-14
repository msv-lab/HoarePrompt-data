#State of the program right berfore the function call: n is an integer such that 1 <= n <= 10^9.
def func_1(n):
    min_segments_needed = float('inf')
    for a in range(1, int(math.sqrt(n)) + 1):
        b = (n + a - 1) // a
        
        segments_needed = 2 * (a + b)
        
        min_segments_needed = min(min_segments_needed, segments_needed)
        
    #State of the program after the  for loop has been executed: `min_segments_needed` is the minimum segments needed for all `a` from 1 to `int(math.sqrt(n))`, `b` is the corresponding maximum integer value calculated for the last executed `a`, and `segments_needed` is equal to the minimum segments calculated from the last iteration; `n` is an integer such that 1 <= n <= 10^9.
    return min_segments_needed
    #The program returns the minimum segments needed for all `a` from 1 to `int(math.sqrt(n))`
#Overall this is what the function does:The function accepts an integer `n` (where 1 <= n <= 10^9) and calculates the minimum number of segments needed based on possible values of `a` from 1 to the integer square root of `n`. For each value of `a`, it computes the corresponding value of `b`, determining the number of segments required, and returns the minimum segments needed across all iterations.

