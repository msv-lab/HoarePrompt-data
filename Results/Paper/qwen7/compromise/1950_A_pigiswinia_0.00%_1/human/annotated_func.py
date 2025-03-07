#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
def func():
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIRS')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: Output State: The output state will consist of 'STAIRS', 'PEAK', or 'NONE' printed for each iteration of the loop based on the input values of `a`, `b`, and `c`. The exact sequence of these outputs cannot be determined without knowing the specific inputs provided during each iteration.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \(a\), \(b\), and \(c\) within the range 0 to 9, and an integer \(t\) indicating the number of test cases (with \(1 \leq t \leq 1000\)). For each test case, it prints either 'STAIRS', 'PEAK', or 'NONE' based on the relative values of \(a\), \(b\), and \(c\). After processing all test cases, the function does not return any value.

