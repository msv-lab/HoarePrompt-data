#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, a, b, and c are integers such that 0 <= a, b, c <= 10^9.
def func():
    for s in [*open(0)][1:]:
        a, b, c = map(int, s.split())
        
        b += c
        
        print((a - -b // 3, -1)[c < b % 3])
        
    #State: the values of a, b, and c from the last test case will be the final values, but the primary output is a series of printed values for each test case.
#Overall this is what the function does:The function reads a number of test cases, each consisting of three integers `a`, `b`, and `c`. For each test case, it computes and prints a specific integer value derived from these inputs. The primary output is a series of printed values corresponding to each test case.

