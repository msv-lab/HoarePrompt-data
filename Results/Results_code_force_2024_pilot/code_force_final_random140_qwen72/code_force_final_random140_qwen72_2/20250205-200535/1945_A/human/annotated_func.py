#State of the program right berfore the function call: a, b, and c are non-negative integers such that 0 <= a, b, c <= 10^9, representing the number of introverts, extroverts, and universals, respectively.
def func():
    for line in [*open(0)][1:]:
        p, q, r = map(int, line.split())
        
        q += r
        
        print((p - q // 3, -1)[r < q % 3])
        
    #State: `a`, `b`, and `c` are non-negative integers such that 0 <= a, b, c <= 10^9, `p` is the first integer from the last line processed in the file, `q` is the sum of the second integer from the last line processed in the file and the third integer from the last line processed in the file, `r` is the third integer from the last line processed in the file, and the file has been fully read with no more lines remaining.
#Overall this is what the function does:The function reads lines from the standard input (stdin), excluding the first line, and processes each line to extract three integers `p`, `q`, and `r`. It then calculates a new value `q` by adding `r` to the original `q`. The function prints a result based on the condition `r < q % 3`. If `r` is less than `q % 3`, the function prints `-1`; otherwise, it prints `p - q // 3`. After processing all lines, the function completes, and the file is fully read with no more lines remaining. The function does not accept any parameters and does not return any values.

