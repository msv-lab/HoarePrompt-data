#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, a, b, and c are integers such that 0 <= a, b, c <= 10^9.
def func():
    for s in [*open(0)][1:]:
        a, b, c = map(int, s.split())
        
        b += c
        
        print((a - -b // 3, -1)[c < b % 3])
        
    #State: a series of printed results, one for each test case, where each result is either `a - -b // 3` or `-1` based on the condition `c < b % 3`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of three integers `a`, `b`, and `c`. For each test case, it calculates and prints either `a - -b // 3` or `-1` based on whether `c` is less than `b % 3`.

