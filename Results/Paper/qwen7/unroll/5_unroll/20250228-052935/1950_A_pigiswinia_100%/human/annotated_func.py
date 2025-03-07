#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
def func():
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: Output State: The output state will consist of 'STAIR', 'PEAK', or 'NONE' printed for each iteration of the loop based on the input values provided for `a`, `b`, and `c`. Specifically, it will print 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. The exact sequence of these outputs depends on the inputs given during each iteration of the loop.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \(a\), \(b\), and \(c\) within the range 0 to 9. For each test case, it prints 'STAIR' if \(a < b < c\), 'PEAK' if \(a < b > c\), and 'NONE' otherwise. The function does not return any value but prints the results for each test case.

