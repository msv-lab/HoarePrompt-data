#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, a, b, and c are integers such that 0 <= a, b, c <= 10^9.
def func():
    for s in [*open(0)][1:]:
        a, b, c = map(int, s.split())
        
        b += c
        
        print((a - -b // 3, -1)[c < b % 3])
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `a` is the integer from the last test case, `b` is the sum of the second and third integers from the last test case, and `c` is the third integer from the last test case.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of three integers `a`, `b`, and `c`. For each test case, it calculates a value based on the formula `(a - -(b + c) // 3, -1)[c < (b + c) % 3]` and prints the result.

