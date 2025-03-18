#State of the program right berfore the function call: The function should take three non-negative integers a, b, and c as input, where 0 <= a, b, c <= 10^9, representing the number of introverts, extroverts, and universals, respectively.
def func():
    for s in [*open(0)][1:]:
        a, b, c = map(int, s.split())
        
        b += c
        
        print((a - -b // 3, -1)[c < b % 3])
        
    #State: The function will print a series of outputs, each corresponding to a line of input from the file. For each line, it will print the value of `a - -b // 3` if `c` is not less than `b % 3`, otherwise it will print `-1`. The values of `a`, `b`, and `c` will be updated for each line, but the final state of these variables after the loop will depend on the last line of input.
#Overall this is what the function does:The function reads from standard input, ignoring the first line, and processes each subsequent line. Each line is expected to contain three non-negative integers `a`, `b`, and `c`. For each line, the function updates `b` by adding `c` to it, then prints a value based on the condition `c >= b % 3`. If the condition is true, it prints `a - -b // 3`; otherwise, it prints `-1`. The function does not return any value, but it prints the result for each line of input. The final state of the program after the function concludes is that all lines from the input have been processed and the corresponding results have been printed.

