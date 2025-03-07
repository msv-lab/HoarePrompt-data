#State of the program right berfore the function call: a, b, and c are non-negative integers such that 0 <= a, b, c <= 10^9, representing the number of introverts, extroverts, and universals, respectively.
def func():
    for s in [*open(0)][1:]:
        a, b, c = map(int, s.split())
        
        b += c
        
        print((a - -b // 3, -1)[c < b % 3])
        
    #State: After the loop has executed all iterations, `a`, `b`, and `c` will be the values from the last line of the input file. Additionally, `b` will be the sum of the original `b` and `c` values from each line of the input file. The loop will have printed a series of outputs based on the condition `(a - -b // 3, -1)[c < b % 3]` for each line of input.
#Overall this is what the function does:The function reads multiple lines of input from standard input (stdin), where each line contains three non-negative integers `a`, `b`, and `c`. For each line, it updates `b` by adding `c` to it, then computes and prints a value based on the condition `(a - -b // 3, -1)[c < b % 3]`. After processing all lines, the final values of `a`, `b`, and `c` will be those from the last line of the input, with `b` being the sum of the original `b` and `c` from that line. The function does not return any value; its primary action is to print the computed results for each line of input.

