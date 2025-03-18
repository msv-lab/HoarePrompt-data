#State of the program right berfore the function call: a, b, and c are non-negative integers such that 0 <= a, b, c <= 10^9, representing the number of introverts, extroverts, and universals, respectively.
def func():
    for s in [*open(0)][1:]:
        a, b, c = map(int, s.split())
        
        b += c
        
        print((a - -b // 3, -1)[c < b % 3])
        
    #State: a, b, and c are non-negative integers such that 0 <= a, b, c <= 10^9, but the value of the expression (a - -b // 3, -1)[c < b % 3] is printed for each line of input after the first line. The values of a, b, and c are updated for each iteration based on the input, and b is incremented by c.
#Overall this is what the function does:The function reads lines from the standard input, starting from the second line. For each line, it parses three non-negative integers `a`, `b`, and `c`, representing the number of introverts, extroverts, and universals, respectively. It then increments `b` by `c` and prints a value based on the condition `c < b % 3`. If the condition is true, it prints `-1`; otherwise, it prints `a - -b // 3`. The function does not return any value, but it processes and prints a result for each line of input after the first line.

