#State of the program right berfore the function call: a, b, and c are non-negative integers such that 0 <= a, b, c <= 10^9, representing the number of introverts, extroverts, and universals, respectively.
def func():
    for line in [*open(0)][1:]:
        p, q, r = map(int, line.split())
        
        q += r
        
        print((p - q // 3, -1)[r < q % 3])
        
    #State: After all iterations of the loop, `a`, `b`, and `c` remain non-negative integers such that 0 <= a, b, c <= 10^9. The variable `q` is the sum of all third integers (`r`) from each line in the file, and the loop has processed all lines in the file except the first one. For each line, the expression `(p - q // 3, -1)[r < q % 3]` has been printed, where `p` is the first integer, `q` is the updated sum of the second and third integers, and `r` is the third integer from the current line.
#Overall this is what the function does:The function reads from standard input (or a file), ignoring the first line, and processes each subsequent line. Each line is expected to contain three integers `p`, `q`, and `r`. The function updates `q` by adding `r` to it, then prints a value based on the condition `r < q % 3`. If `r` is less than `q % 3`, it prints `-1`; otherwise, it prints `p - q // 3`. The function does not modify the input parameters `a`, `b`, and `c`, and it does not return any value. The final state of the program is that all lines in the input have been processed, and the appropriate values have been printed for each line.

