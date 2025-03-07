#State of the program right berfore the function call: a, b, and c are non-negative integers such that 0 <= a, b, c <= 10^9, representing the number of introverts, extroverts, and universals, respectively.
def func():
    for s in [*open(0)][1:]:
        a, b, c = map(int, s.split())
        
        b += c
        
        print((a - -b // 3, -1)[c < b % 3])
        
    #State: a, b, and c remain unchanged, but the loop prints a series of values based on the condition (a - -b // 3, -1)[c < b % 3] for each iteration.
#Overall this is what the function does:The function `func` reads lines from standard input (excluding the first line), where each line contains three non-negative integers `a`, `b`, and `c` representing the number of introverts, extroverts, and universals, respectively. For each line, it calculates a value based on the formula `(a - -b // 3, -1)[c < b % 3]` and prints this value. The function does not modify the input variables `a`, `b`, and `c` and does not return any value.

