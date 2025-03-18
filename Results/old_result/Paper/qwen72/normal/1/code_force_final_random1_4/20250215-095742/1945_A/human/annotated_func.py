#State of the program right berfore the function call: a, b, and c are non-negative integers such that 0 <= a, b, c <= 10^9, representing the number of introverts, extroverts, and universals, respectively.
def func():
    for s in [*open(0)][1:]:
        a, b, c = map(int, s.split())
        
        b += c
        
        print((a - -b // 3, -1)[c < b % 3])
        
    #State: After all iterations, `a` is the last integer obtained from splitting and converting the string `s`, `b` is the sum of the original value of `b` and all the values of `c` encountered during the iterations, and `c` is the last integer obtained from splitting and converting the string `s`. The loop iterates over each line from the second line onward of the standard input, and the file must have at least as many lines as the number of iterations.
#Overall this is what the function does:The function reads lines from the standard input starting from the second line. For each line, it splits the line into three integers `a`, `b`, and `c`, where `a` represents the number of introverts, `b` represents the number of extroverts, and `c` represents the number of universals. It then adds the value of `c` to `b` and prints a result based on the condition `(a - -b // 3, -1)[c < b % 3]`. The final state of the program after the function concludes is that `a` and `c` hold the values from the last line processed, and `b` holds the sum of the original value of `b` and all values of `c` encountered during the iterations. The function does not return any value; it only prints the results to the standard output.

