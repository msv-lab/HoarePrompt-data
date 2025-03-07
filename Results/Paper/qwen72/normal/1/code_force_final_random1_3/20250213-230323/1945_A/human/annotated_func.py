#State of the program right berfore the function call: a, b, and c are non-negative integers such that 0 <= a, b, c <= 10^9, representing the number of introverts, extroverts, and universals, respectively.
def func():
    for s in [*open(0)][1:]:
        a, b, c = map(int, s.split())
        
        b += c
        
        print((a - -b // 3, -1)[c < b % 3])
        
    #State: After all iterations, `a` is the last value read from the input as the first integer in `s`, `b` is the sum of the second integer in `s` and the third integer in `s` for the last iteration, and `c` is the last value read from the input as the third integer in `s`. The loop has processed all lines in the input file except the first line, updating `a`, `b`, and `c` accordingly for each line.
#Overall this is what the function does:The function reads multiple lines of input from standard input (stdin), ignoring the first line. For each subsequent line, it parses three non-negative integers representing the number of introverts (`a`), extroverts (`b`), and universals (`c`). It then updates `b` by adding `c` to it and prints a calculated value based on the updated values of `a` and `b`. The printed value is determined by the expression `(a - -b // 3, -1)[c < b % 3]`, which evaluates to `a - -b // 3` if `c` is less than `b % 3`, otherwise it prints `-1`. After processing all lines, the function does not return any value; it only prints the results to the standard output (stdout). The final state of the program is that the last values of `a`, `b`, and `c` read from the input are retained, but these are not returned or used outside the function.

