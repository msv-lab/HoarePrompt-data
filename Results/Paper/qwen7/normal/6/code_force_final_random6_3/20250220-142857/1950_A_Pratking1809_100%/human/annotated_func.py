#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
def func():
    q = int(input())
    for i in range(q):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: Output State: `t` is an integer such that \(1 \leq t \leq 1000\), `q` is an integer greater than or equal to 1, `i` is 3, `a`, `b`, and `c` are integers obtained from the last input provided during the loop's execution, and the values of `t`, `q`, `i`, `a`, `b`, and `c` remain unchanged after the loop finishes.
    #
    #In simpler terms, after the loop has completed all its iterations, `t` will still be between 1 and 1000, `q` will still be at least 1, `i` will be set to 3 (indicating the loop has run three times), and `a`, `b`, and `c` will contain the values from the last set of inputs provided. The loop has processed all inputs up to the third iteration, but since no further inputs are expected, the values of `t`, `q`, `i`, `a`, `b`, and `c` do not change.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \(a\), \(b\), and \(c\) within the range 0 to 9, and an integer \(t\) within the range 1 to 1000. For each test case, it prints 'STAIR' if \(a < b < c\), 'PEAK' if \(a < b > c\), and 'NONE' otherwise. After processing all test cases, the function does not return any value.

